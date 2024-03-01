# Assignment-3

## Live application Links
[![codelabs](https://img.shields.io/badge/codelabs-4285F4?style=for-the-badge&logo=codelabs&logoColor=white)](https://codelabs-preview.appspot.com/?file_id=1vkNzPBXibaYNVNK3z4BwVSpV7XNYXeLTjbUcQXptyOI#0)



## Problem Statement
Design Python classes for web page and Grobid output schemas, validating data with Pydantic and creating "clean" CSV files. Utilize DBT with Snowflake to load clean data, construct a summary table, and deploy the model with testing. Establish Test and Production Environments in Snowflake, considering necessary considerations for deployment.

## Project Goals
Design and implement Python classes, namely URLClass, MetaDataPDFClass, and ContentPDFClass, to represent the schema for webpages and Grobid output (Part 1). Utilize Pydantic for data and schema validation, generating "clean" CSV files, and creating 5+5 test cases for validation success/failure. For Part 2, use DBT with Snowflake to load clean data, create a summary table schema, materialize it, write tests, and document the model. Additionally, set up Test and Production Environments in Snowflake, considering relevant considerations for each.

## Technologies Used
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![DBT](https://img.shields.io/badge/DBT-861121?style=for-the-badge)](https://www.getdbt.com/)
[![GROBID](https://img.shields.io/badge/GROBID-FFFFFF?style=for-the-badge&logo=GROBID&logoColor=black)](https://grobid.readthedocs.io/en/latest/Introduction/)
[![Snowflake](https://img.shields.io/badge/snowflake-0000FF?style=for-the-badge&logo=snowflake&logoColor=white)](https://docs.snowflake.com/ )

## Data Sources
[CFA Institute's website](https://www.cfainstitute.org/en/membership/professional-development/refresher-readings#sort=%40refreadingcurriculumyear%20descending)

## Pre requisites
1. Python Knowledge
2. Snowflake Account
3. DBT Cloud Knowledge


## How to run Application locally (**To be filled**)
1. Create Python virtual environment
2. run -> pip install -r requirements.txt
3. load Jupyter Notebook
5. run local image of Grobid
6. run the Jupyter notebooks present under the notebooks directory
7. next run 
8. then run 
9. finally run 

## Project run outline

### 1. CFA Data - Cleaning, Validation, Testing

- 
- 

### 2. PDF Data - Extraction to Structured Schema, Metadata Extraction, Cleaning, Validation, Testing
- Extract the pdf contents from Grobid output and store it in a structured schema
- Extract the metadata from Grobid using Langchain and strore it in a structured schema
- Perform Validation using Pydantic and Testing
- Additionally, Extraction of pdf contens from Pypdf output to a structured schema has been done
  
### 3. SnowFlake
- 

### 4. DBT
- 
- 

CodeLab - [Documentation](https://docs.google.com/document/d/1a4kE9iRo0cuh8gUI4NTd2sVjGIwXH5tBalrgW-4uvd0/edit#heading=h.j0flkct7g8l6) 

## References

- https://www.getdbt.com/
- https://docs.getdbt.com/guides/snowflake?step=1
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- https://www.selenium.dev/
- https://www.cfainstitute.org/en/membership/professional-development/refresher-readings#sort=%40refreadingcurriculumyear%20descending
- https://github.com/kermitt2/grobid
- https://diagrams.mingrammer.com/
- https://app.snowflake.com/
- https://github.com/ashrithagoramane/DAMG7245-Spring24/tree/main/repository_structure

  ## Learning Outcomes

  ## Team Information 
  Project Board - https://github.com/orgs/BigDataIA-Spring2024-Sec2-Team2/projects/2/views/1
  
  Name | Contribution %| Contributions |
  --- |--- | --- |
  Anshul Chaudhary  | | |
  Agash Uthayasuriyan |  | PDF content Extraction (Grobid, PyPDF), Metadata Extraction, Pydantic Validation|
  Narayani Arun Patil |  | |
