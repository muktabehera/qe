# -*- coding: UTF-8 -*-

"""PFE Component Tests - Configurations.

* TC-45601 - Configurations PATCH:

  Verify that user is able to Update [configAdminCanCreate= true] for Configuration using request PATCH /configurations/{id} ".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/configurations/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/configurations/POST_PATCH_Configurations"

JSON data sent to PathFinder in this test:

  {'configAdminCanCreate': True,
   'host': 'PATCH_Configurations_configAdminCanCreateIsTrue'}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Configurations')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Configurations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-45601')
    @pytest.mark.Configurations
    @pytest.mark.PATCH
    def test_TC_45601_PATCH_Configurations_Config_Admin_Can_Create_Is_True(self, context):
        """TC-45601 - Configurations-PATCH
           Verify that user is able to Update [configAdminCanCreate= true] for Configuration using request PATCH /configurations/{id} "."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to Update [configAdminCanCreate= true] for Configuration using request PATCH /configurations/{id} "."""):

            ### Positive test example

            # Test case configuration
            configurationDetails = context.sc.ConfigurationDetails(
                configAdminCanCreate=True,
                configurationType=None,
                dsId=None,
                host='PATCH_Configurations_configAdminCanCreateIsTrue',
                id=None,
                reflectorServiceActivationStatus=None)


            # updateEntity the Configurations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Configurations.updateEntity(
                    body=configurationDetails, 
                    id='POST_PATCH_Configurations'
                
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is able to Update [configAdminCanCreate= true] for Configuration using request PATCH /configurations/{id} "."""):

            ### Negative test example

            # Test case configuration
            configurationDetails = context.sc.ConfigurationDetails(
                configAdminCanCreate=True,
                configurationType=None,
                dsId=None,
                host='PATCH_Configurations_configAdminCanCreateIsTrue',
                id=None,
                reflectorServiceActivationStatus=None)


            # prepare the request, so we can modify it
            request = context.cl.Configurations.updateEntity(
                    body=configurationDetails, 
                    id='POST_PATCH_Configurations'
                
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Configurations, and check we got the error we expect
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
