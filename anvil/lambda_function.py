import json
import mysql.connector
import os

def lambda_handler(event, context):
    conn = mysql.connector.connect (
        host=os.environ['host'],
        user=os.environ['user'],
        password=os.environ['password'],
        database=os.environ['database']
    )
    cursor = conn.cursor()

    # testing
    if event.get('type') == 'MakeTable':
        # cursor.execute('CREATE TABLE customer (name VARCHAR(255), address VARCHAR(255))')
        #cursor.execute("INSERT INTO customer (name, address) VALUES ('bob', '123'),('joe','123')")

        cursor.execute("SELECT * FROM customer")
        val1 = cursor.fetchall()

        cursor.execute("SELECT * FROM customer WHERE address = '123'")
        val2 = cursor.fetchall()
        
        conn.commit()
        conn.close()
        return {
            'val1':json.dumps(val1[0]),
            'val2':json.dumps(val2[0])
        }


#Login Page Functions
    # VerifyUser(user_id, hashed_pass)
    if event.get('type') == 'VerifyUser':
        if (event.get('user_id') and event.get('hashed_pass')):
            # database check will set database number
            # TODO DATABASE WORK
            database = 1
            
            if (database): # found in database
                return {
                    'statusCode': 200,
                    'responseValue': 1,
                }
            else: # not found in database
                return {
                    'statusCode': 404,
                    'responseValue': 0
                }
        else:
            return {
                'statusCode':404
            }
        
     # CreateAcct(email, hashed_pass)
    if event.get('type') == 'CreateAcct':
        if (event.get('email') and event.get('hashed_pass')):
            # database check will set database number
            # TODO DATABASE WORK
            database = 1
            
            if (database): # found in database
                return {
                    'statusCode': 200,
                    'responseValue': 1,
                }
            else: # not found in database
                return {
                    'statusCode': 404,
                    'responseValue': 0
                }
        else:
            return {
                'statusCode':404
            }
            
            
#Create Forum

    
    #CreateForum(workplace, addr, forum_name, user_id)       
    if event.get('type') == 'CreateForum':
        if (event.get('workplace') and event.get('addr') and event.get('forum_name') and event.get('user_id')):
            # database check will set database number
            # TODO DATABASE WORK
            database = 1
            
            if (database): # found in database
                return {
                    'statusCode': 200,
                    'responseValue': 1,
                }
            else: # not found in database
                return {
                    'statusCode': 404,
                    'responseValue': 0
                }
        else:
            return {
                'statusCode':404
            }
            
    
    
#User Dashboard Functions
    
    #GetUserForums(user_id)
    if event.get('type') == 'GetUserForums':
        if (event.get('user_id')):
            # database check will set database number
            # TODO DATABASE WORK
            database = 1
            
            if (database): # found in database
                return {
                    'statusCode': 200,
                    'responseValue': 1,
                }
            else: # not found in database
                return {
                    'statusCode': 404,
                    'responseValue': 0
                }
        else:
            return {
                'statusCode':404
            }
    
    
#Join Forum
    
    #AddUserToForum(user_id, forum_id)
    if event.get('type') == 'AddUserToForum':
        if (event.get('user_id') and event.get('forum_id')):
            # database check will set database number
            # TODO DATABASE WORK
            database = 1
            
            if (database): # found in database
                return {
                    'statusCode': 200,
                    'responseValue': 1,
                }
            else: # not found in database
                return {
                    'statusCode': 404,
                    'responseValue': 0
                }
        else:
            return {
                'statusCode':404
            }
    
    return {
        'statusCode': 200,
        'body': json.dumps('Request not defined!'),
        'userID': 1000,
        'event': event.get("userID")
    }
