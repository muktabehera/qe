# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-44765 - Audiences POST:

  Verify that user is able to send simple streaming media file(wmv,flv,mp3,wma,mp4) for distribution using request POST "/distributions" with multiple Audience(Standalone and Videonet).


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences"

JSON data sent to PathFinder in this test:

  {'clients': [{'id': 'broadcastClient'}],
   'deliverySystems': [{'id': 'Broadcast_Route_DS'}],
   'id': 'Broadcast_Videonet_Audience',
   'name': 'Broadcast_Videonet_Audience',
   'networkLocations': [{'id': 'broadcastNetworkLocation'}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Audiences')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Audiences test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44765')
    @pytest.mark.Audiences
    @pytest.mark.POST
    def test_TC_44765_POST_Audiences_Distributions_Multiple_Audience_Simple_Media_Mp4(self, context):
        """TC-44765 - Audiences-POST
           Verify that user is able to send simple streaming media file(wmv,flv,mp3,wma,mp4) for distribution using request POST "/distributions" with multiple Audience(Standalone and Videonet)."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to send simple streaming media file(wmv,flv,mp3,wma,mp4) for distribution using request POST "/distributions" with multiple Audience(Standalone and Videonet)."""):

            ### Positive test example

            # Test case configuration
            audienceDetails = context.sc.AudienceDetails(
                clients=[{
                    'id': 'broadcastClient'
                }],
                configurationId=None,
                deliverySystems=[{
                    'id': 'Broadcast_Route_DS'
                }],
                estimatedTimeForMulticastStreamsToBeAvailable=None,
                id='Broadcast_Videonet_Audience',
                name='Broadcast_Videonet_Audience',
                networkLocations=[{
                    'id': 'broadcastNetworkLocation'
                }])


            # createEntity the Audiences.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Audiences.createEntity(
                    body=audienceDetails
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is able to send simple streaming media file(wmv,flv,mp3,wma,mp4) for distribution using request POST "/distributions" with multiple Audience(Standalone and Videonet)."""):

            ### Negative test example

            # Test case configuration
            audienceDetails = context.sc.AudienceDetails(
                clients=[{
                    'id': 'broadcastClient'
                }],
                configurationId=None,
                deliverySystems=[{
                    'id': 'Broadcast_Route_DS'
                }],
                estimatedTimeForMulticastStreamsToBeAvailable=None,
                id='Broadcast_Videonet_Audience',
                name='Broadcast_Videonet_Audience',
                networkLocations=[{
                    'id': 'broadcastNetworkLocation'
                }])


            # prepare the request, so we can modify it
            request = context.cl.Audiences.createEntity(
                    body=audienceDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # createEntity the Audiences, and check we got the error we expect
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
