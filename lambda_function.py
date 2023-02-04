import json

def lambda_handler(event, context):
    if event.get('type') == 'VerifyUser':
        # required fields from front
        # userID, hashedpass
        if (event.get('userID') and event.get('hashedpass')):
            
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
