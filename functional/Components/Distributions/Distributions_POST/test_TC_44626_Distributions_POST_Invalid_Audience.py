# -*- coding: UTF-8 -*-

"""PFE Component Tests - Distributions.

* TC-44626 - Distributions POST:

  Verify that user is unable to create Distribution  if invalid  targetAudiences 'ID' value is provided using request POST /distributions .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/distributions"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/distributions"

JSON data sent to PathFinder in this test:

  {'activationDate': '2017-09-06T07:36:46.542Z',
   'distributionPolicy': 'REQUIRED',
   'files': [{'id': 'FileID123',
              'sourceUrl': 'qedorigin://Auto_storage/MP4File.mp4',
              'streamMetadata': {'bitrateKbps': 100,
                                 'height': 5,
                                 'mimeType': 'Video/mp4',
                                 'width': 10}}],
   'id': 'invalidDistributionAudi',
   'name': 'Distribution with invalid Audience',
   'targetAudiences': [{'id': 'Invalid_Audience'}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Distributions')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Distributions test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44626')
    @pytest.mark.Distributions
    @pytest.mark.POST
    def test_TC_44626_POST_Distributions_Invalid_Audience(self, context):
        """TC-44626 - Distributions-POST
           Verify that user is unable to create Distribution  if invalid  targetAudiences 'ID' value is provided using request POST /distributions ."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to create Distribution  if invalid  targetAudiences 'ID' value is provided using request POST /distributions ."""):

            ### Positive test example

            # Test case configuration
            distributionDetails = context.sc.DistributionDetails(
                activationDate='2017-09-06T07:36:46.542Z',
                distributionPolicy='REQUIRED',
                expirationDate=None,
                files=[{
                    'id': 'FileID123',
                    'sourceUrl': 'qedorigin://Auto_storage/MP4File.mp4',
                    'streamMetadata': {
                        'bitrateKbps': 100,
                        'width': 10,
                        'height': 5,
                        'mimeType': 'Video/mp4'
                    }
                }],
                id='invalidDistributionAudi',
                name='Distribution with invalid Audience',
                status=None,
                tags=None,
                targetAudiences=[{
                    'id': 'Invalid_Audience'
                }])


            # createEntity the Distributions.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Distributions.createEntity(
                    body=distributionDetails
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is unable to create Distribution  if invalid  targetAudiences 'ID' value is provided using request POST /distributions ."""):

            ### Negative test example

            # Test case configuration
            distributionDetails = context.sc.DistributionDetails(
                activationDate='2017-09-06T07:36:46.542Z',
                distributionPolicy='REQUIRED',
                expirationDate=None,
                files=[{
                    'id': 'FileID123',
                    'sourceUrl': 'qedorigin://Auto_storage/MP4File.mp4',
                    'streamMetadata': {
                        'bitrateKbps': 100,
                        'width': 10,
                        'height': 5,
                        'mimeType': 'Video/mp4'
                    }
                }],
                id='invalidDistributionAudi',
                name='Distribution with invalid Audience',
                status=None,
                tags=None,
                targetAudiences=[{
                    'id': 'Invalid_Audience'
                }])


            # prepare the request, so we can modify it
            request = context.cl.Distributions.createEntity(
                    body=distributionDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # createEntity the Distributions, and check we got the error we expect
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
