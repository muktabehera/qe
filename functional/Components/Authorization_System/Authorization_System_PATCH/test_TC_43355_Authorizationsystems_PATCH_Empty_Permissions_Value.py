# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-43355 - Authorization_Systems PATCH:

   Verify that validation message is displayed while removing mandatory field (Permissions)  Authorization System using request PATCH authorizationSystems/{id}  ".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems/PATCH_authorizationSystem_testdata"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [],
   'creationDate': '2016-04-21T07:00:16Z',
   'grantablePermissions': [],
   'modificationDate': '2016-04-21T07:00:16Z',
   'name': 'PATCH_authorizationSystem_emptyPermissionsValue',
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Authorization_Systems')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Authorization_Systems test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43355')
    @pytest.mark.Authorization_Systems
    @pytest.mark.PATCH
    def test_TC_43355_PATCH_Authorization_Systems_Empty_Permissions_Value(self, context):
        """TC-43355 - Authorization_Systems-PATCH
            Verify that validation message is displayed while removing mandatory field (Permissions)  Authorization System using request PATCH authorizationSystems/{id}  "."""
        # Define a test step

        with pytest.allure.step(""" Verify that validation message is displayed while removing mandatory field (Permissions)  Authorization System using request PATCH authorizationSystems/{id}  "."""):

            # Test case configuration
            authorizationSystemDetails = context.sc.AuthorizationSystemDetails(
                configAdminCanEdit=True,
                configurations=[],
                grantablePermissions=[],
                id=None,
                macKey=None,
                name='PATCH_authorizationSystem_emptyPermissionsValue',
                visibleInAllConfigurations=True)


            # prepare the request, so we can modify it
            request = context.cl.Authorization_Systems.updateEntity(
                    body=authorizationSystemDetails, 
                    id='PATCH_authorizationSystem_testdata'
                
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Authorization_Systems, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('size must be between 1 and 2147483647')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
