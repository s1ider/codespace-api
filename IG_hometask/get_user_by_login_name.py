import requests
from base_test import BaseTestApi
import xmltodict

class TestGetUserByLoginName(BaseTestApi):

    def test_get_user_by_login_name(self):
        url = self.base_url + '/user/' + self.creds[0]
        r = requests.get(url, cookies=self.cookies)
        response_dict = xmltodict.parse(r.text)

        self.assertEquals(r.status_code, 200)
        self.assertEquals(response_dict['user']['@login'], self.creds[0])

    def test_get_user_by_nonexisting_user_name(self):
        url = self.base_url + '/ZZZ'
        r = requests.get(url, cookies=self.cookies)

        self.assertEquals(r.status_code, 404)