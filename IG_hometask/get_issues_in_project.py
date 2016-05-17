from base_test import BaseTestApi
import requests


class TestGetIssuesInProject(BaseTestApi):

    def setUp(self):
        super(TestGetIssuesInProject, self).setUp()
        self.url = self.base_url + '/issue/byproject/'

    def test_get_issues_in_project(self):
        url = self.url + 'API'
        r = requests.get(url, cookies=self.cookies)

        self.assertEquals(r.status_code, 200)

    def test_get_issues_in_nonexisting_project(self):
        url = self.url + 'ZZZ'

        r = requests.get(url, cookies=self.cookies)

        self.assertEquals(r.status_code, 404)
