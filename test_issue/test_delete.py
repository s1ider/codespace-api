from base_test import BaseAPITest
import requests


class TestDelete(BaseAPITest):

    def test_delete_user(self):
        issue_id = self.create_issue()

        url = self.url + '/issue/' + issue_id
        r = requests.delete(url, auth=self.creds)

        self.assertEquals(r.status_code, 200)

        r = requests.get(url, auth=self.creds)
        self.assertEquals(r.status_code, 404)

    def test_delete_nonexisted_user(self):
        url = self.url + '/issue/' + 'ZZZ'
        r = requests.delete(url, auth=self.creds)
        self.assertEquals(r.status_code, 404)

    def test_count(self):
        url = self.url + '/issue/count'


