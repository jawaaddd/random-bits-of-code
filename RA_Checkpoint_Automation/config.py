"""
Configuration file for RA Checkpoint Automation
Customize these settings based on your specific form
"""

# Form Configuration
FORM_URL = "https://your-form-url.com"  # Replace with actual form URL

# CSV Configuration
CSV_FILE = "residents.csv"

# Browser Configuration
HEADLESS_MODE = False  # Set to True to run without browser window
BROWSER_WAIT_TIME = 10  # Implicit wait time in seconds

# Form Field Mappings
# Update these based on your actual form field names/IDs
FORM_FIELDS = {
    'date_picker': [
        "input[type='date']",
        "input[name*='date']",
        "input[id*='date']",
        ".date-picker",
        "#date"
    ],
    'dropdown_fields': [
        'status', 'room', 'floor', 'building', 'year', 'major', 'program'
    ],
    'multiple_choice_fields': [
        'concerns', 'activities', 'preferences', 'interests', 'needs'
    ],
    'submit_button': [
        "input[type='submit']",
        "button[type='submit']",
        "button:contains('Submit')",
        "input[value*='Submit']",
        ".submit-button",
        "#submit"
    ]
}

# CSV Column Mappings
# Map CSV columns to form fields
CSV_MAPPINGS = {
    'name': 'name',  # Used for logging
    'date': 'date',
    'status': 'status',
    'room': 'room',
    'floor': 'floor',
    'building': 'building',
    'year': 'year',
    'concerns_count': 'concerns_count',
    'activities_count': 'activities_count',
    'preferences_count': 'preferences_count'
}

# Random Selection Settings
RANDOM_SELECTION = {
    'min_selections': 0,
    'max_selections': 2,
    'default_selections': None  # None means random between min and max
}
