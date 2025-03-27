# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from manticoresearch.models.base_model import Model
from manticoresearch import util


class SearchResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, took: int=None, timed_out: bool=None, aggregations: object=None, hits: SearchResponseHits=None, profile: object=None, scroll: str=None, warning: object=None):
        """SearchResponse - a model defined in OpenAPI

        :param took: The took of this SearchResponse.
        :param timed_out: The timed_out of this SearchResponse.
        :param aggregations: The aggregations of this SearchResponse.
        :param hits: The hits of this SearchResponse.
        :param profile: The profile of this SearchResponse.
        :param scroll: The scroll of this SearchResponse.
        :param warning: The warning of this SearchResponse.
        """
        self.openapi_types = {
            'took': int,
            'timed_out': bool,
            'aggregations': object,
            'hits': SearchResponseHits,
            'profile': object,
            'scroll': str,
            'warning': object
        }

        self.attribute_map = {
            'took': 'took',
            'timed_out': 'timed_out',
            'aggregations': 'aggregations',
            'hits': 'hits',
            'profile': 'profile',
            'scroll': 'scroll',
            'warning': 'warning'
        }

        self._took = took
        self._timed_out = timed_out
        self._aggregations = aggregations
        self._hits = hits
        self._profile = profile
        self._scroll = scroll
        self._warning = warning

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SearchResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The searchResponse of this SearchResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def took(self):
        """Gets the took of this SearchResponse.

        Time taken to execute the search

        :return: The took of this SearchResponse.
        :rtype: int
        """
        return self._took

    @took.setter
    def took(self, took):
        """Sets the took of this SearchResponse.

        Time taken to execute the search

        :param took: The took of this SearchResponse.
        :type took: int
        """

        self._took = took

    @property
    def timed_out(self):
        """Gets the timed_out of this SearchResponse.

        Indicates whether the search operation timed out

        :return: The timed_out of this SearchResponse.
        :rtype: bool
        """
        return self._timed_out

    @timed_out.setter
    def timed_out(self, timed_out):
        """Sets the timed_out of this SearchResponse.

        Indicates whether the search operation timed out

        :param timed_out: The timed_out of this SearchResponse.
        :type timed_out: bool
        """

        self._timed_out = timed_out

    @property
    def aggregations(self):
        """Gets the aggregations of this SearchResponse.

        Aggregated search results grouped by the specified criteria

        :return: The aggregations of this SearchResponse.
        :rtype: object
        """
        return self._aggregations

    @aggregations.setter
    def aggregations(self, aggregations):
        """Sets the aggregations of this SearchResponse.

        Aggregated search results grouped by the specified criteria

        :param aggregations: The aggregations of this SearchResponse.
        :type aggregations: object
        """

        self._aggregations = aggregations

    @property
    def hits(self):
        """Gets the hits of this SearchResponse.


        :return: The hits of this SearchResponse.
        :rtype: SearchResponseHits
        """
        return self._hits

    @hits.setter
    def hits(self, hits):
        """Sets the hits of this SearchResponse.


        :param hits: The hits of this SearchResponse.
        :type hits: SearchResponseHits
        """

        self._hits = hits

    @property
    def profile(self):
        """Gets the profile of this SearchResponse.

        Profile information about the search execution, if profiling is enabled

        :return: The profile of this SearchResponse.
        :rtype: object
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this SearchResponse.

        Profile information about the search execution, if profiling is enabled

        :param profile: The profile of this SearchResponse.
        :type profile: object
        """

        self._profile = profile

    @property
    def scroll(self):
        """Gets the scroll of this SearchResponse.

        Scroll token to be used fo pagination

        :return: The scroll of this SearchResponse.
        :rtype: str
        """
        return self._scroll

    @scroll.setter
    def scroll(self, scroll):
        """Sets the scroll of this SearchResponse.

        Scroll token to be used fo pagination

        :param scroll: The scroll of this SearchResponse.
        :type scroll: str
        """

        self._scroll = scroll

    @property
    def warning(self):
        """Gets the warning of this SearchResponse.

        Warnings encountered during the search operation

        :return: The warning of this SearchResponse.
        :rtype: object
        """
        return self._warning

    @warning.setter
    def warning(self, warning):
        """Sets the warning of this SearchResponse.

        Warnings encountered during the search operation

        :param warning: The warning of this SearchResponse.
        :type warning: object
        """

        self._warning = warning
