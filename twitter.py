import GetOldTweets3 as got

def get_tweets():

        tweetCriteria = got.manager.TweetCriteria().setQuerySearch('corona virus')\
                                           .setSince("2019-08-01")\
                                           .setUntil("2020-09-30")\
                                           .setMaxTweets(10)
        tweet = got.manager.TweetManager.getTweets(tweetCriteria)
        print(tweet.text)

get_tweets()

