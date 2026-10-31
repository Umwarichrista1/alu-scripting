#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests

HEADERS = {"User-Agent": "alu-scripting:v1.0 (by /u/Umwarichrista1)"}


def top_ten(subreddit):
    """Print the first 10 hot post titles, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=HEADERS, params={"limit": 10},
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    for post in response.json().get("data", {}).get("children", []):
        print(post.get("data", {}).get("title"))
