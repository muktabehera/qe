# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43331 - Clients PATCH:

  Verify that user is able to modify child group with parameter 'Remote Address>Matches IP' using request PATCH '/clients/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/clientUpdate"

JSON data sent to PathFinder in this test:

  {'bitrateCapLive': 0,
   'bitrateCapVOD': 0,
   'description': None,
   'matchingRule': {'groups': [{'groups': [],
                                'operator': 'ALL',
                                'rules': [{'contextField': 'remoteAddress',
                                           'contextFieldKey': None,
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': '10.10.10.10/32',
                                           'operator': 'IPMATCH'}]}],
                    'operator': 'ALL',
                    'rules': []},
   'name': 'PATCH: Client updated with Group Rule Remote Address IP1',
   'sourceSelectionRule': []}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43331')
    @pytest.mark.Clients
    @pytest.mark.PATCH
    def test_TC_43331_PATCH_Clients_Client_Group_Remote_Address_Ip(self, context):
        """TC-43331 - Clients-PATCH
           Verify that user is able to modify child group with parameter 'Remote Address>Matches IP' using request PATCH '/clients/'."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to modify child group with parameter 'Remote Address>Matches IP' using request PATCH '/clients/'."""):


            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'remoteAddress',
                            'operator': 'IPMATCH',
                            'contextFieldType': 'String',
                            'matchValue': '10.10.10.10/32',
                            'contextFieldKey': None
                        }],
                        'groups': []
                    }]
                },
                name='PATCH: Client updated with Group Rule Remote Address IP1',
                sourceSelectionRule=[])


            # updateEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.updateEntity(
                    body=clientDetails, 
                    id='clientUpdate'
                
                )
            )

        # Define a test step
        with pytest.allure.step("""Test2: Verify that user is able to modify child group with parameter 'Remote Address>Matches IP' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [],
                    'groups': [{
                        'operator':
                            'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'remoteHost',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': '10.10.10.10',
                            'contextFieldKey': None
                        }],
                        'groups': []
                    }]
                },
                name='PATCH: Client updated with Group Rule Remote Host EQ Rule1',
                sourceSelectionRule=[])

            # updateEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.updateEntity(
                    body=clientDetails,
                    id='clientUpdate'

                )
            )

