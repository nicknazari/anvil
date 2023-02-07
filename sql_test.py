import mysql.connector
import rds_login
import json

# in the case that the app crashes, we don't want to lose all db items,
# so we will open and close a db connection every time we write data,
# within each request handler

def connect():
    conn = mysql.connector.connect (
        host=rds_login.host,
        user=rds_login.user,
        password=rds_login.password,
        database=rds_login.database
    )
    cursor = conn.cursor(buffered=True)

    return (conn,cursor)

def disconnect(conn):
    conn.commit()
    conn.close()

def execute_sql(query):
    connection = connect()
    conn = connection[0]
    cursor = connection[1]
    cursor.execute(query)
    disconnect(conn)
    return cursor.fetchall()

if (__name__ == "__main__"):
    print(execute_sql("select * from users;"))
