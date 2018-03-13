# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Global_Configuration.

* TC-42590 - Pathfinder_Edge_Global_Configuration PATCH:

  Verify that user is unable to modify(PATCH) the VideoEdge Global configuration using request /devices/veGlobalConfig  with invalid token.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer
       123aswdasfdqw3e432dadasdadasdqwq3eqwed" -X PATCH -d
       @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veGlobalConfig"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer
       123aswdasfdqw3e432dadasdadasdqwq3eqwed" -X PATCH -d
       @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veGlobalConfig"

JSON data sent to PathFinder in this test:

  {'configRequestFrequency': 700,
   'deliveryServiceHost': '172.30.2.149',
   'deliveryServicePort': 8080,
   'deliveryServiceProtocol': 'http',
   'id': '1'}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Pathfinder_Edge_Global_Configuration')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Pathfinder_Edge_Global_Configuration test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42590')
    @pytest.mark.Pathfinder_Edge_Global_Configuration
    @pytest.mark.PATCH
    def test_TC_42590_PATCH_Pathfinder_Edge_Global_Configuration_Invalid_Token(self, context):
        """TC-42590 - Pathfinder_Edge_Global_Configuration-PATCH
           Verify that user is unable to modify(PATCH) the VideoEdge Global configuration using request /devices/veGlobalConfig  with invalid token."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to modify(PATCH) the VideoEdge Global configuration using request /devices/veGlobalConfig  with invalid token."""):

            ### Positive test example

            # Test case configuration
            videoEdgeGlobalConfigDetails = context.sc.VideoEdgeGlobalConfigDetails(
                configRequestFrequency=700,
                deliveryServiceHost='172.30.2.149',
                deliveryServicePort=8080,
                deliveryServiceProtocol='http',
                id='1',
                synthetic=None)


            # updateEntity the Pathfinder_Edge_Global_Configuration.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Pathfinder_Edge_Global_Configuration.updateEntity(
                    body=videoEdgeGlobalConfigDetails
                ),
                token='invalid_token'
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is unable to modify(PATCH) the VideoEdge Global configuration using request /devices/veGlobalConfig  with invalid token."""):

            ### Negative test example

            # Test case configuration
            videoEdgeGlobalConfigDetails = context.sc.VideoEdgeGlobalConfigDetails(
                configRequestFrequency=700,
                deliveryServiceHost='172.30.2.149',
                deliveryServicePort=8080,
                deliveryServiceProtocol='http',
                id='1',
                synthetic=None)


            # prepare the request, so we can modify it
            request = context.cl.Pathfinder_Edge_Global_Configuration.updateEntity(
                    body=videoEdgeGlobalConfigDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Pathfinder_Edge_Global_Configuration, and check we got the error we expect
            try:
                client, response = check(
                    request,
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