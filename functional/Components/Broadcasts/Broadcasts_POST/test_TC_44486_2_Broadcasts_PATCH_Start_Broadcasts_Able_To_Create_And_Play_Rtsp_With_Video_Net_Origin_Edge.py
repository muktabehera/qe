# -*- coding: UTF-8 -*-

"""PFE Component Tests - Broadcasts.

* TC-44486 - Broadcasts PATCH:

  Verify that user is able to create and play RTSP stream with VideoNet(origin-Edge) in live program using request POST "/broadcasts".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/broadcasts/<data_ID3_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/broadcasts/Broadcast_Videonet"

JSON data sent to PathFinder in this test:

  {'status': 'ACTIVE'}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Broadcasts')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Broadcasts test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44486')
    @pytest.mark.Broadcasts
    @pytest.mark.PATCH
    def test_TC_44486_PATCH_Broadcasts_Start_Broadcasts_Able_To_Create_And_Play_Rtsp_With_Video_Net_Origin_Edge(self, context):
        """TC-44486 - Broadcasts-PATCH
           Verify that user is able to create and play RTSP stream with VideoNet(origin-Edge) in live program using request POST "/broadcasts"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create and play RTSP stream with VideoNet(origin-Edge) in live program using request POST "/broadcasts"."""):

            ### Positive test example

            # Test case configuration
            broadcastStatusUpdate = context.sc.BroadcastStatusUpdate(status='ACTIVE')


            # updateEntity the Broadcasts.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Broadcasts.updateEntity(
                    body=broadcastStatusUpdate, 
                    id='Broadcast_Videonet'
                
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is able to create and play RTSP stream with VideoNet(origin-Edge) in live program using request POST "/broadcasts"."""):

            ### Negative test example

            # Test case configuration
            broadcastStatusUpdate = context.sc.BroadcastStatusUpdate(status='ACTIVE')


            # prepare the request, so we can modify it
            request = context.cl.Broadcasts.updateEntity(
                    body=broadcastStatusUpdate, 
                    id='Broadcast_Videonet'
                
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Broadcasts, and check we got the error we expect
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
