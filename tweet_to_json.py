import os
import tweepy 
import json
import argparse

# Twitter API credentials
consumer_key =  "RXcyOZ1nnpEFuaCdOc6KhSsuK"
consumer_secret = "y9VzsaPmyLP34BcpJCzzV1FqYiemxwpEablbcr94obWfhN9v9d"
access_key = "277726408-imwLuQjIdAOHw2O75IOqwdFIjXfbcYjsyxZiTd29"
access_secret = "buqlZn4k4HkMJKAUj83DlcBadE15KE6OnfQr1v9C5rRvg"

def tweet_to_json(tweet_id, write_json=True):
    """ Get json of a tweet.

    Inputs:
        - tweet_id: tweet identification number.
        - write_json: boolean. If True, writes the json file.
    """    
    # Authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    

    # Save tweet
    tweet = api.get_status(tweet_id)

    # Save actual path
    path = os.path.dirname(os.path.abspath(__file__))

    # Create directory to save the json file if it doesn't exist
    path_json = os.path.join(path, "Json files")
    if not os.path.exists(path_json):
        os.makedirs(path_json)
    
    # Write json
    if write_json:
        with open(os.path.join(path_json, ("tweet_" + tweet_id + ".json")), "w") as f:
            json.dump(tweet._json, f, sort_keys=True, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("tweet_id", help="Tweet id number")
    parser.parse_args()
    args = parser.parse_args()
    try:
        tweet_to_json(args.tweet_id)
    except:
        print("Oops! There is no tweet with this ID number.")