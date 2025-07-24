#!/usr/bin/python3
"""Function that queries the Reddit API"""
import requests


def top_ten(subreddit):
    """Prints titles of first 10 hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'linux:0:1.0 (by /u/JuiceExtension6952)'}
    params = {"limit": 10}

    try:
        r = requests.get(url, headers=headers, params=params,
                         allow_redirects=False)

        # Check if we got redirected (invalid subreddit)
        if r.status_code == 302:
            print("None")
            return

        # Check if request was successful
        if r.status_code == 200:
            data = r.json()

            # Check if we have the expected data structure
            if 'data' in data and 'children' in data['data']:
                posts = data['data']['children']

                # Print titles of the first 10 hot posts
                for post in posts:
                    if 'data' in post and 'title' in post['data']:
                        print(post['data']['title'])
            else:
                print("None")
        else:
            print("None")

    except Exception:
        print("None")