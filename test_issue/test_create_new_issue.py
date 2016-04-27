import requests
import unittest
from base_test import BaseAPITest
from yaml import load


class TestCreatNewIssue(BaseAPITest):

    def setUp(self):
        super(TestCreatNewIssue, self).setUp()
        self.url = self.settings['url'] + '/issue/'

    def test_create_valid_issue(self):
        params = {
            'project': 'API',
            'summary': 'test issue by robot',
            'description': 'hail the robots',
        }

        response = requests.put(self.url, data=params, auth=self.creds)
        issue_id = response.headers['location'].split('/')[-1]

        self.assertEquals(response.status_code, 201)
        self.assertIn('API', issue_id)

        r = requests.get(self.url + issue_id, auth=self.creds)
        self.assertEquals(r.status_code, 200)

    def test_create_issue_with_invalid_project(self):
        params = {
            'project': 'INVALID',
            'summary': 'test issue by robot',
            'description': 'hail the robots',
        }

        response = requests.put(self.url, data=params, auth=self.creds)
        self.assertEquals(response.status_code, 403)

