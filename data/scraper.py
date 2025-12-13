import requests
import pandas as pd
import time
import random

# --- CONFIGURATION ---
TARGET_COUNT = 10000 
COMMENTS_PER_POST = 60
CHECKPOINT_INTERVAL = 500 # Save every 500 rows (Safety Net)

auto_subreddits = {
    "cscareerquestions": "CAREER_ANXIETY",
    "Layoffs": "CAREER_ANXIETY",
    "Singularity": "FUTURE_HYPE",
    "Futurology": "FUTURE_HYPE",
    "OpenAI": "FUTURE_HYPE"
}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
all_reviews = []

def save_checkpoint(data):
    """Saves the current progress to a file"""
    df = pd.DataFrame(data)
    df.to_csv("reddit_reviews_partial.csv", index=False)
    print(f"    >>> SAFEGUARD: Saved {len(df)} rows to reddit_reviews_partial.csv")

def get_json(url):
    for _ in range(3):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200: return response.json()
            elif response.status_code == 429:
                time.sleep(5)
        except: time.sleep(1)
    return None

def scrape_post_and_comments(permalink, label):
    url = f"https://www.reddit.com{permalink}.json" if permalink.startswith("/") else f"{permalink.split('?')[0]}.json"
    data = get_json(url)
    if not data: return

    # 1. Post
    try:
        post_data = data[0]['data']['children'][0]['data']
        selftext = post_data.get('selftext', '')
        if len(selftext) > 50:
            all_reviews.append({'text': post_data.get('title', '') + " " + selftext, 'label': label, 'type': 'post'})
    except: pass

    # 2. Comments
    try:
        comments = data[1]['data']['children']
        count = 0
        for comment in comments:
            if count >= COMMENTS_PER_POST: break
            if len(all_reviews) >= TARGET_COUNT: break
            
            body = comment.get('data', {}).get('body', '')
            if body and body != "[deleted]" and len(body) > 30:
                all_reviews.append({'text': body, 'label': label, 'type': 'comment'})
                count += 1
    except: pass

# --- MAIN LOOP ---
print(f"--- STARTING SAFETY MINER (Target: {TARGET_COUNT}) ---")

for sub, label in auto_subreddits.items():
    if len(all_reviews) >= TARGET_COUNT: break
    
    print(f"\n>>> Searching r/{sub}...")
    listing_url = f"https://www.reddit.com/r/{sub}/top.json?t=month&limit=100"
    data = get_json(listing_url)
    if not data: continue
    
    posts = data['data']['children']
    for i, post in enumerate(posts):
        if len(all_reviews) >= TARGET_COUNT: break
        
        permalink = post['data']['permalink']
        title = post['data']['title'][:30]
        print(f"  [{i+1}/{len(posts)}] Mining: {title}... (Total: {len(all_reviews)})")
        
        scrape_post_and_comments(permalink, label)
        
        # --- THE SAFETY CHECK ---
        if len(all_reviews) % CHECKPOINT_INTERVAL < 50 and len(all_reviews) > 0:
            save_checkpoint(all_reviews) # Saves every ~500 posts
            
        time.sleep(1.5)

# Final Save
df = pd.DataFrame(all_reviews)
df.to_csv("reddit_reviews_10k_FINAL.csv", index=False)
print(f"\nSUCCESS! Final count: {len(df)}")
