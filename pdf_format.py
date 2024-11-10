import fitz
import os
from pathlib import Path

input_directory = "input"
overlay_img_filename = 'black_box.png'
overlay_pdf_filename = 'black_box.pdf'

old_style = "old_style"
new_style = "new_style"



for subdir, dirs, files in os.walk(input_directory):
    # print(f"subdir {subdir}")
    # print(f"dors {dirs}")
    # print(f"files {files}")
    for file in files:
        full_input_filename = os.path.join(subdir, file)
        output_dir_name = subdir.replace("input", "output")
        full_output_filename = full_input_filename.replace("input", "output")
        if full_input_filename.endswith(".pdf"):
            #print(f"\nfull_output_filename: {full_output_filename}\n\n")
            if new_style in str(subdir):
                pass
                # img_rect = fitz.Rect(0, -1, 124, 330)
                # document = fitz.open(full_input_filename)
                # # We'll put image on first page only but you could put it elsewhere
                # page = document[0]
                # page.insert_image(img_rect, filename=overlay_img_filename)
                # document.save(full_output_filename)
                # document.close()
            elif old_style in str(subdir):
                Path(output_dir_name ).mkdir(parents=True, exist_ok=True)
                # 0, -1, 124, 350
                # 350 is def the right number
                # img_rect = fitz.Rect(0, -1, 350, 425) great size but too far left
                # img_rect = fitz.Rect(250, -100, 550, 500) almost perfect but i wish were a little longer
                img_rect = fitz.Rect(200, -150, 550, 560)
                document = fitz.open(full_input_filename)
                # We'll put image on first page only but you could put it elsewhere
                page = document[0]
                page.insert_image(img_rect, filename=overlay_img_filename)
                document.save(full_output_filename)
                document.close()
