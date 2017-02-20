import tweepy
import consumer

def get_api():
    """Get authentication information and create API"""
    auth = tweepy.OAuthHandler(consumer.CONSUMER_KEY, consumer.CONSUMER_SECRET)
    auth.set_access_token(consumer.ACCESS_KEY, consumer.ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

def post_tweet(tweet, api):
    """Post tweet"""
    try:
        api.update_status(tweet)
    except tweepy.TweepError:
        print("Couldn't post tweet. Quitting!")
        quit()

def get_last_tweet(api, trump_handle, first_tweet):
    """Get last tweet"""
    last_tweet = api.user_timeline(count=1)
    try:
        last_tweet = last_tweet[0].text
    except IndexError:
        # this must be a new account. post the beginning and quit
        post_tweet(first_tweet, api)
        quit()

    # remove handle from last tweet
    last_tweet = last_tweet[len(trump_handle):]
    return last_tweet

def get_start_position(last_tweet, text):
    """Get current position in constitution based on last tweet"""
    start_position = text.index(last_tweet)
    start_position = start_position + len(last_tweet)
    return start_position

def get_constitution():
    """Get the US Constitution. Weep if it cannot be found."""
    try:
        with open('const.txt', 'r') as c:
            text = c.read()
            return text
    except FileNotFoundError:
        print("Couldn't find the US Constitution.")
        print("This is a sad day for America")
        quit()

def construct_tweet(start_position, end_position, max, max_tweet_increment, text, trump_handle):
    """Construct the tweet"""
    if start_position >= max:
        # we are past the end, let's go back to the beginning
        tweet = text[0:max_tweet_increment]
    elif end_position >= max:
        tweet = text[start_position:]
    else:
        tweet = text[start_position:end_position]
    tweet = trump_handle + tweet

    # get the last space in the tweet and rewind back
    try:
        if end_position < max:
            last_space = tweet.rindex(' ')
        else:
            last_space = len(tweet)
    except ValueError:
        last_space = len(tweet)

    tweet = tweet[:last_space]
    return tweet

def main():
    """Main function"""
    api = get_api() # get twitter api
    trump_handle = '.@realDonaldTrump\n'
    max_tweet_increment = 140 - len(trump_handle) # account for handle
    text = get_constitution()

    # set max words of constitution
    max = len(text)

    # get current position in the constitution
    last_tweet = get_last_tweet(api, trump_handle, text[0:max_tweet_increment])
    start_position = get_start_position(last_tweet, text)
    end_position = start_position + max_tweet_increment
    print(start_position)
    tweet = construct_tweet(start_position, end_position, max, max_tweet_increment, text, trump_handle)

    # print tweet for debugging
    print(tweet)

    # post tweet
    post_tweet(tweet, api)

# run
if __name__ == "__main__":
    main()
