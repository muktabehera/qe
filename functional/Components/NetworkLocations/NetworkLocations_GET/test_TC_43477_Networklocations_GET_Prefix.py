# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-43477 - Network_Locations GET:

  Verify that user is able to GET the details of network location using request GET /networkLocations with parameter prefix.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations?prefix=network"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations?prefix=network"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Network_Locations')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Network_Locations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43477')
    @pytest.mark.Network_Locations
    @pytest.mark.GET
    def test_TC_43477_GET_Network_Locations_Prefix(self, context):
        """TC-43477 - Network_Locations-GET
           Verify that user is able to GET the details of network location using request GET /networkLocations with parameter prefix."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of network location using request GET /networkLocations with parameter prefix."""):

            # listEntities the Network_Locations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Network_Locations.listEntities(
                    prefix='network')
            )

