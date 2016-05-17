import unittest
import requests
from yaml import load


class BaseTestApi(unittest.TestCase):

    def setUp(self):
        self.settings = load(open('settings.yaml').read())
        self.base_url = self.settings['base_url']
        login = self.settings['credentials']['login']
        pwd = self.settings['credentials']['password']
        self.creds = (login, pwd)

        params = {
            'login': self.settings['credentials']['login'],
            'password': self.settings['credentials']['password']
        }

        url = self.base_url + '/user/login'
        r = requests.post(url, data=params)
        self.cookies = r.cookies

    def create_issue(self):
        url = self.base_url + '/issue/'

        params = {
            'project': 'API',
            'summary': 'test_summary',
            'description': 'test_description'
        }

        r = requests.put(url, data=params, cookies=self.cookies)
        location = r.headers['Location']
        issue_id = location.split('/')[-1]

        return issue_id

    def delete_issue(self, issue_id):
        url = self.base_url + '/issue/' + issue_id
        r = requests.delete(url, cookies=self.cookies)
