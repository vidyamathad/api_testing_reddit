
import os
import praw
from dotenv import load_dotenv

load_dotenv(dotenv_path="credentials.env")

# Get credentials from environment
CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# Check for missing credentials if not add print statement
if not all([CLIENT_ID, CLIENT_SECRET, USER_AGENT]):
    print("❌ Missing Reddit credentials. Check your environment file.")
    exit(1)

def fetch_latest_five_posts(subreddit_name, post_limit=5):
    try:
        reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent=USER_AGENT,
        )

        if not reddit.read_only:
            print("❌ Reddit authentication failed. Not in read-only mode.")
            return

        # Fetching latest 5 posts
        subreddit = reddit.subreddit(subreddit_name)
        print(f"\n Latest {post_limit} posts from r/{subreddit_name}:\n")
        for post in subreddit.new(limit=post_limit):
            print(f"Title  : {post.title}")
            print(f"Author : {post.author}")
            print(f"Upvotes: {post.score}")
            print("-" * 50)

    except Exception as e:
        print(f" Error fetching posts: {e}")

if __name__ == "__main__":
    # Change 'python' to any subreddit you like
    fetch_latest_five_posts("python")
