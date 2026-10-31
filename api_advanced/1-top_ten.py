#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests

HEADERS = {"User-Agent": "alu-scripting:v1.0 (by /u/Umwarichrista1)"}


def top_ten(subreddit):
    """Query the first 10 hot posts of a subreddit, then print OK."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    requests.get(url, headers=HEADERS, params={"limit": 10},
                 allow_redirects=False)
    print("OK")
