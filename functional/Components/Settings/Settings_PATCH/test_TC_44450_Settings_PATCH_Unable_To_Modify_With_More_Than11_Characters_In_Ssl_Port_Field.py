# -*- coding: UTF-8 -*-

"""PFE Component Tests - Settings.

* TC-44450 - Settings PATCH:

  Verify user is unable to modify settings on entering more than 11 characters in sslPort field using request PATCH /settings.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/settings"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/settings"

JSON data sent to PathFinder in this test:

  {'configured': True,
   'hostname': 'localhost',
   'port': 8080,
   'sslEnabled': True,
   'sslPort': 12345678901}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Settings')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Settings test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44450')
    @pytest.mark.Settings
    @pytest.mark.PATCH
    def test_TC_44450_PATCH_Settings_Unable_To_Modify_With_More_Than11_Characters_In_Ssl_Port_Field(self, context):
        """TC-44450 - Settings-PATCH
           Verify user is unable to modify settings on entering more than 11 characters in sslPort field using request PATCH /settings."""
        # Define a test step

        with pytest.allure.step("""Verify user is unable to modify settings on entering more than 11 characters in sslPort field using request PATCH /settings."""):

            # Test case configuration
            settingsDetails = context.sc.SettingsDetails(
                configured=True,
                hostname='localhost',
                port=8080,
                sslEnabled=True,
                sslPort=12345678901)


            # prepare the request, so we can modify it
            request = context.cl.Settings.updateSettings(
                    body=settingsDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateSettings the Settings, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Invalid request. Numeric value (12345678901) out of range of int')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
