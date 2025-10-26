#!/usr/bin/python3
"""
This module contains a functions that queries the Reddit API
and prints the titles of the first 10 hot posts listed for a
given subreddit.
"""

import requests
import sys


def number_of_subscribers(subreddit):
    "This function is used to obtain the number of subscribers of a subreddit"
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = { "User-Agent": "python:intranetassignment:apis-Jeremiah"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return 0
    else:
        output = response.json()
        return (output["data"])["hotposts"]
        """
        The return value is the number of subscribers of the subreddit
        """


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please pass an argument for the subreddit to search.")
        sys.exit(1)
    else:
        subreddit = sys.argv[1]
        """
        The Argv value is the subreddit that the user wants to know the number of subscribers.
        """
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)

# ...existing code...
subreddit = "learnpython"
import requests

def print_top_10_titles(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:top_ten_script:v1.0 (by /u/you)"}
    params = {"limit": 25}  # request extra so we can skip stickied posts
    resp = requests.get(url, headers=headers, params=params, timeout=10)
    resp.raise_for_status()
    posts = resp.json().get("data", {}).get("children", [])
    count = 0
    for post in posts:
        if post.get("data", {}).get("stickied"):
            continue
        title = post.get("data", {}).get("title", "[deleted]")
        count += 1
        print(f"{count}. {title}")
        if count >= 10:
            break

if __name__ == "__main__":
    print_top_10_titles(subreddit)
# ...existing code...