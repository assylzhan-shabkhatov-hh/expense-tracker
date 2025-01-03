from datetime import datetime
import re
from PyPDF2 import PdfReader


# Specify the path to the PDF file
pdf_path = "C:\\Users\\me\\Downloads\\Telegram Desktop\\Выписка по карте.pdf"

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
                        transactions.append({
                            "date": date,
                            "amount": amount,
                            "description": description.strip()
                        })
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
                transactions.append({
                    "date": date,
                    "amount": amount,
                    "description": description.strip()
                })
    return transactions

pdf_data = extract_text_from_pdf(pdf_path)

for line in pdf_data:
    print(line)

