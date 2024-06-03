'''
Project 5, Working with SQL in Python
Carter Smith
Objective: Create a Python script that demonstrates the ability to interact with a SQL database, including creating a database, defining a schema, and executing various SQL commands. Incorporate logging to document the process and provide user feedback.
'''

import sqlite3
import pandas as pd
import pathlib
import logging
import db_initialize_cartersmith as init

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

def execute_sql_from_file(db_filepath, sql_file):
    sql_path = pathlib.Path('sql')/sql_file
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_path, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")
    


def main():
    logging.info("Program started") # add this at the beginning of the main method
    db_filepath = 'project.db'
    
    init.main()
    

    # Create database schema and populate with data
    
    execute_sql_from_file(db_filepath, 'insert_records.sql')
    execute_sql_from_file(db_filepath, 'update_records.sql')
    execute_sql_from_file(db_filepath, 'delete_records.sql')
    execute_sql_from_file(db_filepath, 'query_aggregation.sql')
    execute_sql_from_file(db_filepath, 'query_filter.sql')
    execute_sql_from_file(db_filepath, 'query_sorting.sql')
    execute_sql_from_file(db_filepath, 'query_group_by.sql')
    execute_sql_from_file(db_filepath, 'query_join.sql')

    logging.info("All SQL operations completed successfully")
    logging.info("Program ended")  # add this at the end of the main method
    
if __name__ == "__main__":
    main()