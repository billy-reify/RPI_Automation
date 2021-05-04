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
# Initialize collection_start_time variable used later in the test
# When we incorporate this into a production test we will need to generate this value at test start
# site_data.update(collection_start_time=utility.get_collection_start_time())
# print(str(site_data["collection_start_time"]))

# Initialize API authentication call and return valid key
rpi_headers = RPIApiHeaders.get_token_header()
rpi_payload = RPIConnectionProperties.get_connection_properties(testing_env)
rpi_url = RPIApiUrls.get_authentication_url(testing_env)
access_token = parse_response.get_auth_token(ExecuteRPIRequests.execute_rpi_api_call('POST',rpi_url,rpi_headers,rpi_payload))

###############
# Sites Tests #
###############

print("\nSites Test 1 -- This test will query for site information and return data related to Sites,Trials and Sponsors.")
rpi_url = RPIApiUrls.get_sites()
rpi_headers = RPIApiHeaders.get_auth_header(access_token)
rpi_payload = RPIPayloads.get_empty_payload()
site_data = parse_response.get_sites_data(ExecuteRPIRequests.execute_rpi_api_call("GET",rpi_url,rpi_headers,rpi_payload))


print("\n401 Sites Test 2 -- This negative test will pass if a 401 error is returned.")
# We are purposely passing an empty header to cause the 401 to occur
rpi_url = RPIApiUrls.set_sites_401()
rpi_headers = RPIApiHeaders.get_401_header()
rpi_payload = RPIPayloads.get_empty_payload()
parse_response.validate_401_error(ExecuteRPIRequests.execute_rpi_api_call("GET",rpi_url,rpi_headers,rpi_payload))

print("\nSites Test 3 -- We use the site_id variable from the site_data dictionary object to filter API data.")
# We then validate that the status = 200 and the site_id and trials_id exists within the filtered data
rpi_url = RPIApiUrls.get_sites_by_site_id(site_data['site_id'])
rpi_headers = RPIApiHeaders.get_auth_header(access_token)
rpi_payload = RPIPayloads.get_empty_payload()
parse_response.validate_sites_data(ExecuteRPIRequests.execute_rpi_api_call("GET",rpi_url,rpi_headers,rpi_payload))

print("\nSites Test 4 -- This negative test will pass if a 404 error is returned.")
# We are purposely passing an incorrect url (/rpi/sites/404) to the API to ensure a 404 error.
rpi_url = RPIApiUrls.set_sites_404()
rpi_headers = RPIApiHeaders.get_auth_header(access_token)
rpi_payload = RPIPayloads.get_empty_payload()
parse_response.validate_404_error(ExecuteRPIRequests.execute_rpi_api_call("GET",rpi_url,rpi_headers,rpi_payload))

print("\n401 Sites Test 5 -- This negative test will pass if a 401 error is returned.")
# We are purposely passing an empty header to cause the 401 to occur.
# We are passing a valid site id to the sites endpoint
rpi_url = RPIApiUrls.get_sites_by_site_id(site_data['site_id'])
rpi_headers = RPIApiHeaders.get_401_header()
rpi_payload = RPIPayloads.get_empty_payload()
parse_response.validate_401_error(ExecuteRPIRequests.execute_rpi_api_call("GET",rpi_url,rpi_headers,rpi_payload))

print("\nSites Test 6 -- This test will submit an incorrect site_id and will pass if a 404 error is returned.")
# We are purposely passing an incorrect url (/rpi/sites/uuid.value) to the API to ensure a 404 error.
rpi_url = RPIApiUrls.get_sites_by_site_id(str(utility.get_uuid()))
rpi_headers = RPIApiHeaders.get_auth_header(access_token)
rpi_payload = RPIPayloads.get_empty_payload()
parse_response.validate_404_error(ExecuteRPIRequests.execute_rpi_api_call("GET",rpi_url,rpi_headers,rpi_payload))

##################
# Referral Tests #
##################

print("\nReferral Test 1 -- (Post Referral) Validate that the response status code = 202 and that the subject_id returned match the test setup generated id .")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload),site_data)

print("\nReferral Test 2 -- (401: Post Referral) Validate that calling a valid referral url without an authorization token will generate a 401 error.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_401_header()
rpi_payload = RPIPayloads.get_referral_payload(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_401_error(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 3 -- (Post Referral Maximal) Validate that the response status code = 202 and that the subject_id returned matches the test setup generated subject_id .")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_maximal(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload),site_data)

print("\nReferral Test 4 -- (Post Referral Minimal) Validate that the response status code = 202 and that the subject_id returned matches the test setup generated subject_id .")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_minimal(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload),site_data)

print("\nReferral Test 5 -- (Post Referral Multi Trial) Validate that the response status code = 202 and that the subject_id "
      "returned matches the test setup generated subject_id as well as the alternate_trial_id.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_multi_trial(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"],
                                                                site_data["alternate_trial_id"],site_data["alternate_sponsor_site_id"])
parse_response.validate_multi_trial_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload),site_data)

print("\nReferral Test 6 -- (Post Referral Blank Address Text) Validate that the response status code = 202 and that the subject_id "
      "returned matches the test setup generated subject_id.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_blank_address_text(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload),site_data)

print("\nReferral Test 7 -- (Post Referral Bad Site Id) Validate that the response status code = 404. "
      "We are intentionally passing an unknown or bad site_id to generate the 404 response error.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(str(utility.get_uuid()))
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_404_error(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 8 -- (Post Referral Bad Trial Id) Validate that the response status code = 404. "
      "We are intentionally passing an unknown or bad trial_id to generate the 404 response error.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload(site_data["subjectId"],str(utility.get_uuid()),site_data["sponsorSiteId"])
parse_response.validate_404_error(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 9 -- (Post Referral Bad Alternate Trial Id) Validate that the response status code = 404 "
      "We are intentionally passing an unknown or bad alternate trial_id to generate the 404 response error.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_multi_trial(site_data["subjectId"],site_data["trial_id"],
                                                                site_data["sponsorSiteId"],str(utility.get_uuid()),
                                                                site_data["alternate_sponsor_site_id"])
parse_response.validate_404_error(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 10 -- (Post Referral Bad Sponsor Site Id) Validate that the response status code = 404. "
      "We are intentionally passing an unknown or bad sponsor_site_id to generate the 404 response error.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload(site_data["subjectId"],site_data["trial_id"],str(utility.get_uuid()))
parse_response.validate_404_error(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 11 -- (Post Referral Value Integer) Validate that an integer value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_integer_answer_value(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload),site_data)

print("\nReferral Test 12 -- (Post Referral Value Uri) Validate that an integer value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_uri_value(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload),site_data)

print("\nReferral Test 13 -- (Post Referral Value Uri) Validate that an Uri value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_uri_value(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload),site_data)

print("\nReferral Test 14 -- (Post Referral Value Bad LinkId Response) Validate that an bad LinkId value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_bad_link_id_value(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_bad_linked_id_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 15 -- (Post Referral Value Boolean) Validate that a boolean value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_boolean_value(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload),site_data)


print("\nReferral Test 16 -- (Post Referral Value Coding) Validate that a coding value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_coding_value(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload),site_data)

print("\nReferral Test 17 -- (Post Referral Value Decimal) Validate that a decimal value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_decimal_value(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload),site_data)

print("\nReferral Test 18 -- (Post Referral Value String) Validate that a string value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_text_value(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload),site_data)

print("\nReferral Test 19 -- (Post Referral Value Time) Validate that a time value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_time_value(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload),site_data)

print("\nReferral Test 20 -- (Post Referral Value Date Time) Validate that a date and time value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_time_and_date(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload),site_data)

print("\nReferral Test 21 -- (Post Referral Value Date) Validate that a date value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_date(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload),site_data)

print("\nReferral Test 22 -- (Post Referral Bad Email) Validate that a bad email value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_bad_email(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_bad_email_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 23 -- (Post Referral Bad Coding) Validate that a bad coding value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_bad_coding(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_bad_coding_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 24 -- (Post Referral Bad Source) Validate that a bad source value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_bad_source(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_bad_source_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 25 -- (Post Referral Bad Response) Validate that a bad response value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_bad_response(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_bad_response_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 26 -- (Post Referral Empty Answer) Validate that a empty answer value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_empty_answer(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_empty_answer_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 27 -- (Post Referral Empty Telecom Period) Validate that a empty telecom period value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_empty_telecom_period(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_empty_telecom_period_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 28 -- (Post Referral Empty Line) Validate that a empty line value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_empty_line(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_empty_line_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 29 -- (Post Referral Empty Address) Validate that a empty address value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_empty_address(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_empty_address_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 30 -- (Post Referral Empty Alt Trials Id) Validate that a empty alt trials id value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_empty_alternate_trial_ids(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_empty_alt_trials_id_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 31 -- (Post Referral Empty Encounter) Validate that a empty encounter value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_empty_encounters(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_empty_encounter_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 32 -- (Post Referral Empty Response Item) Validate that a empty response item value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_empty_response_item(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_empty_response_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 33 -- (Post Referral Empty Given Name) Validate that a empty given name item value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_empty_given_name(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_empty_given_name_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 34 -- (Post Referral Empty Telecom) Validate that a empty telecom value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_empty_telecom(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"])
parse_response.validate_empty_telecom_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 35 -- (Post Referral Empty) Validate that a empty referral {} value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_empty_referral_payload()
parse_response.validate_empty_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 36 -- (Post Referral Empty Referral) Validate that a empty referral {referral: []} value can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_empty_referral()
parse_response.validate_empty_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload))

print("\nReferral Test 37 -- (Post Two Referral) Validate that two referrals can be passed to response.")
site_data.update(subjectId=str(utility.get_uuid()))
site_data.update(alternatesubjectId=str(utility.get_uuid()))
rpi_url = RPIApiUrls.get_referral_by_site_id(site_data["site_id"])
rpi_headers = RPIApiHeaders.get_referral_auth_header(access_token)
rpi_payload = RPIPayloads.get_referral_payload_with_two_referrals(site_data["subjectId"],site_data["trial_id"],site_data["sponsorSiteId"],site_data["alternatesubjectId"])
parse_response.validate_two_referral_post(ExecuteRPIRequests.execute_rpi_api_call("POST",rpi_url,rpi_headers,rpi_payload),site_data)


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

##############################
# RPI Reporting Events Tests #
##############################

print("\nRPI Reporting Test 1 -- (RPI Reporting Events) Validate status code = 200. That response contains the following: "
      "pagination element events greater than 0 and that trial,alternate_trial Id's are present and valid")
rpi_url = RPIApiUrls.get_reporting_events_by_collection_start_date(str(site_data["collection_start_time"]))
rpi_headers = RPIApiHeaders.get_auth_header(access_token)
rpi_payload = RPIPayloads.get_empty_dict_payload()
parse_response.validate_rpi_reporting_events(ExecuteRPIRequests.execute_rpi_api_call("GET",rpi_url,rpi_headers,rpi_payload),site_data)


print("\nRPI Reporting Test 2 -- (RPI Reporting Events Limit) Validate status code = 200. That response contains the following: "
      "pagination element events greater than 0 and that trial,alternate_trial Id's are present and valid")
rpi_url = RPIApiUrls.get_reporting_events_by_collection_start_date_with_limit(str(site_data["collection_start_time"]))
rpi_headers = RPIApiHeaders.get_auth_header(access_token)
rpi_payload = RPIPayloads.get_empty_dict_payload()
parse_response.validate_rpi_reporting_events_with_limit(ExecuteRPIRequests.execute_rpi_api_call("GET",rpi_url,rpi_headers,rpi_payload))

print("\nRPI Reporting Test 3 -- (RPI Reporting Events Pagination) Validate status code = 200. That response contains the following: "
      "pagination element events greater than 0 and that trial,alternate_trial Id's are present and valid")
rpi_url = RPIApiUrls.get_reporting_events_by_collection_start_date_with_limit(str(site_data["collection_start_time"]))
rpi_headers = RPIApiHeaders.get_auth_header(access_token)
rpi_payload = RPIPayloads.get_empty_dict_payload()
pagination_url = parse_response.get_pagination_url(ExecuteRPIRequests.execute_rpi_api_call("GET",rpi_url,rpi_headers,rpi_payload))
parse_response.validate_rpi_reporting_events(ExecuteRPIRequests.execute_rpi_api_call("GET",pagination_url,rpi_headers,rpi_payload),site_data)

print("\nRPI Reporting Test 4 -- (RPI Reporting Events Trial Filter) Validate status code = 200. That response contains the following: "
      "pagination element events greater than 0 and that trial,alternate_trial Id's are present and valid")
rpi_url = RPIApiUrls.get_reporting_events_by_collection_start_date_and_trial_id(str(site_data["collection_start_time"]),site_data["alternate_sponsor_site_id"])
rpi_headers = RPIApiHeaders.get_auth_header(access_token)
rpi_payload = RPIPayloads.get_empty_dict_payload()
parse_response.validate_rpi_reporting_events(ExecuteRPIRequests.execute_rpi_api_call("GET",rpi_url,rpi_headers,rpi_payload),site_data)

print("\nRPI Reporting Test 5 -- (RPI Reporting Bad Events) Validate status code = 400.")
rpi_url = RPIApiUrls.get_reporting_events_with_bad_event()
rpi_headers = RPIApiHeaders.get_auth_header(access_token)
rpi_payload = RPIPayloads.get_empty_dict_payload()
parse_response.validate_400_error(ExecuteRPIRequests.execute_rpi_api_call("GET",rpi_url,rpi_headers,rpi_payload))

print("\nRPI Reporting Test 6 -- (RPI Reporting No Events) Validate status code = 400.")
rpi_url = RPIApiUrls.get_reporting_events_with_no_event(str(site_data["collection_start_time"]))
rpi_headers = RPIApiHeaders.get_auth_header(access_token)
rpi_payload = RPIPayloads.get_empty_dict_payload()
parse_response.validate_400_error(ExecuteRPIRequests.execute_rpi_api_call("GET",rpi_url,rpi_headers,rpi_payload))

print("\nRPI Reporting Test 7 -- (RPI Reporting Events Bad Trial ID) Validate status code = 404.")
rpi_url = RPIApiUrls.get_reporting_events_by_with_bad_trial_id()
rpi_headers = RPIApiHeaders.get_auth_header(access_token)
rpi_payload = RPIPayloads.get_empty_dict_payload()
parse_response.validate_404_error(ExecuteRPIRequests.execute_rpi_api_call("GET",rpi_url,rpi_headers,rpi_payload))











