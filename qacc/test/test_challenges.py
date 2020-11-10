'''
Created on Nov 9, 2020

@author: Derek Stoddard

test_challenges.py > Run As > Python unit-test
'''
import unittest
from qacc.challenges import Challenges


class TestChallenges(unittest.TestCase):
    def test_challenge_one(self):
        url = 'https://www.google.com/'
        result = Challenges.challenge_one(self, url)
        self.assertEqual(result, 200)  # If site is up, expect 200

    if __name__ == '__main__':
        unittest.main()
