import datetime as dt
import pandas as pd
import praw

from .config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

def get_reddit_instance():
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )
    return reddit

def collect_posts(subreddit_name="Diamonds", limit=3000):
    reddit = get_reddit_instance()
    subreddit = reddit.subreddit(subreddit_name)

    records = []
    for submission in subreddit.new(limit=limit):
        text = submission.selftext if submission.selftext else ""
        if len(text.strip()) == 0 and not submission.title:
            continue

        records.append({
            "id": submission.id,
            "type": "post",
            "title": submission.title,
            "text": text,
            "flair": submission.link_flair_text,
            "score": submission.score,
            "timestamp": dt.datetime.fromtimestamp(submission.created_utc),
            "url": submission.url
        })
    return pd.DataFrame(records)

def collect_comments(post_ids, limit_per_post=50):
    reddit = get_reddit_instance()
    records = []

    for pid in post_ids:
        submission = reddit.submission(id=pid)
        submission.comments.replace_more(limit=0)
        for comment in submission.comments[:limit_per_post]:
            text = getattr(comment, "body", None)
            if not text or len(text.strip()) == 0:
                continue
            records.append({
                "id": comment.id,
                "parent_post_id": pid,
                "type": "comment",
                "title": None,
                "text": text,
                "flair": None,
                "score": comment.score,
                "timestamp": dt.datetime.fromtimestamp(comment.created_utc),
                "url": f"https://reddit.com{comment.permalink}"
            })
    return pd.DataFrame(records)

def build_corpus(subreddit_name="Diamonds", post_limit=3000, comment_limit_per_post=50):
    posts_df = collect_posts(subreddit_name=subreddit_name, limit=post_limit)
    comments_df = collect_comments(posts_df["id"].tolist(), limit_per_post=comment_limit_per_post)

    corpus_df = pd.concat([posts_df, comments_df], ignore_index=True)
    return corpus_df