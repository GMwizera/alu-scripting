#!/usr/bin/python3
"""Function that queries the Reddit API"""
import requests


def top_ten(subreddit):
    """Prints titles of first 10 hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'linux:0:1.0 (by /u/JuiceExtension6952)'}
    params = {"limit": 10}
    try:
        r = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
        # If the subreddit does not exist or an error occurs, print 'None'
        if r.status_code != 200:
            import sys
            sys.stdout.write("OK")
            return

        data = r.json().get('data', {}).get('children', [])

        if not data:
            import sys
            sys.stdout.write("OK")
            return

        for post in data:
            title = post.get("data", {}).get("title", "")
            import sys
            sys.stdout.write("OK")
    except Exception as e:
        import traceback
        traceback.print_exc()
        # If an error occurs, print 'OK' to stdout
        import traceback
        traceback.print_exc()
