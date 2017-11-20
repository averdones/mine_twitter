# **Mine twitter**

This is part of a larger project with the objective of automatically displaying **Twitter data in Adobe After Effects CC from a JSON file**. My friend Arturo Bracero posted a [complete tutorial](http://www.arturobracero.com/how-to-import-json-files-in-after-effects-cc-2018-to-display-twitter-data/) about this topic on his personal blog.

In this repository, the python script _tweet_to_json.py_ contains the necessary code to extract a JSON file from a _tweet ID_ (the digits at the end of a tweet URL).

## Using the script

First of all, you need to obtain your Twitter API credentials from [https://apps.twitter.com/](https://apps.twitter.com/), if you still haven't done it.

Once you have it, simply substitute your own credentials on the four lines following the comment _Twitter API credentials_.

Then, you just call the program as ```python tweet_to_json.py TWEET_ID```, where _TWEET_ID_ should be the numeric ID of the wanted tweet. For example, to get the JSON file from [this tweet](https://twitter.com/goodfellow_ian/status/932728419640492032), run:

	python tweet_to_json.py 932728419640492032

### Optional arguments

When calling the script, apart from the JSON file, the profile picture of the user that posted the tweet will also be saved. The image will be saved to _400x400_ pixels by default. Adding an additional argument after the tweet ID while calling the script modifies the size of the saved image. For example, running the following code saves the image to _1000x1000_ pixels:

	python tweet_to_json.py 932728419640492032 1000
