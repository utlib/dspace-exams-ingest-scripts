#!/usr/bin/python

import os
import shutil
import argparse

# Run the script with the directory of the packaged exams after running step1.py
parser = argparse.ArgumentParser()
parser.add_argument('path', help='Path to the working directory')
args = parser.parse_args()

# Traverse through the packaged exams directory and move the pdf and xml 
# that match the same exam name into the same folder.
for exam_pdf in os.listdir(args.path):		
  if exam_pdf.endswith(".pdf"):
    exam_name = exam_pdf.split(".")[0]
    exam_dest = os.path.join(args.path, exam_name)    
       
    # move PDF and XML into their own directory
    os.mkdir(exam_dest)
    shutil.move(os.path.join(args.path, exam_name + ".pdf"), exam_dest)
    shutil.move(os.path.join(args.path, exam_name + ".xml"), exam_dest + "/dublin_core.xml")

    # the contents file used by DSpace to recognize bitstreams
    with open(exam_dest + "/contents", "w") as contents:
      contents.write(exam_pdf)
