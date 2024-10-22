import json

def lambda_handler(event, context):
    # Log the incoming event for debugging
    print("Event:", event)
    
    # Example logic for testing
    message = "Hello from test----  !"
    
    # Example response
    response = {
        'statusCode': 200,
        'body': json.dumps({
            'message': message,
            'input_event': event
        })
    }
   #new line

    return response
