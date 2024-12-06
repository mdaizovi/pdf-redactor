import fitz
import os
from pathlib import Path
from PIL import Image
import pdf2image
import os
from fpdf import FPDF



input_directory = "input"
overlay_img_filename = 'black_box.png'
overlay_pdf_filename = 'black_box.pdf'

old_style = "old_style"
new_style = "new_style"

def flatten_pdf(input_path, output_path):
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
    # print(f"subdir {subdir}")
    # print(f"dors {dirs}")
    # print(f"files {files}")
    for file in files:
        full_input_filename = os.path.join(subdir, file)
        output_dir_name = subdir.replace("input", "output")
        full_output_filename = full_input_filename.replace("input", "output")
        if full_input_filename.endswith(".pdf"):
            Path(output_dir_name ).mkdir(parents=True, exist_ok=True)
            flatten_pdf(full_input_filename, full_input_filename)
            #print(f"\nfull_output_filename: {full_output_filename}\n\n")
            if new_style in str(subdir):
                img_rect = fitz.Rect(0, -1, 124, 330)
                document = fitz.open(full_input_filename)
                # We'll put image on first page only but you could put it elsewhere
                page = document[0]
                page.insert_image(img_rect, filename=overlay_img_filename)
                document.save(full_output_filename)
                document.close()

            elif old_style in str(subdir):
                # 0, -1, 124, 350
                # 350 is def the right number
                # img_rect = fitz.Rect(0, -1, 350, 425) great size but too far left
                # img_rect = fitz.Rect(250, -100, 550, 500) almost perfect but i wish were a little longer
                img_rect = fitz.Rect(200, -150, 550, 560)
                document = fitz.open(full_input_filename)
                # We'll put image on first page only but you could put it elsewhere
                page = document[0]
                page.insert_image(img_rect, filename=overlay_img_filename)
                document.save(full_output_filename, garbage=3,deflate=True)
                document.close()


