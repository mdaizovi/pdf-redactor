import os
from pathlib import Path
import fitz
# NOTE For some reason only installing fitz doesn't work, it has to be instaled via pymupdf
# PyMuPDF==1.25.0
# I didn't make requirements.txt bc all you really need is
# pip install pymupdf
# (in a virtual environment, and then acticat virtual environmnt)

input_directory = "input"
overlay_img_filename = "black_box.png"
rect_args_by_input_dir_name = {
    "old_style": [0, -1, 124, 330],
    "new_style": [200, -150, 550, 560],
}


def flatten_pdf(input_path, output_path):
    """
    Converts PDF to an image and then back to a pdf again.
    This admittedly leaves it looking a little blurry, but 
    email, address, phone number, is no longer selectable behind the black box
    """
    # Open the PDF
    pdf_document = fitz.open(input_path)

    # Create a new PDF document
    new_pdf = fitz.open()

    # Process each page
    for page_num in range(pdf_document.page_count):
        # Get the page
        page = pdf_document[page_num]

        # Convert page to image (this removes all interactive elements)
        pix = page.get_pixmap()

        # Create a new page in the output PDF
        new_page = new_pdf.new_page(width=page.rect.width, height=page.rect.height)

        # Insert the image into the new page
        new_page.insert_image(new_page.rect, pixmap=pix)

    # Save the flattened PDF
    new_pdf.save(output_path)

    # Close both documents
    pdf_document.close()
    new_pdf.close()


for subdir, dirs, files in os.walk(input_directory):
    for file in files:
        full_input_filename = os.path.join(subdir, file)
        if full_input_filename.endswith(".pdf"):
            # mimic input filepath in output so files will be easy to find
            output_dir_name = subdir.replace("input", "output")
            full_output_filename = full_input_filename.replace("input", "output")
            # Creat the directory, if need be
            Path(output_dir_name).mkdir(parents=True, exist_ok=True)
            # flatten PDF else identifying info will still be selectabl under the black box
            flatten_pdf(full_input_filename, full_input_filename)
            # Find the right box arguments based on input direcotry name
            for k, v in rect_args_by_input_dir_name.items():
                if k in str(subdir):
                    img_rect = fitz.Rect(*v)
                    document = fitz.open(full_input_filename)
                    # put black box in specified area of pdf
                    page = document[0]
                    page.insert_image(img_rect, filename=overlay_img_filename)
                    document.save(full_output_filename)
                    document.close()
