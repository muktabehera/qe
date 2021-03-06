# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43125 - Clients POST:

  Verify that user is able to add source constraint rule with specific rule 'matchingRule'(ALL, ANY, NONE) using request POST '/clients.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

JSON data sent to PathFinder in this test:

  {'id': 'sourceRuleMatchingRuleALL',
   'matchingRule': {'groups': [], 'operator': 'ALL', 'rules': []},
   'name': 'POST: Client with Matching Source Rule ALL',
   'sourceSelectionRule': [{'groups': [],
                            'operator': 'ALL',
                            'rules': [{'contextField': 'mimetype',
                                       'contextFieldKey': None,
                                       'contextFieldType': 'String',
                                       'expressionType': 'Single',
                                       'matchValue': 'application/x-mpegURL',
                                       'operator': 'MIMEMATCH'}]}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43125')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_43125_POST_Clients_Client_Source_Rule_Matching_Rule_All(self, context):
        """TC-43125 - Clients-POST
           Verify that user is able to add source constraint rule with specific rule 'matchingRule'(ALL, ANY, NONE) using request POST '/clients."""
        # Define a test step
        with pytest.allure.step("""ALL: Verify that user is able to add source constraint rule with specific rule 'matchingRule'(ALL) using request POST '/clients."""):


            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='sourceRuleMatchingRuleALL',
                matchingRule={'operator': 'ALL',
                              'rules': [],
                              'groups': []},
                name='POST: Client with Matching Source Rule ALL',
                sourceSelectionRule=[{
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'mimetype',
                        'operator': 'MIMEMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'application/x-mpegURL',
                        'contextFieldKey': None
                    }],
                    'groups': []
                }])


            # createEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.createEntity(
                    body=clientDetails
                )
            )

        # Define a test step
        with pytest.allure.step("""ANY: Verify that user is able to add source constraint rule with specific rule 'matchingRule'(ANY) using request POST '/clients."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='sourceRuleMatchingRuleANY',
                matchingRule={'operator': 'ALL',
                              'rules': [],
                              'groups': []},
                name='POST: Client with Matching sourceRule Rule ANY',
                sourceSelectionRule=[{
                    'operator':
                    'ANY',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'mimetype',
                        'operator': 'MIMEMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'application/x-mpegURL',
                        'contextFieldKey': None
                    }],
                    'groups': []
                }])


            # createEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.createEntity(
                    body=clientDetails
                )
            )

        # Define a test step
        with pytest.allure.step("""Verify that user is able to add source constraint rule with specific rule 'matchingRule'(NONE) using request POST '/clients."""):


            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='sourceRuleMatchingRuleNONE',
                matchingRule={'operator': 'ALL',
                              'rules': [],
                              'groups': []},
                name='POST: Client with Matching sourceRule Rule NONE',
                sourceSelectionRule=[{
                    'operator':
                    'NONE',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'mimetype',
                        'operator': 'MIMEMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'application/x-mpegURL',
                        'contextFieldKey': None
                    }],
                    'groups': []
                }])


            # createEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.createEntity(
                    body=clientDetails
                )
            )
