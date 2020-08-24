#!/usr/bin/python3
"""List 10 commits (from the most recent to oldest) of the repository
   “rails” by the user “rails”
"""
from requests import get, post
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    r = get(url)
    commits = r.json()
    counter = 0
    for commit in commits:
        if counter == 10:
            break
        print('{}: {}'.format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
        counter += 1
