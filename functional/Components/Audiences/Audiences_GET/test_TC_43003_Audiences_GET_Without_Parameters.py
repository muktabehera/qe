# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-43003 - Audiences GET:

  Verify that user is able to GET the details of Audience request /audiences  without providing any parameters.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Audiences')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Audiences test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43003')
    @pytest.mark.Audiences
    @pytest.mark.GET
    def test_TC_43003_GET_Audiences_Without_Parameters(self, context):
        """TC-43003 - Audiences-GET
           Verify that user is able to GET the details of Audience request /audiences  without providing any parameters."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of Audience request /audiences  without providing any parameters."""):

            # listEntities the Audiences.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Audiences.listEntities()
            )

