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



