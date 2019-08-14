import json
def lambda_handler(event, context):
    print (event)
    if event['httpMethod'] == 'GET':
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "hello world",
                # "location": ip.text.replace("\n", "")
            })
        }
    else:
        return {
                'body': 'Hello there {0}'.format(event['requestContext']['identity']['sourceIp']),
                'headers': {
                'Content-Type': 'text/plain'
                },
                'statusCode': 200
            }