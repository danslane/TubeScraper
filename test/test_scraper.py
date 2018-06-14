"""
Tests for `scraper` module.
"""

import pytest
from tube_scraper.scraper import quick_add


class TestScraper(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_something(self):
        assert quick_add(5, 6) == 11
        pass

    @classmethod
    def teardown_class(cls):
        pass
