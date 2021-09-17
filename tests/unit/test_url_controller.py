from unittest import TestCase
from dependencies.python.url_controller import TwitterApi


class TestTwitterApi(TestCase):
    def test_create_twitter_url(self):
        twitter_user = 'Twitter'
        number_of_tweets = '50'
        url = TwitterApi.create_sentiment_url(twitter_user, number_of_tweets)
        expected_url = 'https://api.twitter.com/2/tweets/search/recent?max_results={}&query=from:{}'.format(
            number_of_tweets, twitter_user
        )

        self.assertEqual(url, expected_url)
