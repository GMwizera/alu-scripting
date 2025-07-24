#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    
    Args:
        subreddit (str): The subreddit to query
        
    Returns:
        None: Prints the titles or None if invalid subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return
    
    # Reddit API URL for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    
    # Set custom User-Agent to avoid Too Many Requests error
    headers = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'
    }
    
    # Parameters to limit results to 10 posts
    params = {
        'limit': 10
    }
    
    try:
        # Make the request without following redirects
        response = requests.get(url, headers=headers, params=params, 
                               allow_redirects=False, timeout=30)
        
        # Check if we got redirected (invalid subreddit)
        if response.status_code == 302:
            print("None")
            return
            
        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            
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
            
    except (requests.RequestException, ValueError, KeyError):
        print("None")