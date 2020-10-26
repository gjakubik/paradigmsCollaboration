import unittest
import requests
import json

class TestReset(unittest.TestCase):
    SITE_URL = 'http://localhost:51068' # replace with your port id
    print("Testing for server: " + SITE_URL)
    RESET_URL = SITE_URL + '/reset/'
    MOVIES_URL = SITE_URL + '/movies/'

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_put_reset_index(self):
        m = {}
        r = requests.put(self.RESET_URL, data = json.dumps(m))

        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

    def test_put_reset_key(self):
        movie_id = 95

        m = {}
        m['title'] = 'Broken Arrow (1996)'
        m['genres'] = 'Action|Thriller'
        r = requests.put(self.RESET_URL + str(movie_id), data = json.dumps({}))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.MOVIES_URL + str(movie_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['title'], m['title'])
        self.assertEqual(resp['genres'], m['genres'])

if __name__ == "__main__":
    unittest.main()

