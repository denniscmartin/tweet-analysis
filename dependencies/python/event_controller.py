class SentimentFunctionEvent:

    @staticmethod
    def unwrap_parameters(event):
        """
        Unwrap string parameters from /sentiment api call
        :param event: dict, required
            API Gateway Lambda Proxy Input Format
        :return:
        """

        twitter_user = 'Twitter'
        number_of_tweets = '100'

        query_string_parameters = event['queryStringParameters']
        if event['queryStringParameters'] is not None:
            if 'twitterUser' in query_string_parameters:
                twitter_user = query_string_parameters['twitterUser']
                if not twitter_user:
                    twitter_user = 'Twitter'

            if 'numberOfTweets' in query_string_parameters:
                number_of_tweets = query_string_parameters['numberOfTweets']
                if not number_of_tweets:
                    number_of_tweets = '100'

        return twitter_user, number_of_tweets
