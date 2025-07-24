#!/usr/bin/python3
"""Function that queries the Reddit API"""
import requests
import sys


def top_ten(subreddit):
    """Prints titles of first 10 hot posts for a given subreddit using sys"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'linux:0:1.0 (by /u/JuiceExtension6952)'}
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code != 200:
            sys.stdout.write("None\n")
            return

        posts = response.json().get("data", {}).get("children", [])

        if not posts:
            sys.stdout.write("None\n")
            return

        for post in posts:
            title = post.get("data", {}).get("title", "")
            sys.stdout.write(title + "\n")
    except Exception:
        sys.stdout.write("None\n")
