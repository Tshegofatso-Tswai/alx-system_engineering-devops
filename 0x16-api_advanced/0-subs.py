#!/usr/bin/python3
"""Query Reddit API to determine subreddit sub count
"""

import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0"}  # Custom User-Agent header required
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
