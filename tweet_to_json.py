import os
import tweepy 
import json
import argparse
import urllib.request
from PIL import Image

# Twitter API credentials
consumer_key = "Consumer key goes here"
consumer_secret = "Consumer secret goes here"
access_key = "access key goes here"
access_secret = "access secret goes here"

def tweet_to_json(tweet_id, size_img=400, remove_url=True, write_json=True):
    """ Get json of a tweet.

    Inputs:
        - tweet_id: tweet identification number.
        - size_img: size to which the profile picture will be resized.
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
    tweet = api.get_status(tweet_id, tweet_mode='extended')

    # Save jason as a string
    json_str = json.dumps(tweet._json)

    # Parse json from string
    j = json.loads(json_str)

    ### ----------------------------------------
    # Remove the url from the text
    if remove_url:
        try:
            # Save url of the tweet
            j_url = j["entities"]["media"][0]["url"]
            
            # Save text from the tweet
            j_text = j["full_text"]
            
            # Remove url from text
            j["full_text"] = j_text.replace(j_url, "")
        except:
            pass
    ### ----------------------------------------
        
    # Write json
    if write_json:
        with open(os.path.join(path_json, ("tweet_" + tweet_id + ".json")), "w") as f:
            json.dump(j, f, sort_keys=True, indent=4)

    ### ----------------------------------------
    # Download profile picture of the user that posted the tweet
    # Create directory to save the images if it doesn't exist
    path_img = os.path.join(path, "images")
    if not os.path.exists(path_img):
        os.makedirs(path_img)
    # Save user name
    try:
        if j["user"]["screen_name"] != "":
            user_name = j["user"]["screen_name"]
        else:
            user_name = "user"
        
        profile_img = j["user"]["profile_image_url_https"]
        # Remove 'normal', so image is in full size
        profile_img = profile_img.replace("_normal", "")
        # Save image from URL
        saved_url = os.path.join(path_img, (user_name + "_profile_image.jpg"))
        urllib.request.urlretrieve(profile_img, saved_url)
        # Resize image to have the same size every time
        size = (size_img, size_img)
        img = Image.open(saved_url)
        img_resized = img.resize(size, Image.ANTIALIAS)
        img_resized.save(saved_url)
    except:
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("tweet_id", help="Tweet id number")
    parser.add_argument("size_img", nargs="?", default=400,
        help="Size of the resized profile picture")
    parser.add_argument("remove_url", nargs="?", default=True,
        help="True to remove URL from text")
    args = parser.parse_args()

    try:
        tweet_to_json(args.tweet_id, int(args.size_img), int(args.remove_url))
    except:
        print("Oops! Some error occurred. Perhaps, there is no tweet with this ID number.")