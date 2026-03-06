import os
import re
import logging
import praw
from dotenv import load_dotenv

# Configure logging for backend monitoring and research tracking
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Load environment variables for secure credential management
load_dotenv()

def sanitize_text(raw_text):
    """
    Cleans raw Reddit text for NLP processing.
    Removes URLs, markdown formatting, and standardizes spacing.
    """
    # Strip URLs
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', raw_text)
    # Strip basic Markdown styling
    text = re.sub(r'[*_~]', '', text)
    # Normalize whitespace
    text = ' '.join(text.split())
    return text

def initialize_reddit_client():
    """
    Initializes a STRICTLY READ-ONLY PRAW instance.
    Requires Reddit Data API approval to function.
    """
    try:
        reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT")
        )
        # Verify the instance is read-only for API compliance
        logging.info(f"Reddit Client Initialized. Read-Only Mode: {reddit.read_only}")
        return reddit
    except Exception as e:
        logging.error(f"Failed to initialize Reddit client: {e}")
        return None

def stream_and_process_sentiment(reddit_client, subreddits="investing+wallstreetbets+pennystocks"):
    """
    Streams new submissions, sanitizes the text, and prepares it for the NLP engine.
    Respects all built-in PRAW rate limits (max 100 requests/minute).
    """
    logging.info(f"Starting read-only stream for: {subreddits}")
    subreddit_stream = reddit_client.subreddit(subreddits)

    try:
        # skip_existing=True ensures we only process live, forward-looking data
        for submission in subreddit_stream.stream.submissions(skip_existing=True):
            
            # Extract and sanitize only the necessary text fields
            title = sanitize_text(submission.title)
            body = sanitize_text(submission.selftext)
            
            combined_text = f"{title}. {body}"
            
            # Skip empty or media-only posts (images/videos)
            if len(combined_text) < 10:
                continue
                
            logging.info(f"Extracted
