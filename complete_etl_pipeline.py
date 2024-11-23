# Import the necessary functions
from data_extraction import extract_data as extract_employee_data
from data_transformation import transform_data as transform_employee_data
from data_storage import load_data_to_db

def run_etl_pipeline(file_path, db_name='employee_data_etl.db'):
    # Extract
    data = extract_employee_data(file_path)
    if data is not None:
        # Transform
        transformed_data = transform_employee_data(data)
        if transformed_data is not None:
            # Load
            load_data_to_db(transformed_data, db_name)

# Run the ETL pipeline
run_etl_pipeline('contents/employees_data.csv', 'employee_data_etl.db')
