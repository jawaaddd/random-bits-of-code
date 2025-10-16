import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import re
from email.mime.text import MIMEText
import base64

# ------------Some boilerplate API setup taken from Google's docs----------------

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
def get_gmail_service():
    """Gets or creates Gmail API credentials and returns the service."""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)
# -------------------------------------------------------------------------------

# Determines if an email is news-related based on subject and sender
def is_news_email(subject, sender):
    # List of common news-related keywords
    news_keywords = ['news', 'breaking', 'headline', 'report', 'journal', 'times', 'post', 'tribune', 'gazette']
    
    # List of common news domains
    news_domains = ['reuters.com', 'apnews.com', 'bloomberg.com', 'nytimes.com', 'washingtonpost.com', 
                   'theguardian.com', 'bbc.com', 'cnn.com', 'wsj.com', 'economist.com']
    
    # Check subject for news keywords
    subject_lower = subject.lower()
    if any(keyword in subject_lower for keyword in news_keywords):
        return True
    
    # Check sender domain
    sender_domain = sender.split('@')[-1].lower()
    if any(domain in sender_domain for domain in news_domains):
        return True
    
    return False

# Process unread emails and add 'News' label to news-related emails
def process_unread_emails():
    service = get_gmail_service()
    
    # Get all unread messages
    results = service.users().messages().list(
        userId='me',
        labelIds=['UNREAD'],
        maxResults=100  # Adjust this number as needed
    ).execute()
    
    messages = results.get('messages', [])
    
    if not messages:
        print('No unread messages found.')
        return
    
    # Create 'News' label if it doesn't exist
    try:
        service.users().labels().create(
            userId='me',
            body={'name': 'News'}
        ).execute()
    except:
        pass  # Label might already exist
    
    # Get the 'News' label ID
    labels = service.users().labels().list(userId='me').execute()
    news_label_id = next(label['id'] for label in labels['labels'] if label['name'] == 'News')
    
    for message in messages:
        msg = service.users().messages().get(
            userId='me',
            id=message['id'],
            format='metadata',
            metadataHeaders=['From', 'Subject']
        ).execute()
        
        headers = msg['payload']['headers']
        subject = next(h['value'] for h in headers if h['name'] == 'Subject')
        sender = next(h['value'] for h in headers if h['name'] == 'From')
        
        if is_news_email(subject, sender):
            # Add 'News' label to the message
            service.users().messages().modify(
                userId='me',
                id=message['id'],
                body={'addLabelIds': [news_label_id]}
            ).execute()
            print(f'Added News label to email: {subject}')

if __name__ == '__main__':
    process_unread_emails()
