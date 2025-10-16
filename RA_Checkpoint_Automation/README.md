# RA Checkpoint Automation Tool

A Python web scraper and automation tool to help Resident Assistants (RAs) automatically fill out repetitive forms for their residents.

## Features

- **CSV Data Integration**: Loads resident data from a CSV file
- **Form Automation**: Automatically fills out web forms using Selenium WebDriver
- **Smart Field Detection**: Automatically detects and fills various form field types:
  - Date pickers
  - Dropdown selectors
  - Multiple choice questions (with random selection)
- **Error Handling**: Robust error handling and logging
- **Configurable**: Easy to customize for different forms

## Installation

1. Install Python 3.7 or higher
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. **Update Configuration**: Edit `config.py` to match your form:
   - Set the correct `FORM_URL`
   - Update field mappings based on your form's HTML structure
   - Adjust CSV column mappings

2. **Prepare CSV Data**: Update `residents.csv` with your resident data:
   - Include columns for all form fields
   - Add `_count` columns for multiple choice questions to specify how many options to select

3. **Test Form Structure**: Run the tool once to see what fields it can detect and adjust selectors as needed

## Usage

### Basic Usage
```python
python Automater.py
```

### Custom Usage
```python
from Automater import RACheckpointAutomator

automator = RACheckpointAutomator(
    csv_file="your_residents.csv",
    form_url="https://your-form-url.com",
    headless=False  # Set to True for headless mode
)

automator.run_automation()
```

## CSV Format

Your CSV file should include columns for each form field. Example:

```csv
name,date,status,room,floor,building,year,concerns_count,activities_count
John Smith,2024-01-15,Active,101,1,North Hall,Freshman,1,2
Jane Doe,2024-01-15,Active,205,2,South Hall,Sophomore,0,1
```

### Multiple Choice Questions
For multiple choice questions, add a `_count` column to specify how many options to select:
- `0`: Select no options
- `1`: Select 1 random option
- `2`: Select 2 random options
- Leave empty: Randomly select 0-2 options

## Customization

### Form Field Detection
The tool uses CSS selectors to find form fields. Update the selectors in `config.py` based on your form's HTML structure.

### Field Mappings
Map your CSV columns to form fields in the `CSV_MAPPINGS` section of `config.py`.

### Random Selection
Configure random selection behavior in the `RANDOM_SELECTION` section of `config.py`.

## Logging

The tool creates detailed logs in `automation.log` and displays progress in the console.

## Troubleshooting

1. **Form Fields Not Found**: Update the CSS selectors in `config.py`
2. **Chrome Driver Issues**: The tool automatically downloads the correct Chrome driver
3. **Form Submission Issues**: Check the submit button selectors in `config.py`
4. **CSV Loading Issues**: Ensure your CSV file exists and has the correct column names

## Safety Features

- **Error Recovery**: Continues processing even if one resident fails
- **Logging**: Detailed logs for debugging
- **Validation**: Checks for required data before processing
- **Graceful Shutdown**: Properly closes browser even on errors

## Legal and Ethical Considerations

- Only use this tool for legitimate administrative purposes
- Ensure you have permission to automate form filling
- Respect website terms of service
- Use responsibly and ethically
