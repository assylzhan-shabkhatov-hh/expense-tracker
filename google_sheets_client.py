import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
from datetime import datetime
import os
from jusan_extract_pdf import extract_text_from_pdf

# Load environment variables from the .env file
load_dotenv()

# Define the scope of the access required
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Authenticate using the credentials from the downloaded JSON key file
service_account_json_path  = os.getenv("SERVICE_ACCOUNT_JSON_PATH")
creds = ServiceAccountCredentials.from_json_keyfile_name(service_account_json_path , scope)

# Authorize the client with the credentials
client = gspread.authorize(creds)

# Open the Google Spreadsheet by its title or URL
spreadsheet_url = os.getenv("GOOGLE_SHEET_URL") 
spreadsheet = client.open_by_url(spreadsheet_url)

def get_or_create_worksheet(worksheet_name):
    try:
        worksheet = spreadsheet.worksheet(worksheet_name)
    except gspread.exceptions.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(worksheet_name, rows=1000, cols=100)
    return worksheet

JUSAN_PDF_PATH = os.getenv("JUSAN_PDF_PATH")
if(JUSAN_PDF_PATH):
    pdf_data = extract_text_from_pdf(JUSAN_PDF_PATH)
    
    current_date = datetime.now().date()
    jusan_sheet = get_or_create_worksheet(f"{current_date}-jusan")
    
    jusan_sheet.clear()

    for line in pdf_data:
        jusan_sheet.append_row([line["date"], line["amount"], line["description"]])

print("Spreadsheet updated successfully!")