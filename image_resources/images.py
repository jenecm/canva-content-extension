import json


def lambda_handler(event, context):
    """Sample Canva content extension

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    return {
        "statusCode": 200,
        "body": json.dumps({
            "type": 'SUCCESS',
            "resources": [
                {
                    "type": 'IMAGE',
                    "id": '123456',
                    "name": 'Flowers',
                    "thumbnail": {
                        "url": 'https://picsum.photos/id/152/500/333',
                        "width": 500,
                        "height": 333,
                    },
                    "url": 'https://picsum.photos/id/152/3888/2592',
                    "contentType": 'image/jpeg',
                },
            ],
        }),
    }
