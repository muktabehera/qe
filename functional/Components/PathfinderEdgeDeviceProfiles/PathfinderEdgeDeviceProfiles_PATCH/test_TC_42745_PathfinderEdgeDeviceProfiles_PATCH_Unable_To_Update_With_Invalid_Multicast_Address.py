# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Device_Profiles.

* TC-42745 - Pathfinder_Edge_Device_Profiles PATCH:

  Verify that VideoEdge device profile is not getting updated with invalid (mulitcastaddress)  using PATCH/devices/veProfiles  .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veProfiles/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veProfiles/PATCH_Proxy_profile"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [],
   'description': '',
   'enablePrepositioning': True,
   'enableTokenAuthentication': False,
   'httpService': {'httpPort': 80,
                   'httpsPort': 443,
                   'protocol': 'http',
                   'serviceActive': True,
                   'vodPublishingPoints': [{'guid': '4322b86e-2e32-4134-90da-b8f1d1a0c4e3',
                                            'name': 'testUpdate2',
                                            'originId': '12Client'},
                                           {'guid': '81aa7dbf-8a85-430f-922a-9926b7f63615',
                                            'name': 'testUpdate1',
                                            'originId': '123456'}]},
   'manifestRequestFrequency': 60,
   'maximumDownloadTime': 54000,
   'name': 'PATCH_Proxy_profile',
   'nonRestrictedPeriodDownloadBandwidth': 500,
   'proxyMode': 'NO_PROXY',
   'restrictedBandwidthEnd': 17,
   'restrictedBandwidthStart': 8,
   'restrictedPeriodDownloadBandwidth': 100,
   'rtspService': {'multicastAddress': '192.16.17.1934',
                   'multicastEnabled': True,
                   'multicastTtl': 5,
                   'rtspStreamingPort': 554,
                   'serviceActive': True,
                   'unicastFailoverEnabled': True},
   'tokenExpirationTime': 180,
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Pathfinder_Edge_Device_Profiles')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Pathfinder_Edge_Device_Profiles test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42745')
    @pytest.mark.Pathfinder_Edge_Device_Profiles
    @pytest.mark.PATCH
    def test_TC_42745_PATCH_Pathfinder_Edge_Device_Profiles_Unable_To_Update_With_Invalid_Multicast_Address(self, context):
        """TC-42745 - Pathfinder_Edge_Device_Profiles-PATCH
           Verify that VideoEdge device profile is not getting updated with invalid (mulitcastaddress)  using PATCH/devices/veProfiles  ."""
        # Define a test step
        with pytest.allure.step("""Verify that VideoEdge device profile is not getting updated with invalid (mulitcastaddress)  using PATCH/devices/veProfiles  ."""):

            ### Positive test example

            # Test case configuration
            videoEdgeDevicePropertyDetails = context.sc.VideoEdgeDevicePropertyDetails(
                configAdminCanEdit=True,
                configurations=[],
                enablePrepositioning=True,
                enableTokenAuthentication=False,
                httpService={
                    'serviceActive':
                    True,
                    'protocol':
                    'http',
                    'httpPort':
                    80,
                    'httpsPort':
                    443,
                    'vodPublishingPoints': [{
                        'guid':
                        '4322b86e-2e32-4134-90da-b8f1d1a0c4e3',
                        'originId':
                        '12Client',
                        'name':
                        'testUpdate2'
                    }, {
                        'guid':
                        '81aa7dbf-8a85-430f-922a-9926b7f63615',
                        'originId':
                        '123456',
                        'name':
                        'testUpdate1'
                    }]
                },
                id=None,
                manifestRequestFrequency=60,
                maximumDownloadTime=54000,
                name='PATCH_Proxy_profile',
                nonRestrictedPeriodDownloadBandwidth=500,
                proxyMode='NO_PROXY',
                restrictedBandwidthEnd=17,
                restrictedBandwidthStart=8,
                restrictedPeriodDownloadBandwidth=100,
                rtspService={
                    'serviceActive': True,
                    'rtspStreamingPort': 554,
                    'multicastEnabled': True,
                    'multicastAddress': '192.16.17.1934',
                    'multicastTtl': 5,
                    'unicastFailoverEnabled': True
                },
                tokenExpirationTime=180,
                visibleInAllConfigurations=True)


            # updateEntity the Pathfinder_Edge_Device_Profiles.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Pathfinder_Edge_Device_Profiles.updateEntity(
                    body=videoEdgeDevicePropertyDetails, 
                    id='PATCH_Proxy_profile'
                
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that VideoEdge device profile is not getting updated with invalid (mulitcastaddress)  using PATCH/devices/veProfiles  ."""):

            ### Negative test example

            # Test case configuration
            videoEdgeDevicePropertyDetails = context.sc.VideoEdgeDevicePropertyDetails(
                configAdminCanEdit=True,
                configurations=[],
                enablePrepositioning=True,
                enableTokenAuthentication=False,
                httpService={
                    'serviceActive':
                    True,
                    'protocol':
                    'http',
                    'httpPort':
                    80,
                    'httpsPort':
                    443,
                    'vodPublishingPoints': [{
                        'guid':
                        '4322b86e-2e32-4134-90da-b8f1d1a0c4e3',
                        'originId':
                        '12Client',
                        'name':
                        'testUpdate2'
                    }, {
                        'guid':
                        '81aa7dbf-8a85-430f-922a-9926b7f63615',
                        'originId':
                        '123456',
                        'name':
                        'testUpdate1'
                    }]
                },
                id=None,
                manifestRequestFrequency=60,
                maximumDownloadTime=54000,
                name='PATCH_Proxy_profile',
                nonRestrictedPeriodDownloadBandwidth=500,
                proxyMode='NO_PROXY',
                restrictedBandwidthEnd=17,
                restrictedBandwidthStart=8,
                restrictedPeriodDownloadBandwidth=100,
                rtspService={
                    'serviceActive': True,
                    'rtspStreamingPort': 554,
                    'multicastEnabled': True,
                    'multicastAddress': '192.16.17.1934',
                    'multicastTtl': 5,
                    'unicastFailoverEnabled': True
                },
                tokenExpirationTime=180,
                visibleInAllConfigurations=True)


            # prepare the request, so we can modify it
            request = context.cl.Pathfinder_Edge_Device_Profiles.updateEntity(
                    body=videoEdgeDevicePropertyDetails, 
                    id='PATCH_Proxy_profile'
                
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Pathfinder_Edge_Device_Profiles, and check we got the error we expect
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
