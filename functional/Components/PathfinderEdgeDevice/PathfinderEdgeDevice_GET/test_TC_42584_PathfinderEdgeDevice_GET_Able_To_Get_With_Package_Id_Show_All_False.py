# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Device.

* TC-42584 - Pathfinder_Edge_Device GET:

  Verify that user is able to GET the details of VideoEdge device profiles request  /devices/veDevices  with packageid & showall=false parameters.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veDevices?packageId=a6be07f6-d468-4d38-9315-3a71cb90f93d
       &showAll=false"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veDevices?packageId=a6be07f6-d468-4d38-9315-3a71cb90f93d
       &showAll=false"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Pathfinder_Edge_Device')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Pathfinder_Edge_Device test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42584')
    @pytest.mark.Pathfinder_Edge_Device
    @pytest.mark.GET
    def test_TC_42584_GET_Pathfinder_Edge_Device_Able_To_Get_With_Package_Id_Show_All_False(self, context):
        """TC-42584 - Pathfinder_Edge_Device-GET
           Verify that user is able to GET the details of VideoEdge device profiles request  /devices/veDevices  with packageid & showall=false parameters."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of VideoEdge device profiles request  /devices/veDevices  with packageid & showall=false parameters."""):

            ### Positive test example

            # listEntities the Pathfinder_Edge_Device.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Pathfinder_Edge_Device.listEntities(
                    packageId='a6be07f6-d468-4d38-9315-3a71cb90f93d', 
                    showAll='false'
                )
            )

        with pytest.allure.step("""Verify that user is able to GET the details of VideoEdge device profiles request  /devices/veDevices  with packageid & showall=false parameters."""):

            ### Negative test example

            # listEntities the Pathfinder_Edge_Device, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Pathfinder_Edge_Device.listEntities(
                        packageId='a6be07f6-d468-4d38-9315-3a71cb90f93d', 
                        showAll='false'
                    ),
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
