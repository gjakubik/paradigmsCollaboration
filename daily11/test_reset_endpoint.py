import unittest
import requests
import json

class TestReset(unittest.TestCase):
    SITE_URL = 'http://localhost:51068' # replace with your port id
    print("Testing for server: " + SITE_URL)
    RESET_URL = SITE_URL + '/reset/'

    def test_put_reset_index(self):
        m = {}
        r = requests.put(self.RESET_URL)
        #TODO complete this test

    def test_put_reset_key(self):
        pass
        #TODO write this entire test

if __name__ == "__main__":
    unittest.main()

