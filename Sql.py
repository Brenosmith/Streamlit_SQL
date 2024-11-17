import pyodbc
import pandas as pd

class SQL:
    def __init__(self):
        # Define your connection string
        self.conn_str = (
            r'DRIVER={ODBC Driver 17 for SQL Server};'
            r'SERVER=VIVOBOOK\SQLEXPRESS;'
            r'DATABASE=SQNPRC001;'
            r'Trusted_Connection=yes;'
        )

    def fetch_table_data(self, table_name, kwargs=None):
        # Establish the connection
        conn = pyodbc.connect(self.conn_str)

        # Create a cursor object using the connection
        cursor = conn.cursor()

        # Execute a query
        if kwargs:
            query = f"SELECT * FROM {table_name} WHERE {kwargs};"
        else:
            query = f"SELECT * FROM {table_name};"
        
        cursor.execute(query)

        # Fetch all rows and column names
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]

        # Close the connection
        conn.close()

        # Create a DataFrame from the fetched data
        df = pd.DataFrame.from_records(rows, columns=columns)

        return df

    def update_table_data(self, table_name, ferias_sim_nao, analista):
        try:
            # Establish the connection
            conn = pyodbc.connect(self.conn_str)

            # Create a cursor object using the connection
            cursor = conn.cursor()

            # Execute an update query
            query = f"UPDATE {table_name} SET FERIAS = ? WHERE ANALISTA = ?;"
            cursor.execute(query, ferias_sim_nao, analista)

            # Commit the transaction
            conn.commit()

            # Close the connection
            conn.close()

            return "Success"
        except Exception as e:
            return f"Error: {e}"
