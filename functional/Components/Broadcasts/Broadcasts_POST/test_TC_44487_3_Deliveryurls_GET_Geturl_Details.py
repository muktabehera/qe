# -*- coding: UTF-8 -*-

"""PFE Component Tests - Delivery_Urls.

* TC-44487 - Delivery_Urls GET:

  Verify that user is able to create and play HLS stream with VideoNet(origin-Edge) in live program using request POST "/broadcasts".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/deliveryUrls?sourceUrl=qedbroadcast://<data_ID5_under_test>
       &possibleAudiences=<data_ID4_under_test> &contentType=UNSPECIFIED"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/deliveryUrls?sourceUrl=qedbroadcast://Broadcast_VidoenetVNE_HLS
       &possibleAudiences=Broadcast_Videonet_Audience
       &contentType=UNSPECIFIED"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Delivery_Urls')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Delivery_Urls test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44487')
    @pytest.mark.Delivery_Urls
    @pytest.mark.GET
    def test_TC_44487_GET_Delivery_Urls_Geturl_Details(self, context):
        """TC-44487 - Delivery_Urls-GET
           Verify that user is able to create and play HLS stream with VideoNet(origin-Edge) in live program using request POST "/broadcasts"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create and play HLS stream with VideoNet(origin-Edge) in live program using request POST "/broadcasts"."""):

            ### Positive test example

            # deliveryUrlsGet the Delivery_Urls.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Delivery_Urls.deliveryUrlsGet(
                    sourceUrl='qedbroadcast://Broadcast_VidoenetVNE_HLS', 
                    possibleAudiences='Broadcast_Videonet_Audience', 
                    contentType='UNSPECIFIED'
                )
            )

        with pytest.allure.step("""Verify that user is able to create and play HLS stream with VideoNet(origin-Edge) in live program using request POST "/broadcasts"."""):

            ### Negative test example

            # deliveryUrlsGet the Delivery_Urls, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Delivery_Urls.deliveryUrlsGet(
                        sourceUrl='qedbroadcast://Broadcast_VidoenetVNE_HLS', 
                        possibleAudiences='Broadcast_Videonet_Audience', 
                        contentType='UNSPECIFIED'
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
