import pyodbc
import pandas as pd

def fetch_table_data(table_name, kwargs=None):
    # Define your connection string
    conn_str = (
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=VIVOBOOK\SQLEXPRESS;'
        r'DATABASE=SQNPRC001;'
        r'Trusted_Connection=yes;'
    )

    # Establish the connection
    conn = pyodbc.connect(conn_str)

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

if __name__ == "__main__":
    # Example usage
    table_name = "Twister.Tabela_Teste"
    df = fetch_table_data(table_name)
    print(df)


def update_table_data(table_name, ferias_sim_nao, analista):
    # Define your connection string
    conn_str = (
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=VIVOBOOK\SQLEXPRESS;'
        r'DATABASE=SQNPRC001;'
        r'Trusted_Connection=yes;'
    )

    try:
        # Establish the connection
        conn = pyodbc.connect(conn_str)

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

# Example usage
table_name = "Twister.TB_TWISTER_ONBOARDING"
ferias_sim_nao = "SIM"
analista = "Camila Sousa"
result = update_table_data(table_name, ferias_sim_nao, analista)
print(result)
