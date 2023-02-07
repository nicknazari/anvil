from flask import Flask
from waitress import serve
import mysql.connector
import rds_login
import json

app = Flask('anvil')

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

@app.route('/')
def hello_world():
    return (execute_sql('select * from users'))

@app.route('/anvil_test')
def anvil_test():
    return "<p>testing</p>"

# API functions should return json formatted data
@app.route('/verifyUser')
def verify_user():
    # args: email, hashedP 
    return "<p>Verified</p>"

@app.route('/createAccount')
def create_account():
    # args: email, hashedP
    return "<p>account create</p>"

@app.route('/createForum')
def create_forum():
    # args: workplace, address, forum_name, forum_id
    return "<p>forum create</p>"

@app.route('/getUserForums')
def get_user_forms():
    # args: user_id
    return "<p>get user forums</p>"

@app.route('/addUserToForum')
def add_user_to_forum():
    # args: user_id, forum_id
    return "<p>add user to forum</p>"

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=80)
