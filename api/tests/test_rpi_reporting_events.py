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


print("\nTest Setup -- This test will query for site information and return data related to Sites,Trials and Sponsors.")
rpi_url = RPIApiUrls.get_sites()
rpi_headers = RPIApiHeaders.get_auth_header(access_token)
rpi_payload = RPIPayloads.get_empty_payload()
site_data = parse_response.get_sites_data(ExecuteRPIRequests.execute_rpi_api_call("GET",rpi_url,rpi_headers,rpi_payload))




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






