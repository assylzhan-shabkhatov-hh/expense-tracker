from datetime import datetime
import re
from PyPDF2 import PdfReader

# Specify the path to the PDF file
pdf_path = "C:\\Users\\me\\Downloads\\Telegram Desktop\\fe1c916c-1ae3-42f3-9c53-982059151dc3_gold_statement.pdf"

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = "\n".join(page.extract_text() for page in reader.pages)
    pattern = re.compile(r"^(\d{2}\.\d{2}\.\d{2}) ([+-]) ([\d\s]+,\d{2}) ₸ (.+)", re.MULTILINE)

    transactions = []

    for match in pattern.finditer(text):
        try:
            date, sign, amount, description = match.groups()
            amount = float(amount.replace(" ", "").replace(",", "."))
            amount = amount if sign == "+" else -amount
            transactions.append({
                "date": date,
                "amount": amount,
                "description": description.strip()
            })
        except:
            print("Error while processing line:", match.group(0))
    return transactions

pdf_data = extract_text_from_pdf(pdf_path)

for line in pdf_data:
    print(line)

