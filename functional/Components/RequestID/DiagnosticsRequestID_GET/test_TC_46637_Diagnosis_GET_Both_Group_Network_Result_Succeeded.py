# -*- coding: UTF-8 -*-

"""PFE Component Tests - Diagnosis.

* TC-46637 - Diagnosis GET:

  Verify that network Locations result is displayed as 'Succeeded' if both the groups result 'Succeeded' using request GET /diagnostices/requestId.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/diagnosis/requestId"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/diagnosis/requestId"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Diagnosis')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Diagnosis test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-46637')
    @pytest.mark.Diagnosis
    @pytest.mark.GET
    def test_TC_46637_GET_Diagnosis_Both_Group_Network_Result_Succeeded(self, context):
        """TC-46637 - Diagnosis-GET
           Verify that network Locations result is displayed as 'Succeeded' if both the groups result 'Succeeded' using request GET /diagnostices/requestId."""
        # Define a test step
        with pytest.allure.step("""Verify that network Locations result is displayed as 'Succeeded' if both the groups result 'Succeeded' using request GET /diagnostices/requestId."""):

            ### Positive test example

            # evaluateNetworkContextGet the Diagnosis.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Diagnosis.evaluateNetworkContextGet()
            )

        with pytest.allure.step("""Verify that network Locations result is displayed as 'Succeeded' if both the groups result 'Succeeded' using request GET /diagnostices/requestId."""):

            ### Negative test example

            # evaluateNetworkContextGet the Diagnosis, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Diagnosis.evaluateNetworkContextGet(),
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('may not be empty'),
                    should.start_with('Invalid page parameter specified'),
                    should.contain('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
