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
        cursor.execute('CREATE TABLE Users (user_id INT, forum_id INT, email VARCHAR(255), passcode INT)')
        cursor.execute('CREATE TABLE Forums (forum_id INT, workplace VARCHAR(255), addr VARCHAR(255), forum_name VARCHAR(255))')
        cursor.execute('CREATE TABLE Messages (messages JSON, forum_id INT, message_number INT)')
        
        
        #cursor.execute("INSERT INTO customer (name, address) VALUES ('bob', '123'),('joe','123')")

        #cursor.execute("SELECT * FROM customer")
        #val1 = cursor.fetchall()

        #cursor.execute("SELECT * FROM customer WHERE address = '123'")
        #val2 = cursor.fetchall()
        
        conn.commit()
        conn.close()
        
        #return {
        #    'val1':json.dumps(val1[0]),
        #    'val2':json.dumps(val2[0])
        #}


#Login Page Functions
    # VerifyUser(email, passcode)
    if event.get('type') == 'VerifyUser':
        if (event.get('email') and event.get('passcode')):
            # database check will set database number
            # TODO DATABASE WORK
            cursor.execute("SELECT email,passcode FROM Users WHERE email = event.get('email') AND passcode = event.get('passcode')")
            result = cursor.fetchall()
            
            if (len(result)==0): # no user found in database
                return {
                    'statusCode': 404,
                    'responseValue': 0,
                }
            else: 
                if((result[0] != event.get('email')) or (result[1] != event.get('passcode')):
                    return {
                        'statusCode': 404,
                        'responseValue': 0
                    }
                else:
                    if((result[0] == event.get('email')) and (result[1] == event.get('passcode')):
                        return {
                            'statusCode': 200,
                            'responseValue': 1
                        }
        conn.commit()
        conn.close()
           
        
     # CreateAcct(user_id, email, hashed_pass)
    if event.get('type') == 'CreateAcct':
        if (event.get('user_id') and event.get('email') and event.get('passcode')):
            # database check will set database number
            # TODO DATABASE WORK
            cursor.execute("SELECT email FROM Users WHERE email = event.get('email')")          
            result = cursor.fetchall()
            
            if (len(result)==0): # no user found in database
                cursor.execute("INSERT INTO Users (user_id, forum_id, email, passcode) VALUES (event.get('user_id'), 0, event.get('email'), event.get('passcode'))")
                return 
                {
                    'statusCode': 200,
                    'responseValue': 1,
                }
            else: #a user with the same email exists
                return 
                {
                    'statusCode': 404,
                    'responseValue': 0
                }
        conn.commit()
        conn.close()
       


       
#Create Forum
    #CreateForum(workplace, addr, forum_name, forum_id)       
    if event.get('type') == 'CreateForum':
        if (event.get('forum_id') and event.get('workplace') and event.get('addr') and event.get('forum_name')):
            # database check will set database number
            # TODO DATABASE WORK
            cursor.execute("SELECT forum_id,forum_name FROM Forums WHERE forum_id = event.get('forum_id') AND forum_name = event.get('forum_name')")
            result = curson.fetchall()
            
            if (len(result)==0): # no forum found in database
                cursor.execute("INSERT INTO Forums (forum_id, workplace, addr, forum_name) VALUES (event.get('forum_id'), event.get('workplace'), event.get('addr'), event.get('forum_name'))")
                return 
                {
                    #Successful Add
                    'statusCode': 200,
                    'responseValue': 1,
                }
            else:
                return 
                {
                    #A forum with that id/name already exists
                    'statusCode': 404,
                    'responseValue': 0,
                }
        conn.commit()
        conn.close()    
            
         
    
#User Dashboard Functions
    #GetUserForums(user_id) return list of forum ids and names
    if event.get('type') == 'GetUserForums':
        if (event.get('user_id')):
            # database check will set database number
            # TODO DATABASE WORK
            cursor.execute("SELECT forum_id FROM Users WHERE user_id = event.get('user_id')")
            result = cursor.fetchall()
            
            if (len(result)==0): # no forum attached to user in database
                return 
                {
                    #Search failure
                    'statusCode': 404,
                    'responseValue': 0
                }
            else: #At least one forum found attached to user
                forum_list = []
                for row in result:
                    cursor.execute("SELECT forum_id, forum_name FROM Forums WHERE forum_id = row[0]")
                    forum_info = cursor.fetchall() #list of a single two tuple
                    forum_list.append(forum_info[0])  
                return
                {
                    'forum_list':json.dumps(forum_list)
                }
        conn.commit()
        conn.close()

#Join Forum
    #AddUserToForum(user_id, forum_id)
    if (event.get('type') == 'AddUserToForum'):
        if (event.get('user_id') and event.get('forum_id')):
            # database check will set database number
            # TODO DATABASE WORK
            cursor.execute("SELECT user_id, forum_id FROM Users WHERE user_id = event.get('user_id') AND forum_id =  event.get('forum_id')")
            result = cursor.fetchall()
            
            if(len(result) == 0):
                
            
            for row in result:
                if(row[1] == 0): 
                    cursor.execute("UPDATE Users SET forum_id = event.get('forum_id') WHERE user_id = event.get('user_id') AND forum_id = 0")
                else:
                    

            
            
            
            
            
            
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
