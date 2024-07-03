import csv
import json
# import time
import praw
import prawcore
# from langdetect import detect
import tweepy


def load_credentials(filename):
    with open(filename, "r") as f:  # open the json file and load it
        return json.load(f)


def scrape_pulsechain_social_media(reddit_credentials_file, twitter_credentials_file, reddit_output_file,
                                   twitter_output_file):
    # Load the reddit credentials from the config file
    reddit_credentials = load_credentials(reddit_credentials_file)  # credentials = load_credentials(credentials_file)

    # Load the twitter credentials from the config file
    twitter_credentials = load_credentials(twitter_credentials_file)

    # Initialize the Reddit API wrapper
    reddit = praw.Reddit(client_id=reddit_credentials["reddit"]["client_id"],
                         client_secret=reddit_credentials["reddit"]["client_secret"],
                         user_agent=reddit_credentials["reddit"]["user_agent"])
    # Similarly initialize the Tweepy API wrapper
    auth = tweepy.OAuthHandler(twitter_credentials["api_key"], twitter_credentials["api_secret_key"])
    auth.set_access_token(twitter_credentials["access_token"], twitter_credentials["access_token_secret"])
    twitter_api = tweepy.API(auth)

    # output file paths
    reddit_output_file_path = '/Users/nectarioskisiigha/Documents/GitHub/pulsechain_sentiment_analysis/' + reddit_output_file
    twitter_output_file_path = '/Users/nectarioskisiigha/Documents/GitHub/pulsechain_sentiment_analysis/' + twitter_output_file

    # Initialize a list to store the extracted posts
    # pulsechain_posts = []

    # Open the CSV file for writing (for both Twitter and Reddit; however, done separately)
    with open(reddit_output_file_path, mode='w', newline='', encoding='utf-8') as reddit_csvfile, \
            open(twitter_output_file_path, mode='w', newline='', encoding='utf-8') as twitter_csvfile:

        # Reddit CSV writer
        reddit_fieldnames = ['Title', 'Comment']
        reddit_writer = csv.DictWriter(reddit_csvfile, fieldnames=reddit_fieldnames)
        reddit_writer.writeheader()

        # Twitter CSV writer
        twitter_fieldnames = ['Source', 'Content']
        twitter_writer = csv.DictWriter(twitter_csvfile, fieldnames=twitter_fieldnames)
        twitter_writer.writeheader()

        # Search for posts containing the specific keywords (e.g., pulsechain, PulseX, PLS, Richard Heart (founder)) not just r/pulsechain
        reddit_keywords = ["Pulsechain", "PulseX", "PLS", "PLSX"]
        twitter_keywords = ["#Pulsechain", "#PulseX", "#PLS", "#PLSX"]

        # Iterate through each keyword for Reddit
        for keyword in reddit_keywords:
            for submission in reddit.subreddit("all").search(keyword, limit=None):
                title = submission.title
                submission.comments.replace_more()  # Get all comments including the nested ones
                comments = submission.comments.list()

                # Write the title and comments to CSV file
                for comment in comments:
                    reddit_writer.writerow({'Title': title, 'Comment': comment.body})

        # Iterate through each keyword for Twitter
        for keyword in twitter_keywords:
            tweets = tweepy.Cursor(twitter_api.search_tweets, q=keyword, tweet_mode='extended').items()
            for tweet in tweets:
                if hasattr(tweet, 'retweeted_status'):  # Check if it's a retweet
                    twitter_writer.writerow({'Source': 'Twitter Retweet', 'Content': tweet.retweeted_status.full_text})
                else:
                    twitter_writer.writerow({'Source': 'Twitter Tweet', 'Content': tweet.full_text})

    """# open the CSV file for writing (for both twitter and Reddit; however, done separately)
    with open(reddit_output_file_path, mode='w', newline='', encoding='utf-8') as reddit_csvfile, \
        open(twitter_output_file_path, mode='w', newline='', encoding='utf-8') as twitter_csvfile:

        # Reddit csv writer
        reddit_fieldnames = ['Title', 'Comment']
        reddit_writer = csv.DictWriter(reddit_csvfile, fieldnames=reddit_fieldnames)
        reddit_writer.writeheader()

        # Twitter CSV writer
        twitter_fieldnames = ['Source', 'Content']
        twitter_writer = csv.DictWriter(twitter_csvfile, fieldnames=twitter_fieldnames)
        twitter_writer.writeheader()

        with open(twitter_output_file_path, mode='w', newline='', encoding='utf-8') as twitter_csvfile:
            twitter_fieldnames = ['Source', 'Content']
            twitter_writer = csv.DictWriter(twitter_csvfile, fieldnames=twitter_fieldnames)
            twitter_writer.writeheader()

            # Search for posts containing the specific keywords (e.g., pulsechain, PulseX, PLS, Richard Heart (founder)) not just r/pulsechain
            reddit_keywords = ["Pulsechain", "PulseX", "PLS", "PLSX"]  # subreddit = reddit.subreddit("pulsechain")
            twitter_keywords = ["#Pulsechain", "#PulseX", "#PLS", "#PLSX"] # prepend '#' to each word
            # Iterate through each keyword
            for keyword in reddit_keywords:
                # Collect the title and comments from Reddit
                for submission in reddit.subreddit("all").search(keyword, limit=None):
                    #Extract the title of the post
                    title = submission.title
                    #Extract the comments from the post
                    submission.comments.replace_more() #Get all comments including the nested ones
                    comments = submission.comments.list()

                    #write the title and comments to CSV file
                    for comment in comments:
                        reddit_writer.writerow({'Title': title, 'Comment': comment.body})
                    reddit_writer.writerow({'Title': 'Reddit', 'Content': title})

            # iterate through each keyword for Twitter
            for keyword in twitter_keywords:
            # collect tweets and retweets from Twitter
                tweets = tweepy.Cursor(twitter_api.search, q=keyword, tweet_mode='extended').items()
                for tweet in tweets:
                    if hasattr(tweet, 'retweeted_status'): # check if it's a retweet
                        twitter_writer.writerow({'Source': 'Twitter Retweet', 'Content': tweet.retweeted_status.full_text})
                    else:
                        twitter_writer.writerow({'Source': 'Twitter Tweet', 'Content': tweet.full_text})"""


# Examples usage:
if __name__ == "__main__":
    scrape_pulsechain_social_media("/Users/nectarioskisiigha/API_credentials/Reddit_API_credentials/redditconfig.json",
                                   "/Users/nectarioskisiigha/API_credentials/Twitter_API_credentials/twitterconfig.json",
                                   "reddit_data.csv",
                                   "twitter_data.csv"
                                   )

