import unittest
import requests
import xmltodict
from yaml import load
from base_test import BaseAPITest


class TestGetIssue(BaseAPITest):


    def test_get_issue_sunny(self):
        url = self.url + '/issue/' + 'API-1'

        response = requests.get(url, auth=self.creds)
        response_dict = xmltodict.parse(response.text)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response_dict['issue']['@id'], 'API-1')

    def test_get_issue_invalid_id(self):
        url = self.url + '/issue/' + 'ZZZ'

        response = requests.get(url, auth=self.creds)
        response_dict = xmltodict.parse(response.text)

        self.assertEquals(response.status_code, 404, response.text)
        self.assertEquals(response_dict['error'], 'Issue not found.')


if __name__ == '__main__':
    unittest.main()
