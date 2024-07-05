import csv
import json
import time
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
    twitter_api = tweepy.API(auth, wait_onrate_limit=True, wait_on_rate_limit_notify=True) # Adding rate limit handling to Tweepy API Initialization

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
            try:
                for submission in reddit.subreddit("all").search(keyword, limit=None):
                    title = submission.title
                    submission.comments.replace_more()  # Get all comments including the nested ones
                    comments = submission.comments.list()

                    # Write the title and comments to CSV file
                    for comment in comments:
                        reddit_writer.writerow({'Title': title, 'Comment': comment.body})
                    time.sleep(2) # Add a delay between requests to avoid hitting the subreddit rate limit
                    #Adding an exception handling for rate limit exceedance
            except prawcore.exceptions.TooManyRequests as e: #try-except block to handle 'TooManyRequests' exceptions
                print(f"Rate limit exceeded for Reddit: {e}")
                time.sleep(60) # wait before retrying
            except Exception as e:
                print(f"And error occured while processing Reddit data: {e}")

        # Iterate through each keyword for Twitter
        for keyword in twitter_keywords:
            try:
                print(f"Searching tweets for keywords: {keyword}")  # debugging statement
                tweets = tweepy.Cursor(twitter_api.search_tweets, q=keyword, tweet_mode='extended').items()
                for tweet in tweets:
                    if hasattr(tweet, 'retweeted_status'):
                        content = tweet.retweeted_status.full_text  # Retweet
                        source = 'Twitter Retweet'
                    else:
                        content = tweet.full_text  # Tweet
                        source = 'Twitter Tweet'

                    print(f'Tweet fetched: {content}')  # Debugging statement if tweets are being fetched
                    twitter_writer.writerow({'Source': source, 'Content': content})  # Write tweet content once
                print(f"Finished writing tweets for keyword: {keyword}")
            except tweepy.TweepError as e:  # Handle 'TweepError' and other exceptions for Twitter
                print(f"An error occurred with the Twitter API: {e}")
            except Exception as e:
                print(f"An error occurred while processing Twitter data: {e}")

# Examples usage:
if __name__ == "__main__":
    scrape_pulsechain_social_media("/Users/nectarioskisiigha/API_credentials/Reddit_API_credentials/redditconfig.json",
                                   "/Users/nectarioskisiigha/API_credentials/Twitter_API_credentials/twitterconfig.json",
                                   "reddit_data.csv",
                                   "twitter_data.csv"
                                   )

