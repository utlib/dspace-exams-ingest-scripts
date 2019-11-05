# Exam metadata generation and ingest for DSpace

This is a generalized workflow followed by the University of Toronto Libraries for its DSpace-based repository of previous exam questions from its 3 campuses.

- **step1.py** creates Dubin Core metadata from PDF's filename + department code in the spreadsheets based on the campus. 
- **step2.py** packages DSpace simple archive that consists of the PDF, DC metadata in XML and "content" file. These archives can then be imported using the DSpace admin batch import functionality.

## System Requirements

* [Python version 3](https://www.python.org/downloads/)
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
* Exams are scanned/created in PDF with file names based on this [file naming convention](exam-pdf-filename-conventions.png) 
* Each PDF file must contain the course code, month and year.
<br>

### 2. Generate metadata 
* Run step1.py to generate metadata from PDF's filename 
* The script also uses a CSV file of departmental codes per campus for mapping

<br>

[sample generated metadata file found here](mat700h-ap18.xml)

### 3. Package DSpace Simple Archive
* Run step2.py script to package the PDFs and metadata into DSpace simple archives for ingest

### 4. Batch Import Into TSpace
* Import DSpace simple archives into their respective collections via DSpace batch import

---

## License
DSpace Simple Archives Importer is licensed under Apache License 2.0.
