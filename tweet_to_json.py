import os
import tweepy 
import json
import argparse

# Twitter API credentials
consumer_key = "Consumer key goes here"
consumer_secret = "Consumer secret goes here"
access_key = "access key goes here"
access_secret = "access secret goes here"

def tweet_to_json(tweet_id, remove_url=True, write_json=True):
    """ Get json of a tweet.

    Inputs:
        - tweet_id: tweet identification number.
        - remove_url: boolean. If True, remove url from the text of the tweet.
        When calling the program from the command line, set this argument (the second one)
        to 0 in order no to remove the URL. Don't write anything as second argument 
        in order to remove the URL.
        - write_json: boolean. If True, writes the json file.

    """    
    # Authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    # Save actual path
    path = os.path.dirname(os.path.abspath(__file__))

    # Create directory to save the json file if it doesn't exist
    path_json = os.path.join(path, "Json files")
    if not os.path.exists(path_json):
        os.makedirs(path_json)
    
    # Save tweet
    tweet = api.get_status(tweet_id)

    # Save jason as a string
    json_str = json.dumps(tweet._json)

    # Parse json from string
    j = json.loads(json_str)

    ### ----------------------------------------
    # Remove the url from the text
    if remove_url:
        # Save url of the tweet
        j_url = j["entities"]["media"][0]["url"]
        
        # Save text from the tweet
        j_text = j["text"]
        
        # Remove url from text
        j["text"] = j_text.replace(j_url, "")
    ### ----------------------------------------
        
    # Write json
    if write_json:
        with open(os.path.join(path_json, ("tweet_" + tweet_id + ".json")), "w") as f:
            json.dump(j, f, sort_keys=True, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("tweet_id", help="Tweet id number")
    parser.add_argument("remove_url", nargs="?", help="True to remove URL from text")
    parser.parse_args()
    args = parser.parse_args()

    if args.remove_url is None:
        args.remove_url = 1

    tweet_to_json(args.tweet_id, int(args.remove_url))
    # try:
    #     tweet_to_json(args.tweet_id, int(args.remove_url))
    # except:
    #     print("Oops! There is no tweet with this ID number.")