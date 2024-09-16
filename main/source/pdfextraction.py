import pdfreader

# Open the PDF file in read-binary mode
path = "C:\\Users\\kondu\\PycharmProjects\\pythonProject\\main\\resources\\financial.pdf"
pdffileobj = open(path, 'rb')

# Create a PdfFileReader object
pdfreader = pdfreader.PdfFileReader(pdffileobj)

# Get the number of pages in the PDF
num_pages = pdfreader.numPages

# Get the last page (indexing starts from 0)
pageobj = pdfreader.getPage(num_pages - 1)

# Extract text from the page
text = pageobj.extractText()

# Save the extracted text to a text file
with open('output.txt', 'w') as file:
    file.write(text)
