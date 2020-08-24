#!/usr/bin/python3
"""Takes your Github credentials (username and password) and uses
   the Github API to display your id
"""
from requests import get, post
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo, owner)
    r = get(url)
    commits = r.json()
    for i in range(len(commits) - 11, len(commits)):
        print('{} {}'.format(commits[i]['sha'],
                             commits[i]['commit']['author']['name']))
