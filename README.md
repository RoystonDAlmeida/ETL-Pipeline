# ETL Pipeline Created Using Python

## Overview
This ETL (Extract, Transform, Load) pipeline is designed to automate the process of extracting data from various sources, transforming it into a desired format, and loading it into a target database or data warehouse. The pipeline is built using Python and leverages popular libraries for data manipulation and storage.

## Features
- **Data Extraction**: Supports extraction from various sources such as CSV files, databases (e.g., MySQL, PostgreSQL), and APIs.
- **Data Transformation**: Includes functionalities for data cleaning, normalization, and aggregation.
- **Data Loading**: Loads transformed data into specified target systems such as databases or cloud storage.
- **Logging**: Provides logging capabilities to monitor the ETL process and track errors.

## Creating Your Own `employees_data.csv` File

Since this repository does not include a sample `employees_data.csv` file, please create your own CSV file with the following structure:

1. Open a text editor or spreadsheet application (like Excel or Google Sheets).
2. Create a new file and ensure it has the following headers:

```bash
EmployeeID,Name,Department,Email,Phone,HireDate,Salary,Age
```

3. Fill in the data according to your requirements. Here’s an example of how it should look:

```bash
1,John Doe,Engineering,johndoe@example.com,1234567890,2020-01-15,70000,50
2,Jane Smith,Marketing,jane.smith@example.com,0987654321,2021-02-20,60000,25
```

4. Save the file with a `.csv` extension in the contents folder (e.g., `contents/employees_data.csv`).

### Table Structure

The ETL pipeline will create a table named `employees` in the target database with the following columns:

```bash
| Column Name      | Data Type | Description                                       |
|------------------|-----------|---------------------------------------------------|
| `employee_id`    | INTEGER   | Unique identifier for each employee (Primary Key) |
| `first_name`     | TEXT      | First name of the employee                        |
| `last_name`      | TEXT      | Last name of the employee                         |
| `salary`         | REAL      | Salary of the employee                            |
| `age`            | INTEGER   | Age of the employee                               |
| `department`     | TEXT      | Department where the employee works               |
| `salary_band`    | TEXT      | Classification of salary (e.g., Junior, Senior)   |
| `age_group`      | TEXT      | Age classification (e.g., Youth, Adult)           |
```

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
5. Monitor logs for any errors or status updates.