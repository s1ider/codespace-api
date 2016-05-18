import requests
from base_test import BaseTestApi

class TestGetIssues(BaseTestApi):

    def setUp(self):
        super(TestGetIssues, self).setUp()
        self.url = self.base_url + '/issue'

    def test_get_issues(self):
        params = {
            'filter': 'me #Unresolved #Closed'
        }
        r = requests.get(self.url, params, cookies=self.cookies)

        self.assertEquals(r.status_code, 200)