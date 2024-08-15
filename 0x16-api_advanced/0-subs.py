#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    u_agent = {'User-Agent': '/u/Suspicious-Jelly920'}
    url = 'https://api.reddit.com/r/{}/about/'.format(subreddit)
    #url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url,  headers=u_agent)

    if r.status_code == 200:
        data = r.json()
        total_subscribers = data['data']['subscribers']
    else:
        total_subscribers = 0
    return total_subscribers
