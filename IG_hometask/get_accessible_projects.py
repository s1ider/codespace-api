from base_test import BaseTestApi
import requests

class TestAccessibleProjects(BaseTestApi):

    def setUp(self):
        super(TestAccessibleProjects, self).setUp()
        self.url = self.base_url + '/project/all'

    def test_get_accessible_projects(self):
        r = requests.get(self.url, cookies=self.cookies)

        self.assertEquals(r.status_code, 200)