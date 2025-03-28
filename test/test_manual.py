
# coding: utf-8
# Manticore Search Client
# Copyright (c) 2020-2021, Manticore Software LTD (https://manticoresearch.com)
#
# All rights reserved

from __future__ import absolute_import
from pprint import pprint
import unittest
import json
import manticoresearch
from manticoresearch.api.index_api import IndexApi  # noqa: E501
from manticoresearch.models import *
from manticoresearch.rest import ApiException
from unittest import IsolatedAsyncioTestCase
from urllib.parse import quote
import sys

class TestManualApi(IsolatedAsyncioTestCase):

    def setUp(self):
        self.configuration = manticoresearch.Configuration(
            host = "http://localhost:9408"
        )
        
    def tearDown(self):
        pass
        
    async def test_manual(self):
		async with manticoresearch.ApiClient(self.configuration) as client:
			pprint("Tests finished")
        
if __name__ == '__main__':
    unittest.main()
