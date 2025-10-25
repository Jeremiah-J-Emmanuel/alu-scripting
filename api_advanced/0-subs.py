#!/usr/bin/python3

"""
Query the Reddit API and return the number of subscribers for a given subreddit.
If the subreddit is invalid or not provided, the function returns 0.
"""

import requests
import sys


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:intranetassignment:apis-Jeremiah"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return 0
    output = response.json()
    return output["data"]["subscribers"]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please pass an argument for the subreddit to search.")
        sys.exit(1)

    subreddit = sys.argv[1]
    subscribers = number_of_subscribers(subreddit)
    print(subscribers)
