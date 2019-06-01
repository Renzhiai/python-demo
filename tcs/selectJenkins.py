#!/usr/bin/env
# coding = utf-8
import requests
import unittest

class SelectJenkins(unittest.TestCase):
    def setUp(self):
        self.url = 'http://129.204.45.182:8080'

    def tearDown(self):
        pass

    def test_select(self):
        res = requests.get(self.url)
        statusCode = res.status_code
        self.assertEqual(200, statusCode)
