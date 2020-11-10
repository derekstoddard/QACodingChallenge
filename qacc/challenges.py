'''
Created on Nov 8, 2020

@author: Derek Stoddard

Requires requests: https://requests.readthedocs.io/en/master/
python -m pip install requests
Version: requests==2.24.0
'''
import requests


class Challenges:

    def __init__(self, url):
        self.url = url

    def challenge_one(self, url):
        req = requests.get(url)
        return req.status_code
