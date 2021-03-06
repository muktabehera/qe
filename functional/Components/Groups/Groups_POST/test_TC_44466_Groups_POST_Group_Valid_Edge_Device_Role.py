# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44466 - Groups POST:

  Verify that user is able to create group on providing parameter 'edgeDeviceRoles' as(Origin, Distribution, Edge) using request POST '/groups'.


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
   'dnsName': '',
   'edgeDeviceRoles': ['ORIGIN'],
   'id': 'originId1',
   'members': [{'id': 'Device_Test_API'}],
   'name': 'Group with Origin Role1',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44466')
    @pytest.mark.Groups
    @pytest.mark.POST
    def test_TC_44466_POST_Groups_Group_Valid_Edge_Device_Role(self, context):
        """TC-44466 - Groups-POST
           Verify that user is able to create group on providing parameter 'edgeDeviceRoles' as(Origin, Distribution, Edge) using request POST '/groups'."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to create group on providing parameter 'edgeDeviceRoles' as(Origin, Distribution, Edge) using request POST '/groups'."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='ALL_MEMBERS',
                dnsName='',
                edgeDeviceRoles=['ORIGIN'],
                id='originId1',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Group with Origin Role1',
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

        # Define a test step
        with pytest.allure.step("""Test2: Verify that user is able to create group on providing parameter 'edgeDeviceRoles' as(Origin, Distribution, Edge) using request POST '/groups'."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='ALL_MEMBERS',
                dnsName='',
                edgeDeviceRoles=['EDGE'],
                id='edgeId1',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Group with Edge Role1',
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

        # Define a test step
        with pytest.allure.step("""Test3: Verify that user is able to create group on providing parameter 'edgeDeviceRoles' as(Origin, Distribution, Edge) using request POST '/groups'."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='ALL_MEMBERS',
                dnsName='',
                edgeDeviceRoles=['DISTRIBUTION'],
                id='distributionId1',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Group with distribution Role1',
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
