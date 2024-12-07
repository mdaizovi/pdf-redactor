# pdf-redactor
Custom script to put black boxes in 2 specified locations on pdf invoices, so a friend can 
give her invoices to an auditor, without exposing sensitive client information.

## Installation
Requirements:
(please ensure python in on your machine, or if not, install it)
 - [python 3.10](https://www.python.org/psf/)

### Set Up Your Local Development Environment
- clone this repo
    - `git clone https://github.com/mdaizovi/pdf-redactor.git`
- cd into the repo directory
    - `cd pdf-redactor`
- create a virtual environment
    - `virtualenv -p python venv`
- activate the virtual environment
    - `source venv/bin/activate`
- Install PyMuPDF
    - `pip install pymupdf` 

## Put Input source files
Take your invoices and put them in 
`/input` directory, either in the `/new_style` or `/old_style` directories, depending on where you want the black box to show up.

## Run Script
While in main directory and virtual encironment, run
`python pdf_format.py`

## Future: If you ever have a third invoice style:
Make a new directory in `/input`, give it another name, and then add that directory name to the `rect_args_by_input_dir_name` in pdf_format.py
Give it a list of 4 numbers like the other 2 and trial-error-changing those numbers and running the program, until the box is where you want it.
