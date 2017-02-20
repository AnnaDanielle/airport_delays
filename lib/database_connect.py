import psycopg2

def connect_to_airport_db():
    connection = psycopg2.connect(dbname = 'airports', user = 'annaheller', host = 'localhost')
    cursor = connection.cursor()
    return cursor

def select_entire_tbl(table_name):
    
    sql_statement = u"""

    SELECT * FROM {};

    """.format(table_name)
    
    cursor = connect_to_airport_db()
    cursor.execute(sql_statement)
    
    return cursor.fetchall()