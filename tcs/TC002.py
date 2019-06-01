#!/usr/bin/env
# coding = utf-8
import requests
import unittest
import configparser

class SelectXmind(unittest.TestCase):
    def setUp(self):
        conf = configparser.ConfigParser()
        conf.read('conf.ini')
        host = conf.get('conf', 'host')
        self.url = host + ':8001'

    def tearDown(self):
        pass

    def test_select(self):
        res = requests.get(self.url)
        statusCode = res.status_code
        self.assertEqual(200, statusCode)
