# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-43971 - Origins GET:

  Verify that user is able to GET the details of origins using request GET /origins with parameter prefix.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins?prefix=o &showAll=false"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins?prefix=o &showAll=false"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Origins')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Origins test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43971')
    @pytest.mark.Origins
    @pytest.mark.GET
    def test_TC_43971_GET_Origins_Prefix(self, context):
        """TC-43971 - Origins-GET
           Verify that user is able to GET the details of origins using request GET /origins with parameter prefix."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of origins using request GET /origins with parameter prefix."""):

            # listEntities the Origins.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Origins.listEntities(
                    prefix='o', 
                    showAll='false'
                )
            )
