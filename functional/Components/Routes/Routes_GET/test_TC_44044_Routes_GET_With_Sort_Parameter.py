# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44044 - Routes GET:

  Verify that user is able to GET the details of routes with "sort" parameter using request "routes".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes?sort=name;asc &showAll=false"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes?sort=name;asc &showAll=false"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44044')
    @pytest.mark.Routes
    @pytest.mark.GET
    def test_TC_44044_GET_Routes_With_Sort_Parameter(self, context):
        """TC-44044 - Routes-GET
           Verify that user is able to GET the details of routes with "sort" parameter using request "routes"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of routes with "sort" parameter using request "routes"."""):

            # createHop the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Routes.listAllRoutes(
                    sort='name;asc', 
                    showAll='false'
                )
            )
