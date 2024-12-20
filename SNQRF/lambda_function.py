import json
import os

def lambda_handler(event, context):
    response = {
        "statusCode": 200,
        "statusDescription": "200 OK",
        "isBase64Encoded": False,
        "headers": {
        "Content-Type": "text/html; charset=utf-8"
        }
    }

    file_path = os.path.join(os.path.dirname(__file__), 'SNQuickRefPage.html')

    try:
        # Read the contents of the htmlCode file
        with open(file_path, 'r') as file:
            html_content = file.read()

        # Set the body to the file content
        response['body'] = html_content

    except Exception as e:
        # Handle any exceptions (e.g., file not found)
        response['statusCode'] = 500
        response['body'] = f"Error reading the file: {str(e)}"

    # Return the response
    return response
