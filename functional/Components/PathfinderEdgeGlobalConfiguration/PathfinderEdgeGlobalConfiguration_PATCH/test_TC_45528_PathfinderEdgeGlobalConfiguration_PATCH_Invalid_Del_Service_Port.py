# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Global_Configuration.

* TC-45528 - Pathfinder_Edge_Global_Configuration PATCH:

  Verify that validation message is displayed while providing invalid value for field deliveryServicePort for VideoEdge Global configuration using request PATCH /devices/veGlobalConfig .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veGlobalConfig"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veGlobalConfig"

JSON data sent to PathFinder in this test:

  {
    "deliveryServiceHost": "172.30.4.204",
    "deliveryServiceProtocol": "http",
    "deliveryServicePort": invalid,
    "configRequestFrequency": 700
  }

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-45528')
    @pytest.mark.Pathfinder_Edge_Global_Configuration
    @pytest.mark.PATCH
    def test_TC_45528_PATCH_Pathfinder_Edge_Global_Configuration_Invalid_Del_Service_Port(self, context):
        """TC-45528 - Pathfinder_Edge_Global_Configuration-PATCH
           Verify that validation message is displayed while providing invalid value for field deliveryServicePort for VideoEdge Global configuration using request PATCH /devices/veGlobalConfig ."""
        # Define a test step
        with pytest.allure.step("""Verify that validation message is displayed while providing invalid value for field deliveryServicePort for VideoEdge Global configuration using request PATCH /devices/veGlobalConfig ."""):

            ### Positive test example

            # Test case configuration
            videoEdgeGlobalConfigDetails = context.sc.UNKNOWN

                        ### =!!==>> Could not parse test data.
                        ###         Please fix the following manually:

            unknownJSON= """{
              "deliveryServiceHost": "172.30.4.204",
              "deliveryServiceProtocol": "http",
              "deliveryServicePort": invalid,
              "configRequestFrequency": 700
            }"""
            

            # updateEntity the Pathfinder_Edge_Global_Configuration.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Pathfinder_Edge_Global_Configuration.updateEntity(
                    body=videoEdgeGlobalConfigDetails
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that validation message is displayed while providing invalid value for field deliveryServicePort for VideoEdge Global configuration using request PATCH /devices/veGlobalConfig ."""):

            ### Negative test example

            # Test case configuration
            videoEdgeGlobalConfigDetails = context.sc.UNKNOWN

                        ### =!!==>> Could not parse test data.
                        ###         Please fix the following manually:

            unknownJSON= """{
              "deliveryServiceHost": "172.30.4.204",
              "deliveryServiceProtocol": "http",
              "deliveryServicePort": invalid,
              "configRequestFrequency": 700
            }"""
            

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
