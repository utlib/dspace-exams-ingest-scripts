#!/usr/bin/python

import csv
from bs4 import BeautifulSoup
import argparse
from os import listdir, path

def get_depts_mapping(csv_filename):
  """ Parameters:
      csv_filename (string): filepath of the campus csv, the csv lists a table of three columns: ID, Dept_code and Department.
      
      1,ACT,"Actuarial Science"
      2,ANT,"Anthropology"

      Returns:
      A dictionary with Department code as key and full Department name as value.
      {'ACT': 'Actuarial Science', 'ANT': 'Anthropology'}
  """
  mapping = {}
  with open(csv_filename) as raw_csv:
    for row in csv.DictReader(raw_csv):
      mapping[row['Dept_code']] = row['Department']
  return mapping

def get_dc_row(element, qualifier, value):
  """ Parameters:
      element - xml element 
      qualifier - xml qualifier 
      value - value to be written in the xml file for the the specific element and qualifier
      Returns:
      The newly created xml file row with parsed from the supplied information
      <dcvalue element="date" qualifier="issued">2018-04</dcvalue>
  """
  row = BeautifulSoup("<dcvalue></dcvalue>", "xml").dcvalue
  row['element'] = element
  row['qualifier'] = qualifier
  row.string = value
  return row

def get_filename_dates(filename, campus):
  """ Parameters:
      filename - filepath for the exam file
      campus - campus A, B or C
      The file name is a specific format with Course Code, Semester, and Exam Date
      separated by dashes (-) these are parsed out to determine the dates of the exam

      Returns:
      Exam Period and Date in Numerical format which are values used when generating the dublin core metadata file.
      April 2018 2018-04
  """
  

  
  parts = filename.split('-')  	
  year = "20" + parts[1][-2:]
  if campus == 'C':
    month = parts[1][:2]
  else:
    month = parts[1][0]
    
  if month == "J":
    date = "June " + year
    numbers = year + "-06" 
  elif month == "M":
    date = "May " + year
    numbers = year + "-05"
  elif month == "A" and campus == "C":
    date = "August " + year
    numbers = year + "-08"
  elif month == "AP":
    date = "April " + year
    numbers = year + "-04"
  elif month == "N":
    date = "November " + year
    numbers = year + "-11"
  elif month == "D":
    date = "December " + year
    numbers = year + "-12"
  elif month == "AU":
    date = "August " + year
    numbers = year + "-08"    
  else:
    raise ExamDateException("Unknown exam month in filename " + filename)       

  if len(parts) == 3:
    section = parts[2]
    date += " " + section

  return (date, numbers)

def make_dc(filename, depts, campus):
  """ Parameters: 
      filename - exam file name
      depts - dictionary with department code and department full name
      campus - campus A, B or C
      
      Returns:
      A completed dublin_core xml file for the specified exam.
  """
  if campus == "A":
    campus_abbrev = "campus_a"
  elif campus == "B":
    campus_abbrev = "campus_b"
  elif campus == "C":
    campus_abbrev = "campus_c"
  
  dates = get_filename_dates(filename, campus_abbrev)
  main_dc = BeautifulSoup("<dublin_core schema=\"dc\"></dublin_core>", "xml").dublin_core
  main_dc.append(get_dc_row("contributor", "other", depts[filename[:3]]))
  main_dc.append(get_dc_row("contributor", "other", campus))
  main_dc.append(get_dc_row("title", "none", filename[:7] + " - " + dates[0]))
  main_dc.append(get_dc_row("date", "issued", dates[1]))
  main_dc.append(get_dc_row("language", "iso", "en_ca"))
  main_dc.append(get_dc_row("type", "none", "exam"))
  main_dc.append(get_dc_row("subject", "none", filename[:7]))
  
  return main_dc

class ExamDateException(Exception):
  """Exception thrown if exam month unable to be identified
  """
  pass
 
if __name__ == "__main__":
  doc = "Given the root path of PDF exams and campus, produce accompanying XML files for DSpace."

  parser = argparse.ArgumentParser(description=doc)
  parser.add_argument('pdfpath', help='Path to the root path of PDF exams') 
  parser.add_argument('campus', help='Campus: A, B or C') 
  args = parser.parse_args()  

  if (args.campus == "A"):
    depts = get_depts_mapping("Campus_A.csv")
    campus = "Campus A"
  elif (args.campus == "utsc"):    
    depts = get_depts_mapping("Campus_B.csv")
    campus = "Campus B"
  else:
    depts = get_depts_mapping("Campus_C.csv")
    campus = "Campus C"
   
  for exam_pdf in listdir(args.pdfpath):    
    filename = exam_pdf.split('.')[0]
    dc = make_dc(filename.upper(), depts, campus)        
    with open(path.join(args.pdfpath, filename + ".xml"), "w") as xml:
       xml.write(dc.prettify())
