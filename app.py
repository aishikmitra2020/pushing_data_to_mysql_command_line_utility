import argparse
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv
load_dotenv()

# MySQL connection details (you can customize these values)
HOST = os.getenv('HOST')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
DATABASE = os.getenv('DATABASE')
PORT = 3306  # default MySQL port

def insert_data_to_mysql(excel_file, sheet_name, table_name):
    # Convert to absolute path to ensure correct file handling
    excel_file = os.path.abspath(excel_file)

    # Check if the file exists
    if not os.path.exists(excel_file):
        print(f"Error: File '{excel_file}' not found.")
        return

    # Read the Excel file into a Pandas DataFrame
    try:
        df = pd.read_excel(excel_file, sheet_name=sheet_name)
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return

    # Create the connection string
    connection_string = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

    # Create an engine
    engine = create_engine(connection_string)

    try:
        # Inserting data into MySQL
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Data from '{sheet_name}' inserted into '{table_name}' table successfully.")
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
    finally:
        engine.dispose()

def main():
    # Setting up command-line argument parsing with optional arguments
    parser = argparse.ArgumentParser(description="Insert data from an Excel sheet into a MySQL table")
    
    parser.add_argument("-e", "--excel_file", type=str, required=True, help="Full path to the Excel file")
    parser.add_argument("-s", "--sheet_name", type=str, required=True, help="Name of the sheet in the Excel file")
    parser.add_argument("-t", "--table_name", type=str, required=True, help="Target table name in the MySQL database")

    args = parser.parse_args()

    # Call the function to insert data into the MySQL database
    insert_data_to_mysql(args.excel_file, args.sheet_name, args.table_name)

if __name__ == "__main__":
    main()
