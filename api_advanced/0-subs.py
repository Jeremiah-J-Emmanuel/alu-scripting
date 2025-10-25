"""Query the Reddit API and return the number of subscribers for a given subreddit.
If the subreddit is invalid or not provided, the function returns 0.
"""

#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """function that fetches number_of_subscribers"""
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        return RESPONSE.json().get("data").get("subscribers")

    except Exception:
        return 0
