class TwitterApi:

    @staticmethod
    def create_sentiment_url(twitter_user, number_of_tweets):
        """
        Create url to fetch `max_results` of tweets from `user`
        :param twitter_user: string, required
        :param number_of_tweets: int, required
        :return: string url
        """

        query = 'query=from:{}'.format(twitter_user)
        url = 'https://api.twitter.com/2/tweets/search/recent?max_results={}&{}'.format(number_of_tweets, query)

        return url
