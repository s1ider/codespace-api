from base_test import BaseTestApi
import requests
import xmltodict

class TestInfoForCurrentUser(BaseTestApi):

    def test_get_info_for_current_user(self):
        url = self.base_url + '/user/current'

        r = requests.get(url, cookies=self.cookies)
        response_dict = xmltodict.parse(r.text)

        self.assertEquals(r.status_code, 200)
        self.assertEquals(response_dict['user']['@login'], self.creds[0])