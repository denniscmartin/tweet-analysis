import requests

# noinspection PyUnresolvedReferences
from secrets_controller import get_secret
# noinspection PyUnresolvedReferences
from event_controller import unwrap_sentiment_string_parameters
# noinspection PyUnresolvedReferences
from url_controller import create_twitter_url


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
    twitter_user, number_of_tweets = unwrap_sentiment_string_parameters(event)

    # URL creation & authentication
    twitter_url = create_twitter_url(twitter_user, number_of_tweets)
    twitter_key = get_secret(secret_name='tweet-analysis-keys')
    twitter_header = {"Authorization": "Bearer {}".format(twitter_key['BEARER'])}

    # Request tweets to Twitter
    twitter_response = requests.request("GET", twitter_url, headers=twitter_header)

    # Analyse tweets with AWS Comprehend

    return {
        "statusCode": 200,
        "body": {
            "tweets": twitter_response.json()
        }
    }
