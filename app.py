import argparse
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# MySQL connection details (you can customize these values)
HOST = "your_host"
USERNAME = "your_username"
PASSWORD = "your_password"
DATABASE = "your_database"
PORT = 3306  # default MySQL port

def insert_data_to_mysql(excel_file, sheet_name, table_name):
    # Read the Excel file into a Pandas DataFrame
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

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
    # Setting up command-line argument parsing
    parser = argparse.ArgumentParser(description="Insert data from an Excel sheet into MySQL table")
    
    parser.add_argument("excel_file", help="Path to the Excel file")
    parser.add_argument("sheet_name", help="Name of the sheet in the Excel file")
    parser.add_argument("table_name", help="Target table name in the MySQL database")

    args = parser.parse_args()

    # Call the function to insert data into the MySQL database
    insert_data_to_mysql(args.excel_file, args.sheet_name, args.table_name)

if __name__ == "__main__":
    main()
