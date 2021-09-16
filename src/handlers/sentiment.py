import json
import requests
import boto3
import base64
from botocore.exceptions import ClientError


def get_tweet_sentiment(event, context):
    """
    :param event: dict, required
        API Gateway Lambda Proxy Input Format
    :param context: object, required
        Lambda Context runtime methods and attributes
    :return: dict
        API Gateway Lambda Proxy Output Format
    """

    twitter_url = create_twitter_url(user='dennisconcep')
    twitter_key = get_twitter_key()
    bearer_token = twitter_key['BEARER']
    twitter_header = {"Authorization": "Bearer {}".format(bearer_token)}  # Auth header
    twitter_response = requests.request("GET", twitter_url, headers=twitter_header)
    print(twitter_response.json())

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }


def create_twitter_url(user, max_results=100):
    """
    Create url to fetch `max_results` of tweets from `user`
    :param user: string, required
    :param max_results: int, optional, default 100
    :return: string url
    """

    formatted_max_results = 'max_results={}'.format(max_results)
    formatted_user = 'query=from:{}'.format(user)
    url = "https://api.twitter.com/2/tweets/search/recent?{}&{}".format(formatted_max_results, formatted_user)

    return url


def get_twitter_key():
    """
    Get Twitter Api Key from AWS Secrets Manager
    :return:
    """
    secret_name = "tweet-analysis-keys"
    region_name = "eu-west-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current state of the resource.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # We can't find the resource that you asked for.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
    else:
        # Decrypts secret using the associated KMS CMK.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            secret = base64.b64decode(get_secret_value_response['SecretBinary'])

        return json.loads(secret)
