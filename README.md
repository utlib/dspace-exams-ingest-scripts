# Exam metadata generation and ingest for DSpace

The Old Exams Repository is maintained by the University of Toronto Libraries. 
It contains the 3 most recent years of exams.

## System Requirements

* [Python version 2.7](https://www.python.org/download/releases/2.7/)
* [Beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [lxml](https://pypi.org/project/lxml/)

---

## Installation

Clone or download the scripts to your local repository. Ensure you have a the pre-requistie software installed before running the scripts. 

You must run step1.py before running step2.py, there are more details below about the usage and workflow.

---

## Usage

1. `python step1.py /directory_path_to_pdf_exams/ campus[A, B or C]`

2. `python step2.py '/directory_path_to_pdf_exams/`

---

## Workflow

### 1. Scanning & Filenaming
* Exams are scanned into PDF with file names
* Each PDF file must contain the course code, month and year.
* DSpace Dublin Core metadata are generated based on each PDF's filename. 
<br>

_Example:_ 
Campus C, they should use "au" for August and "ap" for April to properly distinguish these two months. 


[detailed exam file naming convention found here](exam-pdf-filename-conventions.png)

### 2. Retrieve Exams
* Receive scanned exams in PDF format from campuses A, B, C
* Print exams are received as a batch once a year from campus A and 3 times a year from campus C. 

### 3. Generate metadata 
* Once exams are received in PDF format from campuses A, B or C file metadata is generated
* Dublin Core metadata is generated from the file names using beautiful soup 
* The script also uses a CSV file of departmental codes per campus for mapping

<br>

_(Attached in this repository are sample .csv files for Campus A, B & C)_

[sample generated metadata file found here](mat700h-ap18.xml)

### 4. DSpace Simple Archive
* step2.py script is used to package the PDFs and metadata into DSpace simple archives for ingest

### 5. Batch Import Into TSpace
* DSpace simple archives are imported into their respective collections via batch import
* Collections older than 3 years old are removed

---

## License
DSpace Simple Archives Importer is licensed under Apache License 2.0.
