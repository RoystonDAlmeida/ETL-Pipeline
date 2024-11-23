# ETL Pipeline Created Using Python

## Overview
This ETL (Extract, Transform, Load) pipeline is designed to automate the process of extracting data from various sources, transforming it into a desired format, and loading it into a target database or data warehouse. The pipeline is built using Python and leverages popular libraries for data manipulation and storage.

## Features
- **Data Extraction**: Supports extraction from various sources such as CSV files, databases (e.g., MySQL, PostgreSQL), and APIs.
- **Data Transformation**: Includes functionalities for data cleaning, normalization, and aggregation.
- **Data Loading**: Loads transformed data into specified target systems such as databases or cloud storage.
- **Logging**: Provides logging capabilities to monitor the ETL process and track errors.

## Requirements
To run this ETL pipeline, you need to have the following installed:
- Python 3.x
- Required Python libraries:
  - pandas
- sqlite3

You can install the required libraries using pip:


## Installation
1. Clone the repository: git clone `git@github.com:RoystonDAlmeida/ETL-Pipeline.git`
2. Install sqlite3: `sudo apt-get install sqlite3 libsqlite3-dev`
3. Check the version of sqlite3: `sqlite3 --version`


## Usage
1. Navigate the folder to where the files are to be saved.
2. Run the ETL Pipeline: `python3 complete_etl_pipeline.py`. It will save the modified employee data in a database `employee_data_etl.db`.
3. To navigate into the database, run the command `sqlite3 employee_data_etl.db`
4. To view the transformed data, run  the command `SELECT * FROM employees;`
3. Monitor logs for any errors or status updates.
