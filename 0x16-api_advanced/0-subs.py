#!/usr/bin/python3
"""Script to get number of subscribers"""

import requests

def number_of_subscribers(subreddit):
    """function running the script"""

    url = "https://api.reddit.com/r/{}/about/".format(subreddit)
    uagent = {'User-agent': '0-subs'}
    r = requests.get(url, headers=uagent, allow_redirects=False)
    if r.status_code == 200:
        data = r.json()
        subs = data['data']['subscribers']
        return subs
    else:
        return 0
