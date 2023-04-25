# ocronpdf
This code is designed to extract text from a PDF file, clean the text, and then write the text to an Excel spreadsheet. 

The code uses the fitz library to open the PDF file, then loops through each page using page.get_pixmap() to convert each page to an image. Then, ocrmypdf is used to perform optical character recognition (OCR) on each image to extract the text. The extracted text is stored in a variable named text.

Next, the code cleans the text by removing all newline characters (\n) and extra whitespaces, and then store the resulting clean text in the text variable.

Finally, the pandas library is used to create a dataframe named df containing the clean text, and this dataframe is then written to an Excel spreadsheet named training_data.xlsx.

Overall, this code provides a simple and effective way to extract and clean text from PDFs and store it in a structured format for further analysis or use.
