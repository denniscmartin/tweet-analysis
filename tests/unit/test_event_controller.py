from unittest import TestCase
from dependencies.python.event_controller import *


class TestUnwrapStringParameters(TestCase):

    @staticmethod
    def create_event(query_string_parameter):
        event = {
            "resource": "/sentiment",
            "path": "/sentiment",
            "httpMethod": "GET",
            "isBase64Encoded": False,
            "queryStringParameters": query_string_parameter
        }

        return event

    def test_unwrap_sentiment_string_parameters(self):
        test_cases = {
            '1': None,
            '2': {'twitterUser': ''},
            '3': {'twitterUser': 'dennisconcep'},
            '4': {'numberOfTweets': ''},
            '5': {'numberOfTweets': '50'},
            '6': {'twitterUser': 'dennisconcep', 'numberOfTweets': '50'}
        }

        expected_results = {
            '1': {'twitterUser': 'Twitter', 'numberOfTweets': '100'},
            '2': {'twitterUser': 'Twitter', 'numberOfTweets': '100'},
            '3': {'twitterUser': 'dennisconcep', 'numberOfTweets': '100'},
            '4': {'twitterUser': 'Twitter', 'numberOfTweets': '100'},
            '5': {'twitterUser': 'Twitter', 'numberOfTweets': '50'},
            '6': {'twitterUser': 'dennisconcep', 'numberOfTweets': '50'}
        }

        for test_number in test_cases:
            event = self.create_event(test_cases[test_number])
            twitter_user, number_of_tweets = unwrap_sentiment_string_parameters(event)
            expected_twitter_user = expected_results[test_number]['twitterUser']
            expected_number_of_tweets = expected_results[test_number]['numberOfTweets']

            self.assertEqual(twitter_user, expected_twitter_user)
            self.assertEqual(number_of_tweets, expected_number_of_tweets)
