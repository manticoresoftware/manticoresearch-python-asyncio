# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from manticoresearch.models.base_model import Model
from manticoresearch import util


class SqlObjResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, hits: object=None):
        """SqlObjResponse - a model defined in OpenAPI

        :param hits: The hits of this SqlObjResponse.
        """
        self.openapi_types = {
            'hits': object
        }

        self.attribute_map = {
            'hits': 'hits'
        }

        self._hits = hits

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SqlObjResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The sqlObjResponse of this SqlObjResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def hits(self):
        """Gets the hits of this SqlObjResponse.


        :return: The hits of this SqlObjResponse.
        :rtype: object
        """
        return self._hits

    @hits.setter
    def hits(self, hits):
        """Sets the hits of this SqlObjResponse.


        :param hits: The hits of this SqlObjResponse.
        :type hits: object
        """
        if hits is None:
            raise ValueError("Invalid value for `hits`, must not be `None`")

        self._hits = hits
