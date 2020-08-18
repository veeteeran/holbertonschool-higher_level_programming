#!/bin/bash
# Takes in a URL, sends a POST request to the passed URL,
# and displays the body of the response
curl -sX POST $1 -F "email=hr@holbertonschool.com" -F "subject=I will always be here for PLD"
