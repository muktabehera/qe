# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44589 - Groups POST:

  Verify that user is able to create group with parameter "dnsName", if  'DNS_Name' value is not provided in 'originLoadBalancePolicy' or 'deliveryLoadBalancePolicy' parameters using request POST '/groups'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [],
   'deliveryLoadBalancePolicy': 'ALL_MEMBERS',
   'dnsName': 'autovccQED',
   'edgeDeviceRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
   'id': 'DNS_NAMENotProvided1',
   'members': [{'id': 'Device_Test_API'}],
   'name': 'DNS Name not provided1',
   'originLoadBalancePolicy': 'ALL_MEMBERS',
   'provisioningPolicy': 'ALL_MEMBERS',
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Groups')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Groups test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44589')
    @pytest.mark.Groups
    @pytest.mark.POST
    def test_TC_44589_POST_Groups_Dns_Name_Not_Provided(self, context):
        """TC-44589 - Groups-POST
           Verify that user is able to create group with parameter "dnsName", if  'DNS_Name' value is not provided in 'originLoadBalancePolicy' or 'deliveryLoadBalancePolicy' parameters using request POST '/groups'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create group with parameter "dnsName", if  'DNS_Name' value is not provided in 'originLoadBalancePolicy' or 'deliveryLoadBalancePolicy' parameters using request POST '/groups'."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='ALL_MEMBERS',
                dnsName='autovccQED',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='DNS_NAMENotProvided1',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='DNS Name not provided1',
                originLoadBalancePolicy='ALL_MEMBERS',
                provisioningPolicy='ALL_MEMBERS',
                proximityDetails=None,
                visibleInAllConfigurations=True)


            # createEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Groups.createEntity(
                    body=edgeDeviceGroupDetails
                )
            )

