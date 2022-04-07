import tweepy

def get_tweets(Token):
    userID = "ubconews"

    client = tweepy.Client(bearer_token=Token)

    query = 'from:ubcokanagan -is:retweet'

    tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=10)

    return(f"{tweets.data[0].text}\n\n{tweets.data[1].text}\n\n{tweets.data[2].text}")
