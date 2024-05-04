import csv
import json
#import time
import praw
import prawcore


def load_credentials(filename):
    with open(filename, "r") as f:
        return json.load(f)

def scrape_pulsechain_reddit_posts(credentials_file, output_file):
    #Load the credentials from the config file
    credentials = load_credentials(credentials_file)

    # Initialize the Reddit API wrapper
    reddit = praw.Reddit(client_id=credentials["reddit"]["client_id"],
                         client_secret=credentials["reddit"]["client_secret"],
                         user_agent=credentials["reddit"]["user_agent"])

    # Subreddit to scrape (e.g., pulsechain, PLSX, PLS) not just r/pulsechain
    subreddits = ["pulsechain", "PLSX", "PLS"] #subreddit = reddit.subreddit("pulsechain")

    # Initialize a list to store the extracted posts
    # pulsechain_posts = []

    """# Iterate through the top 10 hot posts in the subreddit
    for post in subreddit.hot(limit=10):
        # Extract the title and content of the post
        title = post.title
        content = post.selftext

        # Store the title and content as a dictionary
        pulsechain_posts.append({"title": title, "content": content})

    return pulsechain_posts"""

    #output file path
    output_file_path = '/Users/nectarioskisiigha/Documents/GitHub/pulsechain_sentiment_analysis/' + output_file

    # open the CSV file for writing
    with open(output_file_path, mode='w', newline='', encoding='utf-8') as  csvfile:
        fieldnames = ['Tile', 'Comment']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Iterate through each subreddit
        for subreddit_name in subreddits:
            subreddit = reddit.subreddit(subreddit_name)

            try:
                # Iterate through all the hot posts in the subreddit
                for post in subreddit.hot(): # (limit=100): extracts only the top 100 posts
                    #Extract the title and content of the post
                    title = post.title
                    #content = post.selftext

                    # Store the title and content as a dictionary
                    # pulsechain_posts.append({"title": title, "content": content})

                    #Extract comments from the post
                    post.comments.replace_more() # (limit=None) # Get all comments including the nested ones
                    comments = post.comments.list()

                    # write title and comments to csv file
                    for comment in comments:
                        writer.writerow({'Title': title, 'Comment': comment.body})
                        #comment_body = comment.body
                        #Store the comment body
                        #pulsechain_posts.append({"title": title, "comment": comment})

                        # Add a delay to avoid hitting the API rate limit
                        #time.sleep(1)  # Sleep for 1 second between requests
            except prawcore.exceptions.NotFound as e:
                #try-except block to catch the 'prawcore.exceptions.NotFound' exceptions
                print(f"Subreddit '{subreddit_name}' not found or has insufficient posts: {e}")

        #return pulsechain_posts


# Examples usage:
if __name__ == "__main__":
    scrape_pulsechain_reddit_posts("/Users/nectarioskisiigha/Reddit_API_credentials/config.json", "reddit_date.csv")


    """# Load credentials from the config file
    credentials = load_credentials("/Users/nectarioskisiigha/Reddit_API_credentials/config.json")"""

    # Scrape Pulsechain Reddit posts
    #pulsechain_posts = scrape_pulsechain_reddit_posts("/Users/nectarioskisiigha/Reddit_API_credentials/config.json")

    """# print the scraped data without repeating the title at every instance
    for title, comments in scrape_pulsechain_posts.items():
        print("Title:", title)
        for comment in comments:
            print("Comment:", comment)
        print()"""

    """# Print the scrapped posts
    for post in pulsechain_posts:
        if "content" in post:
            print("Title:", post["title"])
            print("Content:", post["content"])
        elif "comment" in post:
            print("Title:", post["title"])
            print("Comment:", post["comment"])
        print()"""


