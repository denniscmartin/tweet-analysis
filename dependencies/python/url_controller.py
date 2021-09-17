def create_twitter_url(twitter_user, number_of_tweets):
    """
    Create url to fetch `max_results` of tweets from `user`
    :param twitter_user: string, required
    :param number_of_tweets: int, required
    :return: string url
    """

    formatted_max_results = 'max_results={}'.format(number_of_tweets)
    formatted_user = 'query=from:{}'.format(twitter_user)
    url = "https://api.twitter.com/2/tweets/search/recent?{}&{}".format(formatted_max_results, formatted_user)

    return url
