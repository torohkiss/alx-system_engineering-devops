#!/usr/bin/python3

import requests


def top_ten(subreddit):
    url = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    u_agent = {'User-Agent': '/u/Suspicious-Jelly920'}

    r = requests.get(url, headers=u_agent)

    if r.status_code == 200:
        data = r.json()
        posts = data.get('data', {}).get('children', [])
        titles = [post['data']['title'] for post in posts]
        print(titles)
    else:
        print(None)
        """
        hottest_ten = r.json()["data"]["children"]

        count = 0
        for hot in hottest_ten:
            if count == 10:
                break
            print(hot["data"]["title"])
            count += 1
    else:
        print("None")"""
