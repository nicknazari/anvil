import json

def lambda_handler(event, context):
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

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        'userID': 1000,
        'event': event.get("userID")
    }
