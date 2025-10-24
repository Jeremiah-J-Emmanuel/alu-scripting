#!/usr/bin/env python3

import requests
import sys

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = { "User-Agent": "python:intranetassignment:apis-Jeremiah"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return 0
    else:
        output = response.json()
        return (output["data"])["subscribers"]



if len(sys.argv) != 2:
    print("Please pass an argument for the subreddit to search.")
    sys.exit(1)
else:
    subreddit = sys.argv[1]
    subscribers = number_of_subscribers(subreddit)
    print(subscribers)