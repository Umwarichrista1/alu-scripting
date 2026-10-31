#!/usr/bin/python3
"""Return the number of subscribers of a subreddit."""
import requests

HEADERS = {"User-Agent": "alu-scripting:v1.0 (by /u/Umwarichrista1)"}


def number_of_subscribers(subreddit):
    """Return total subscribers of a subreddit, or 0 if it is invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=HEADERS, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get("data", {}).get("subscribers", 0)
