from flask import Flask
from waitress import serve
import mysql.connector
import rds_login

app = Flask('anvil')

conn = mysql.connector.connect (
    host=rds_login.host,
    user=rds_login.user,
    password=rds_login.password,
    database=rds_login.database
)

cursor = conn.cursor()

conn.commit()
conn.close()

@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"

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
