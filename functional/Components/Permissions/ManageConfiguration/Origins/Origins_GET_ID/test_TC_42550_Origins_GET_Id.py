# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-42550 - Origins GET:

  Verify that user is able to view "Authorization System" and "Origin" under System Configuration with Manage Configuration permission. .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins/<data_ID1_under_test>   "

Same, with test data:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins/Auto_Origin     "

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Origins')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Origins test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42550')
    @pytest.mark.Origins
    @pytest.mark.GET
    def test_TC_42550_GET_Origins_Id(self, context):
        """TC-42550 - Origins-GET
           Verify that user is able to view "Authorization System" and "Origin" under System Configuration with Manage Configuration permission. ."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to view "Authorization System" and "Origin" under System Configuration with Manage Configuration permission. ."""):

            ### Positive test example

            # getEntity the Origins.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Origins.getEntity(
                    id='Auto_Origin')
            )

        with pytest.allure.step("""Verify that user is able to view "Authorization System" and "Origin" under System Configuration with Manage Configuration permission. ."""):

            ### Negative test example

            # getEntity the Origins, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Origins.getEntity(
                        id='Auto_Origin'),
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
