from base_test import BaseTestApi
import requests
import xmltodict


class TestUpdateIssue(BaseTestApi):

    def setUp(self):
        super(TestUpdateIssue, self).setUp()
        self.url = self.base_url + '/issue/'

        self.updateData = {
            'summary': 'updated_test_summary',
            'description': 'updated_test_description'
        }

    def test_update_issue(self):
        issue_id = self.create_issue()
        url = self.url + issue_id

        r = requests.post(url, self.updateData, cookies=self.cookies)

        self.assertEquals(r.status_code, 200)

        response = requests.get(url, cookies=self.cookies)
        response_dict = xmltodict.parse(response.text)

        self.assertEquals(response_dict['issue']['field'][2]['value'], self.updateData['summary'])
        self.assertEquals(response_dict['issue']['field'][3]['value'], self.updateData['description'])

        #remove created issue after all checks
        self.delete_issue(issue_id)

    def test_update_nonexisting_issue(self):
        url = self.base_url + 'ZZZ'

        r = requests.post(url, self.updateData, cookies=self.cookies)

        self.assertEquals(r.status_code, 404)