#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    r = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json", headers = {'User-Agent': '0-subs.py'}, allow_redirects=False)

    if r.status_code == 200:
        data = r.json()
        total_subscribers = data['data']['subscribers']
        return total_subscribers
    else:
        return 0
