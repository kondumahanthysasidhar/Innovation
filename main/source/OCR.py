import fitz


def pdf_to_image(pdf_path, image_path):
    # Open the PDF
    pdf_document = fitz.open(pdf_path)

    # Iterate through each page
    for page_number in range(len(pdf_document)):
        # Get the page
        page = pdf_document.load_page(page_number)

        # Render the page to an image (PNG)
        pix = page.get_pixmap()

        # Save the image
        image_file = f"{image_path}_page_{page_number + 1}.png"  # Change the format if needed
        pix.save(image_file)
        print(f"Page {page_number + 1} saved as {image_file}")

    # Close the PDF
    pdf_document.close()


# Example usage:
pdf_path = "C:\\Users\\kondu\\PycharmProjects\\pythonProject\\main\\resources\\financial.pdf"
image_path = "C:\\Users\\kondu\\PycharmProjects\\pythonProject\\main\\resources"  # Output image path without extension
# pdf_to_image(pdf_path, image_path)



import easyocr

# Create an OCR reader object
def convert_img_to_text(image_path):
    reader = easyocr.Reader(['en'])  # Specify languages (e.g., English)

    # Perform OCR on an image file
    result = reader.readtext(image_path)

    # Print the OCR results
    for detection in result:
        print(detection[1])

image_path = "C:\\Users\\kondu\\PycharmProjects\\pythonProject\\main\\resources_page_6.png"
convert_img_to_text(image_path)


import pytessaract