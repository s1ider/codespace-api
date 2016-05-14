import unittest
import xmltodict
import requests
from yaml import load


class BaseAPITest(unittest.TestCase):

    def setUp(self):
        self.settings = load(open('settings.yaml').read())
        self.url = self.settings['url']
        self.creds = tuple(self.settings['credentials'].values())

    def create_issue(self):
        url = self.url + '/issue/'
        params = {
            'project': 'API',
            'summary': 'auto-generated test issue by robot',
            'description': 'hail the robots',
        }

        response = requests.put(url, data=params, auth=self.creds)
        issue_id = response.headers['location'].split('/')[-1]

        return issue_id
