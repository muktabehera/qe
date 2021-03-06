# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43794 - Proximity_Zones GET:

  Verify that user is unable to GET the details of  proximities using request /proximities/{id} with invalid token.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer
       <data_ID1_under_test>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/a"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer
       eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkZWZhdWx0Iiwic3ViIjoiYWRtaW5AMTcyLjMwLjIuMTQ5OjgwODAuY29tIiwiYXVkIjoicWVkOmRlZmF1bHQiLCJxZWRwIjpbInMiLCJjIiwiZyIsInAiLCJkIiwibSIsImEiXX0.uh1W0Hs2nemsjiRFRSiyiZgo4io5bUmmCSJqrjfjfehff"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/a"

"""

import pytest

from qe_common import *

logger = init_logger()







@pytest.mark.components
@pytest.allure.story('Proximity_Zones')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Proximity_Zones test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43794')
    @pytest.mark.Proximity_Zones
    @pytest.mark.GET
    def test_TC_43794_GET_Proximity_Zones_Unable_To_Get_Proximity_Details_With_Invalid_Token(self, context):
        """TC-43794 - Proximity_Zones-GET
           Verify that user is unable to GET the details of  proximities using request /proximities/{id} with invalid token."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to GET the details of  proximities using request /proximities/{id} with invalid token."""):


            # listEntities the Proximity_Zones, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Proximity_Zones.getEntity(id='ProximityPost1'),
                    token='invalid_token',
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
