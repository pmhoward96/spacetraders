import sqlite3
import pandas as pd

dbFile = "data/spaceTradersDb.db"

def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
        print(sqlite3.version)
    except Exception as e:
        print(e)
    finally:
        if conn:
            return conn
        
def close_connection(conn):
    conn.close()

def create_table(tableName, columns):
    #columns is a list of list with [columnName, variableType]
    conn = create_connection()
    cursor = conn.cursor()
    columnString = ""
    columnLen = len(columns)
    count = 0
    for i in columns:
        if count == columnLen - 1:
            columnString += i[0] + " " + i[1]
        else:
            columnString += i[0] + " " + i[1] + ", "
        count += 1
    query = "CREATE TABLE " + tableName + " (" + columnString + ");"
    print(columnString)
    try:
        cursor.execute(query)
    except Exception as e:
        print(e)
    close_connection(conn)

def insert_data(tableName, cvDf):
    conn = create_connection()
    cursor = conn.cursor()
    columns = cvDf.columns
    valuesList = cvDf.values.tolist()
    #print(valuesList)

    #columns = cvDf.columns()
    #columnString = ""
    ##valueLen = len(cvDf)
    #count = 0
    #for i in cvDf:
       # if count == valueLen - 1:
         #   columnString += i.columnName
        #    valueString  += i.value
        #else:
         #   columnString += i.columnName + ", "
         #   valueString  += i.value + ", "
    #query = "INSERT INTO " + tableName + " (" + columnString + ") VALUES (" + valueString + ");"
    columnString = "("
    count = 0
    for c in columns:
        if count == len(columns) - 1:
            columnString += "?)"
        else:
            columnString += "?,"
        count += 1

    query = "INSERT INTO " + tableName + " VALUES " + columnString
    try:
        cursor.executemany(query, valuesList)
        conn.commit()
        close_connection(conn)
    except Exception as e:
        print(e)
        close_connection(conn)
        return e
    return True

def get_all_values(tableName):
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT * from " + tableName
    try:
        df = pd.read_sql_query(query, con = conn)

        close_connection(conn)
    except Exception as e:
        print(e)
        close_connection(conn)
        return e
    return df

