#! ../env/bin/python
# -*- coding: utf-8 -*-

import pytest


@pytest.mark.usefixtures("testapp")
class TestURLs:
    def test_home(self, testapp):
        """ Tests if the home page loads """

        rv = testapp.get('/')
        assert rv.status_code == 200

    def test_get_cms_response(self, testapp):
        """ Tests if the getCMSResponse page loads """

        rv = testapp.get('/getCMSResponse')
        assert rv.status_code == 200

    def test_register_customer(self, testapp):
        """ Tests if the Register Customer Interest page loads """

        rv = testapp.get('/registerCustomer')
        assert rv.status_code == 200


