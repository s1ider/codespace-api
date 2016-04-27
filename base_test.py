import unittest
import xmltodict
from yaml import load


class BaseAPITest(unittest.TestCase):

    def setUp(self):
        self.settings = load(open('settings.yaml').read())
        self.url = self.settings['url']
        self.creds = tuple(self.settings['credentials'].values())
