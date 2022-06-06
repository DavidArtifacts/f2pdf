import os
import sys
from fpdf import FPDF


def getDirectories(dir, ext):
    subdirs = [x[0] for x in os.walk(dir)]
    imagedirs = []
    for s in subdirs:
        files = os.listdir(s)
        for file in files:
            # only directories with images
            if file.endswith('.' + ext):
                imagedirs.append(s)
                break 
    return imagedirs


def getImageList(dir, ext):
    os.chdir(path=dir)
    imagelist = []
    for i in os.listdir():
        # only ext type image files
        if i.endswith('.' + ext):
            imagelist.append(dir + '\\' + i)
    return imagelist


def convertToPDF(imagelist, outdir):
    pdf = FPDF()
    for image in imagelist:
        pdf.add_page()
        pdf.image(image, 0, 0, 210, 297)
    # get closest folder name for pdf file
    filename = os.path.split(os.path.dirname(imagelist[0]))[-1] + ".pdf"
    print("Converting {}...".format(filename))
    pdf.output(outdir + '\\' + filename, 'F')
    

def processDirectory(dir, outdir, ext):
    dirs = getDirectories(dir, ext)
    for i, d in enumerate(dirs):
        print("{} of {}".format(i + 1, len(dirs)))
        images = getImageList(d, ext)
        convertToPDF(images, outdir)
    

def main():
    args = sys.argv[1:]
    dir = ''
    outdir = ''
    # image file extension .jpg is default
    ext = 'jpg'
    if len(args) == 2:
        dir = args[0].strip()
        outdir = args[1].strip()
    
    if len(args) == 3:
        ext = args[2].strip()
    
    if dir != '' and outdir != '':
        processDirectory(dir, outdir, ext)    
        print("done")
    else:
        print("params: dir and outdir are required - ex. './myfolder /outfolder'")
    
    
if  __name__ == '__main__':
    main()