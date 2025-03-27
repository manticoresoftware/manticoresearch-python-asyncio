# coding: utf-8

"""
    Manticore Search Client

    Сlient for Manticore Search. 

    The version of the OpenAPI document: 5.0.0
    Contact: info@manticoresearch.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from manticoresearch.models.update_document_request import UpdateDocumentRequest

class TestUpdateDocumentRequest(unittest.TestCase):
    """UpdateDocumentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateDocumentRequest:
        """Test UpdateDocumentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateDocumentRequest`
        """
        model = UpdateDocumentRequest()
        if include_optional:
            return UpdateDocumentRequest(
                table = '',
                cluster = '',
                doc = {gid=10},
                id = 56,
                query = None
            )
        else:
            return UpdateDocumentRequest(
                table = '',
                doc = {gid=10},
        )
        """

    def testUpdateDocumentRequest(self):
        """Test UpdateDocumentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
