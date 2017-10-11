def lambda_handler(event, context):
    print("test")
    
    resp = {
        "statusCode": "200",
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": "I will do the decrypting here."
    }