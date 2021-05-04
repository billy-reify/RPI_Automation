from api.endpoints.rpi_api_urls import RPIApiUrls,RPIApiHeaders
from api.endpoints.rpi_api_payloads import RPIPayloads
from api.utils.rpi_connection_definition import RPIConnectionProperties
from api.utils.request_execution import ExecuteRPIRequests
from api.utils.parse_response_data import ParseResponseData
from api.utils.utilites import Utilities

# Set testing environment. This would normally be passed in via pytest commandline
testing_env = 'testing'

# Initialize the ParseDataResponse class. We pass response data from the request to the class and depending on the
# method called we parse, store and validate response parameters.
parse_response = ParseResponseData()

# Initialize Utilities class. We use this class for generic helper methods.
utility = Utilities()

# Initialize dictionary to store site data collected
site_data = {}

# Initialize API authentication call and return valid key
rpi_headers = RPIApiHeaders.get_token_header()
rpi_payload = RPIConnectionProperties.get_connection_properties(testing_env)
rpi_url = RPIApiUrls.get_authentication_url(testing_env)
access_token = parse_response.get_auth_token(ExecuteRPIRequests.execute_rpi_api_call('POST',rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test Setup -- This will query for site information and return data related to Sites,Trials and Sponsors required for Referral tests.")
rpi_url = RPIApiUrls.get_sites()
rpi_headers = RPIApiHeaders.get_auth_header(access_token)
rpi_payload = RPIPayloads.get_empty_payload()
site_data = parse_response.get_sites_data(ExecuteRPIRequests.execute_rpi_api_call("GET",rpi_url,rpi_headers,rpi_payload))


print("\nReferral Setup -- (Post Referral) Validate that the response status code = 202 and that the subject_id returned match the test setup generated id .")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload),site_data)


##########################
# Update RPI Value Tests #
##########################

print("\nUpdate Test 1 -- (Update Subject) Validate that the response status code = 202 and that the subject_id returned match the test setup generated id. ")
rpi_url = RPIApiUrls.set_referral_subject_by_site_id_and_subject_id(site_data["site_id"],site_data["subjectId"])
rpi_headers = RPIApiHeaders.get_update_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_update_subject()
parse_response.validate_referral_update(ExecuteRPIRequests.execute_rpi_api_call("PUT",rpi_url,rpi_headers,rpi_payload),site_data)

print("\nUpdate Test 2 -- (Update Subject Blank Address) Validate that the response status code = 202 and that the subject_id returned match the test setup generated id. ")
rpi_url = RPIApiUrls.set_referral_subject_by_site_id_and_subject_id(site_data["site_id"],site_data["subjectId"])
rpi_headers = RPIApiHeaders.get_update_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_update_subject_blank_address_text()
parse_response.validate_referral_update(ExecuteRPIRequests.execute_rpi_api_call("PUT",rpi_url,rpi_headers,rpi_payload),site_data)

print("\nUpdate Test 3 -- (Update Subject 401) Validate that the response status code = 401.")
rpi_url = RPIApiUrls.set_referral_subject_by_site_id_and_subject_id(site_data["site_id"],site_data["subjectId"])
rpi_headers = RPIApiHeaders.get_401_header()
rpi_payload = RPIPayloads.get_referral_payload_update_subject_blank_address_text()
parse_response.validate_401_error(ExecuteRPIRequests.execute_rpi_api_call("PUT",rpi_url,rpi_headers,rpi_payload))

print("\nUpdate Test 4 -- (Update Subject Empty) Validate that the response status code = 400.")
rpi_url = RPIApiUrls.set_referral_subject_by_site_id_and_subject_id(site_data["site_id"],site_data["subjectId"])
rpi_headers = RPIApiHeaders.get_update_auth_header(access_token)
rpi_payload = RPIPayloads.get_400_payload()
parse_response.validate_400_error(ExecuteRPIRequests.execute_rpi_api_call("PUT",rpi_url,rpi_headers,rpi_payload))

print("\nUpdate Test 5 -- (Update Subject Empty Encounter) Validate that the response status code = 400.")
rpi_url = RPIApiUrls.set_referral_subject_by_site_id_and_subject_id(site_data["site_id"],site_data["subjectId"])
rpi_headers = RPIApiHeaders.get_update_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_update_subject_empty_encounter()
parse_response.validate_400_error(ExecuteRPIRequests.execute_rpi_api_call("PUT",rpi_url,rpi_headers,rpi_payload))

print("\nUpdate Test 6 -- (Update Subject Bad Subject Id) Validate that the response status code = 404.")
rpi_url = RPIApiUrls.set_referral_subject_by_site_id_and_subject_id(site_data["site_id"],str(utility.get_uuid()))
rpi_headers = RPIApiHeaders.get_update_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_update_subject_bad_subject_id()
parse_response.validate_404_error(ExecuteRPIRequests.execute_rpi_api_call("PUT",rpi_url,rpi_headers,rpi_payload))

print("\nUpdate Test 7 -- (Update Subject Bad Site Id) Validate that the response status code = 404.")
rpi_url = RPIApiUrls.set_referral_subject_by_site_id_and_subject_id(str(utility.get_uuid()),site_data["subjectId"])
rpi_headers = RPIApiHeaders.get_update_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_update_subject_bad_site_id()
parse_response.validate_404_error(ExecuteRPIRequests.execute_rpi_api_call("PUT",rpi_url,rpi_headers,rpi_payload))
