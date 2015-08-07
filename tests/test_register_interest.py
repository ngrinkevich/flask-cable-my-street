#! ../env/bin/python
# -*- coding: utf-8 -*-

import pytest

create_user = True


@pytest.mark.usefixtures("testapp")
class TestRegisterInterest:
    def test_register_interest(self, testapp):
        """ Tests if the register interest form functions """

        rv = testapp.post('/registerCustomer', data=dict(
            customerType = 'residential',
            title = 'Mrs',
            firstName = 'First Name',
            lastName = 'Last Name',
            email = 'email@email.com',
            buildingNumber = 'Building Number',
            street = 'Street',
            postcode = 'Postcode',
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert 'This field is required.' not in str(rv.data)

    def test_register_interest_fail(self, testapp):
        """ Tests if the register interest form fails correctly """

        rv = testapp.post('/registerCustomer', data=dict(
            customerType = 'residential',
            title = '',
            firstName = '',
            lastName = '',
            email = '',
            buildingNumber = '',
            street = '',
            postcode = '',
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert 'This field is required.' in str(rv.data)
