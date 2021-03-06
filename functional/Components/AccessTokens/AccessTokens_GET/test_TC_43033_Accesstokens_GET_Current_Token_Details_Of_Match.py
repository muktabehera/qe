# -*- coding: UTF-8 -*-

"""PFE Component Tests - Access_Tokens.

* TC-43033 - Access_Tokens GET:

  Verify that user is able to GET current token details of "MATCH" using  "/accessTokens/currentTokenDetails".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer
       eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkZWZhdWx0Iiwic3ViIjoiZGVsaXZlcnlAdG9rZW4uY29tIiwiYXVkIjoicWVkOmRlZmF1bHQiLCJxZWRwIjpbIm0iXSwiZXhwIjoxNTAzNjYyMzU4fQ.5hqQGhp19-NeHoB61h4XJYR5_VvFSE8zOSiVmz67VjY"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/accessTokens/currentTokenDetails"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer
       eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkZWZhdWx0Iiwic3ViIjoiZGVsaXZlcnlAdG9rZW4uY29tIiwiYXVkIjoicWVkOmRlZmF1bHQiLCJxZWRwIjpbIm0iXSwiZXhwIjoxNTAzNjYyMzU4fQ.5hqQGhp19-NeHoB61h4XJYR5_VvFSE8zOSiVmz67VjY"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/accessTokens/currentTokenDetails"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Access_Tokens')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Access_Tokens test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43033')
    @pytest.mark.Access_Tokens
    @pytest.mark.GET
    def test_TC_43033_GET_Access_Tokens_Current_Token_Details_Of_Match(self, context):
        """TC-43033 - Access_Tokens-GET
           Verify that user is able to GET current token details of "MATCH" using  "/accessTokens/currentTokenDetails"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET current token details of "MATCH" using  "/accessTokens/currentTokenDetails"."""):

            ### Positive test example

            # getEntity the Access_Tokens.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Access_Tokens.getEntity(),
                token='invalid_token'
            )

        with pytest.allure.step("""Verify that user is able to GET current token details of "MATCH" using  "/accessTokens/currentTokenDetails"."""):

            ### Negative test example

            # getEntity the Access_Tokens, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Access_Tokens.getEntity(),
                    token='invalid_token',
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
