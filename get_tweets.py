import twitter
import json
import sys

LAST_TWEET="LAST_TWEET"

def get_status(api, id):
    # test 758873275044798464
    status = api.GetStatus(status_id=id)

    return status

def get_timeline_tweets(api, tweet_file, max_id):
    stata = api.GetUserTimeline(screen_name='realDonaldTrump', exclude_replies=True, count=200, max_id=max_id)
    last_id = stata[-1].id

    for status in stata:
        tweet_file.write('%s\n' % (status.AsJsonString()))

    return last_id

def get_timeline_tweets_since(api, tweet_file, since_id):
    stata = api.GetUserTimeline(screen_name='realDonaldTrump', exclude_replies=True, count=200, since_id=since_id)

    first_id = stata[0].id


    for status in stata:
        tweet_file.write('%s\n' % (status.AsJsonString()))

    return first_id

def main():
    # meekmeek credentials
    api = twitter.Api(consumer_key='eCKx5TBJ42FtzwkcgJM19Q',
                      consumer_secret='VuRYfuXX9PvzDU6EQ6PGn3DEyTnfEDOdqkSXD8G0',
                      access_token_key='10711302-CPXQxC3pjAzl4412SKa8LdJibw2BdIBvD7B4MgtAs',
                      access_token_secret='vcvsx6NVkUBhyYgV1D2iT5FdQgOUiXxQqyDbz7lU')


    # get the last tweet
    index_file = open(LAST_TWEET, 'r')
    last_tweet = index_file.read()
    index_file.close()
    
    # push all tweets into a file
    tweet_file = open('tweets-since-%s' % last_tweet, 'wb')

    # get all the tweets since
    try:
        last_tweet = get_timeline_tweets_since(api, tweet_file, last_tweet)
    except IndexError, ex:
        print "No more tweets (%s)" % ex
        sys.exit(0)
    finally:
        tweet_file.close()

        # update LAST_TWEET
        index_file = open(LAST_TWEET, 'w')
        index_file.write(str(last_tweet))
        index_file.close()

    # for loading historical data
    #current_id = get_timeline_tweets(api, tweet_file, max_id=None)
    #while current_id > 0:
    #    current_id = get_timeline_tweets(api, tweet_file, max_id=current_id)
    #    print current_id

if __name__ == "__main__":
    main()

