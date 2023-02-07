from flask import Flask
from flask import request
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

@app.route('/anvil_test', methods=['GET','POST'])
def anvil_test():
    return_value = {
        'status':0,
        'data':0
        }
    if request.method == 'POST':
        return_value['status'] = 1
        return_value['data'] = request.get_json('email')

    return return_value
# API functions should return json formatted data
@app.route('/verifyUser')
def verify_user():
    # args: email, hashedP 
    return "<p>Verified</p>"

@app.route('/createAccount', methods=['POST'])
def create_account():
    # flask automatically returns dicts as json
    # post request containing data email and hashedP
    # args: email, hashedP
    # 3 cases:
        # invalid args BAD, BUT we assume js frontend took care of that
        # account exists BAD
        # account doesnt exist GOOD
    return_value = {
        'status':0
        }

    # now we know they have passed right args, so lets see if acct exists
    query = execute_sql('select email from users where email = "' +  
                           request.form['email'] + '"')
    if len(query) > 0:
        return return_value
    else:
        user_id = 5
        forum_id = 5
        execute_sql('insert into users values ("' + user_id + 
                            '", "' + forum_id + '", "' +
                            request.form['password'] + 
                            '", "' + request.form['email'] + '")')
        return_value['status'] = 1
        return return_value

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
