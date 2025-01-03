import re
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    transactions = []

    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text:
            lines = text.split("\n")
            date = ""
            amount = ""
            description = ""
            amount_pattern = r"^ALMATY.*?(?<!\d)(\d+)(?=\.00)"
            date_pattern = r"^\d{2}\.\d{2}\.\d{2}"
            for line in lines:
                if(re.search(date_pattern, line)):
                    if(date):
                        if('Покупка' in description):
                            amount = '-' + amount
                        transactions.append([date, amount, description.strip()])
                        date = ""
                        amount = ""
                        description = ""
                    date = line
                else:
                    match = re.search(amount_pattern, line)
                    if match:
                        amount = match.group(1)
                    else:
                        if(date):
                            description += line
            
            if(date):
                if('Покупка' in description):
                    amount = '-' + amount
                transactions.append([date, amount, description.strip()])
    return transactions
# from dotenv import load_dotenv

# import os

# # Load environment variables from the .env file
# load_dotenv()

# # Specify the path to the PDF file  
# JUSAN_PDF_PATH = os.getenv("JUSAN_PDF_PATH")

# pdf_data = extract_text_from_pdf(JUSAN_PDF_PATH)

# for line in pdf_data:
#     print(line)

