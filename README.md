# Exam metadata generation and ingest for DSpace

## Pre-requisites 

* Install python version 2.7
* Install beautifulsoup
* Install lxml

## Workflow

### Scanning & Filenaming
* Exams are scanned into PDF with file names
* Each PDF file must contain the course code, month and year.
* DSpace Dublin Core metadata are generated based on each PDF's filename. 
<br>

_Example:_ 
Campus C, they should use "au" for August and "ap" for April to properly distinguish these two months. 


[detailed exam file naming convention found here](exam-pdf-filename-conventions.png)

### Retrieve Exams
* Receive scanned exams in PDF format from campuses A, B, C
* Print exams are received as a batch once a year from campus A and 3 times a year from campus C. 

### Generate metadata 
* Run step1.py to generate metadata
* Dublin Core metadata is generated from the file names using step1.py with Beautiful Soup library
* The script also uses a CSV file of departmental codes per campus for mapping
<br>

_(Attached in this repository are sample .csv files for Campus A, B & C)_

[sample metadata file found here](mat700h-ap18.xml)

### DSpace Simple Archive
* step2.py script is used to package the PDFs and metadata into DSpace simple archives for ingest

### Batch Import Into TSpace
* DSpace simple archives are imported into their respective collections via batch import
* Collections older than 3 years old are removed

## Usage

1. `python step1.py /directory_path_to_pdf_exams/ campus[A, B or C]`

2. `python step2.py '/directory_path_to_pdf_exams/`


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
DSpace Simple Archives Importer is licensed under Apache License 2.0.
