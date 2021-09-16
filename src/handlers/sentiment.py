import json


def get_tweet_sentiment(event, context):
    """

    :param event: dict, required
        API Gateway Lambda Proxy Input Format
    :param context: object, required
        Lambda Context runtime methods and attributes
    :return: dict
        API Gateway Lambda Proxy Output Format
    """

    print('hello world')

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world"
        }),
    }
