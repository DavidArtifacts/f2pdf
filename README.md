# f2pdf
Combine and convert all image files in a folder or directory to PDF.

### Install FPDF

`pip install fpdf`

### How to use
Run python file in terminal

`python dir2pdf.py 'C:/MyImagesDir' 'C:/MyOutputDir' jpg`

Where the parameters are in this order:
1. directory - Where your image files are in
2. output - Output directory where PDF file will be saved
3. ext - Image file extension, jpg is default (optional)

This will walk into your directory and search all folders that contains images,
combine all the images and create a PDF, the result PDF file will have the name 
of the closest directory of the converted images.


Feel free to reuse and modify as you needs ♥️
