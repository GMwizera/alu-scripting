#!/usr/bin/python3
"""Function that queries the Reddit API and prints top 10 hot post titles"""
import requests
import sys


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts from a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:top_ten:v1.0 (by /u/your_username)"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        top_ten(sys.argv[1])
    else:
        print("Usage: ./1-top_ten.py <subreddit>")

