import json
import requests

# noinspection PyUnresolvedReferences
from aws_controller import AwsSecretsManager, AwsComprehend
# noinspection PyUnresolvedReferences
from event_controller import SentimentFunctionEvent
# noinspection PyUnresolvedReferences
from url_controller import TwitterApi


# noinspection PyUnusedLocal
def get_tweet_sentiment(event, context):
    """
    :param event: dict, required
        API Gateway Lambda Proxy Input Format
    :param context: object, required
        Lambda Context runtime methods and attributes
    :return: dict
        API Gateway Lambda Proxy Output Format
    """

    # Unwrap query string parameters
    twitter_user, number_of_tweets = SentimentFunctionEvent.unwrap_parameters(event)

    # URL creation & authentication
    twitter_url = TwitterApi.create_sentiment_url(twitter_user, number_of_tweets)
    twitter_key = AwsSecretsManager.get_secret(secret_name='tweet-analysis-keys')
    twitter_header = {"Authorization": "Bearer {}".format(twitter_key['BEARER'])}

    # Request tweets to Twitter
    twitter_response = requests.request("GET", twitter_url, headers=twitter_header)
    twitter_json_response = twitter_response.json()

    tweets = []
    for tweet in twitter_json_response['data']['tweets']:
        tweets.append(tweet['text'])

    # Analyse tweets with AWS Comprehend
    result = AwsComprehend.get_sentiment(tweets)

    return {
        "statusCode": 200,
        "body": {
            "tweets": json.dumps(result)
        }
    }
