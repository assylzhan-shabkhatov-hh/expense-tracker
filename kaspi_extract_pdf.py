import re
from PyPDF2 import PdfReader


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
            # transactions.append({
            #     "date": date,
            #     "amount": amount,
            #     "description": description.strip()
            # })
            transactions.append([date, amount, description.strip()])
        except:
            print("Error while processing line:", match.group(0))
    return transactions

# # Specify the path to the PDF file
# pdf_path = ""
# pdf_data = extract_text_from_pdf(pdf_path)

# for line in pdf_data:
#     print(line)

