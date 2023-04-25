import fitz
import io
import ocrmypdf
import pandas as pd

# Load the PDF file
pdf_file = "bookingconfirmation.pdf"

# Extract the text from the PDF
text = ""
doc = fitz.open(pdf_file)
for page in doc:
    img_bytes = page.get_pixmap().tobytes("png")
    with io.BytesIO(img_bytes) as img_io, io.BytesIO() as output_io:
        ocrmypdf.ocr(img_io, output_io, pages=1)
        output_io.seek(0)
        raw_output = output_io.read() # get the raw output before decoding
        page_text = raw_output.decode('latin-1') # decode the raw output
        text += page_text

        print(raw_output) # print the raw output

# Clean the text
text = text.replace("\n", " ")
text = " ".join(text.split())
print(text)


# Write the text to a single cell in an Excel spreadsheet
df = pd.DataFrame({"Document Text": [text]})
df.to_excel("training_data.xlsx", index=False)
