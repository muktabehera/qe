# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44100 - Routes GET:

  Verify that user is able to GET the details of route devices with "page", "sort","routeid" and "prefix" parameter using request "/routes/possibleMembers".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/possibleMembers?prefix=a
       &name;asc &routeId=Alpha1_test_Route"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/possibleMembers?prefix=a
       &name;asc &routeId=Alpha1_test_Route"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44100')
    @pytest.mark.Routes
    @pytest.mark.GET
    def test_TC_44100_GET_Routes_Details_With_Route_Page_Sort_Prefix(self, context):
        """TC-44100 - Routes-GET
           Verify that user is able to GET the details of route devices with "page", "sort","routeid" and "prefix" parameter using request "/routes/possibleMembers"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of route devices with "page", "sort","routeid" and "prefix" parameter using request "/routes/possibleMembers"."""):

            # possibleMembers the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Routes.possibleMembers(
                    prefix='g',
                    routeId='route21',
                    page='0;10',
                    sort='name;asc'
                )
            )
