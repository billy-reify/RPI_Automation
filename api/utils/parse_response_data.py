from api.utils.utilites import Utilities
class ParseResponseData(object):


    @staticmethod
    def get_auth_token(data):
        if data['status_code'] == 200:
            auth_token = data['response_json']['access_token']
            if len(auth_token) > 0:
                print(auth_token)
                print("Pass -- Validated that the API framework returned a valid authentication key.")
            return auth_token
        else:
            raise Exception("Failed to get Access Token, server returned status code: " + str(data['status_code']))
        
    @staticmethod
    def get_sites_data(data):
        if data['status_code'] == 200:
            site_data = {}
            if len(data['response_json'][0]["id"]) > 0:
                site_id = data['response_json'][0]["id"]
                postalCode = data['response_json'][0]["postalCode"]
                siteName = data['response_json'][0]["siteName"]
                country = data['response_json'][0]["country"]
                site_data.update(site_id=site_id)
                site_data.update(postalCode=postalCode)
                site_data.update(siteName=siteName)
                site_data.update(country=country)
                if len(data['response_json'][0]["trials"][0]["id"]) > 0:
                    trial_id = data['response_json'][0]["trials"][0]["id"]
                    sponsorSiteId = data['response_json'][0]["trials"][0]["sponsorSiteId"]
                    site_data.update(trial_id=trial_id)
                    site_data.update(sponsorSiteId=sponsorSiteId)
            if len(data['response_json'][0]["trials"]) > 1:
                alternate_trial_id = data['response_json'][0]["trials"][1]["id"]
                alternate_sponsor_site_id = data['response_json'][0]["trials"][1]["sponsorSiteId"]
                site_data.update(alternate_trial_id=alternate_trial_id)
                site_data.update(alternate_sponsor_site_id=alternate_sponsor_site_id)

            site_data.update(collection_start_time=Utilities.get_collection_start_time())

            if len(site_data) > 0:
                print("Pass -- Validated that the Sites API call returned data.")
            return site_data
        else:
            raise Exception("Failed to get sites data, server returned status code: " + str(data['status_code']) + " " + str(data['status_text']))

    @staticmethod
    def validate_401_error(data):
        if data['status_code'] == 401:
            print("Pass -- Validated that the request status code = 401")
        else:
            print("Fail -- Validated that the request status code != 401..\n The status code received was: " + str(data['status_code']) + " " + str(data['status_text']))

    @staticmethod
    def validate_404_error(data):
        if data['status_code'] == 404:
            print("Pass -- Validated that the request status code = 404")
        else:
            print("Fail -- Validated that the request status code != 404..\n The status code received was: " + str(data['status_code']) + " " + str(data['status_text']))

    @staticmethod
    def validate_400_error(data):
        if data['status_code'] == 400:
            print("Pass -- Validated that the request status code = 400")
        else:
            print("Fail -- Validated that the request status code != 400..\n The status code received was: " + str(
                data['status_code']) + " " + str(data['status_text']))

    @staticmethod
    def validate_sites_data(data):
        if data['status_code'] == 200:
            print("Pass -- Validated that the request status code = 200")
            if len(data['response_json']["id"]) > 0:
                print("Pass -- Validated that the site id of: " + str(data['response_json']["id"]) + " exists within the response data.")
            else:
                print("Fail -- Validated that the site id does not exist within the response data.")

            if len(data['response_json']["trials"][0]["id"]) > 0:
                print("Pass -- Validated that the trial id of: " + str(data['response_json']["trials"][0]["id"]) + " exists within the response data.")
            else:
                print("Fail -- Validated that the trial id does not exist within the response data.")
        else:
            print("Fail -- Validated that the request status code != 200..\n The status code received was: " + str(data['status_code']) + " " + str(data['status_text']))


    @staticmethod
    def validate_referral_post(data,site_data):
        if data['status_code'] == 202:
            print("Pass -- Validated that the request status code = 202")
            if len(data['response_json']["id"]) > 0:
                print("Pass -- Validated that the id of: " + str(data['response_json']["id"]) + " exists within the response data.")
            else:
                print("Fail -- Validated that the id does not exist within the response data.")

            if len(data["response_json"]["payload"]["referral"][0]["subjectId"]) > 0:
                print("Pass -- Validated that the subject_id of: " + str(data["response_json"]["payload"]["referral"][0]["subjectId"]) + " exists within the response data.")
                if data["response_json"]["payload"]["referral"][0]["subjectId"] in site_data["subjectId"]:
                    print("Pass -- Validated that the subject_id of: " + str(data["response_json"]["payload"]["referral"][0]["subjectId"]) +
                          " returned by RPI matches the subject_id " + str(site_data["subjectId"]) + " generated by the test.")
                else:
                    print("Fail -- Validated that the subject_id of: " + str(data["response_json"]["payload"]["referral"][0]["subjectId"]) +
                          " returned by RPI does NOT match the subject_id " + str(
                        site_data["subject_id"]) + " generated by the test.")
            else:
                print("Fail -- Validated that the subject_id does not exist within the response data.")
        else:
            print("Fail -- Validated that the request status code != 202..\n The status code received was: " + str(data['status_code']) + " " + str(data['status_text']))


    @staticmethod
    def validate_multi_trial_referral_post(data,site_data):
        if data['status_code'] == 202:
            print("Pass -- Validated that the request status code = 202")
            if len(data['response_json']["id"]) > 0:
                print("Pass -- Validated that the id of: " + str(data['response_json']["id"]) + " exists within the response data.")
            else:
                print("Fail -- Validated that the id does not exist within the response data.")

            if len(data["response_json"]["payload"]["referral"][0]["subjectId"]) > 0:
                print("Pass -- Validated that the subject_id of: " + str(data["response_json"]["payload"]["referral"][0]["subjectId"]) + " exists within the response data.")
                if data["response_json"]["payload"]["referral"][0]["subjectId"] in site_data["subjectId"]:
                    print("Pass -- Validated that the subject_id of: " + str(data["response_json"]["payload"]["referral"][0]["subjectId"]) +
                          " returned by RPI matches the subject_id " + str(site_data["subjectId"]) + " generated by the test.")
                else:
                    print("Fail -- Validated that the subject_id of: " + str(data["response_json"]["payload"]["referral"][0]["subjectId"]) +
                          " returned by RPI does NOT match the subject_id " + str(
                        site_data["subject_id"]) + " generated by the test.")
            else:
                print("Fail -- Validated that the subject_id does not exist within the response data.")

            if len(data["response_json"]["payload"]["referral"][0]["alternateTrials"][0]["id"]) > 0:
                print("Pass -- Validated that the alternate trial id of: " + str(data["response_json"]["payload"]["referral"][0]["alternateTrials"][0]["id"]) + " exists within the response data.")
                if data["response_json"]["payload"]["referral"][0]["alternateTrials"][0]["id"] in site_data["alternate_trial_id"]:
                    print("Pass -- Validated that the alternate trial id of: " + str(data["response_json"]["payload"]["referral"][0]["alternateTrials"][0]["id"]) +
                          " returned by RPI matches the alternate trial id " + str(site_data["alternate_trial_id"]) + " generated by the test.")
                else:
                    print("Fail -- Validated that the alternate trial id: " + str(data["response_json"]["payload"]["referral"][0]["alternateTrials"][0]["id"]) +
                          " returned by RPI does NOT match the alternate trial id " + str(
                        site_data["alternate_trial_id"]) + " generated by the test.")
            else:
                print("Fail -- Validated that the alternate trial id does not exist within the response data.")


        else:
            print("Fail -- Validated that the request status code != 202..\n The status code received was: " + str(data['status_code']))

    @staticmethod
    def validate_bad_linked_id_referral_post(data):
        if data['status_code'] == 400:
            print("Pass -- Validated that the request status code = 400")
        else:
            print("Fail -- Validated that the request status code != 400..\n The status code received was: " + str(data['status_code']) + " " + str(data['status_text']))

        if 'message' in data["response_json"]:
            print("Pass -- Validated that the json key \"message\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"message\" was NOT present within the response.")

        if 'Invalid Payload' in data["response_json"]["message"]:
            print("Pass -- Validated that the error message \"Invalid Payload\" was present within the response.")
        else:
            print("Fail -- Validated that the error message \"Invalid Payload\" was NOT present within the response.")

        if 'errors' in data["response_json"]:
            print("Pass -- Validated that the json key \"errors\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"errors\" was NOT present within the response.")

        if len(data["response_json"]["errors"]) == 2:
            print("Pass -- Validated that the number of errors within the response was 2.")
        else:
            print("Fail -- Validated that the number of errors within the response was NOT 2")


    @staticmethod
    def validate_bad_email_referral_post(data):
        if data['status_code'] == 400:
            print("Pass -- Validated that the request status code = 400")
        else:
            print("Fail -- Validated that the request status code != 400..\n The status code received was: " + str(
                data['status_code']) + " " + str(data['status_text']))

        if 'message' in data["response_json"]:
            print("Pass -- Validated that the json key \"message\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"message\" was NOT present within the response.")

        if 'Invalid Payload' in data["response_json"]["message"]:
            print("Pass -- Validated that the error message \"Invalid Payload\" was present within the response.")
        else:
            print("Fail -- Validated that the error message \"Invalid Payload\" was NOT present within the response.")

        if 'errors' in data["response_json"]:
            print("Pass -- Validated that the json key \"errors\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"errors\" was NOT present within the response.")

        if "The value must be a valid email" in data["response_json"]["errors"][0]["reason"]:
            print("Pass -- Validated that the reason field value matched the expected result.")
        else:
            print("Fail -- Validated that the reason field value did NOT match the expected result.")

    @staticmethod
    def validate_bad_coding_referral_post(data):
        if data['status_code'] == 400:
            print("Pass -- Validated that the request status code = 400")
        else:
            print("Fail -- Validated that the request status code != 400..\n The status code received was: " + str(
                data['status_code']) + " " + str(data['status_text']))

        if 'message' in data["response_json"]:
            print("Pass -- Validated that the json key \"message\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"message\" was NOT present within the response.")

        if 'Invalid Payload' in data["response_json"]["message"]:
            print("Pass -- Validated that the error message \"Invalid Payload\" was present within the response.")
        else:
            print("Fail -- Validated that the error message \"Invalid Payload\" was NOT present within the response.")

        if 'errors' in data["response_json"]:
            print("Pass -- Validated that the json key \"errors\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"errors\" was NOT present within the response.")

        if "Must not be empty" in data["response_json"]["errors"][0]["reason"]:
            print("Pass -- Validated that the reason field value matched the expected result.")
        else:
            print("Fail -- Validated that the reason field value did NOT match the expected result.")

    @staticmethod
    def validate_bad_source_referral_post(data):
        if data['status_code'] == 400:
            print("Pass -- Validated that the request status code = 400")
        else:
            print("Fail -- Validated that the request status code != 400..\n The status code received was: " + str(
                data['status_code']) + " " + str(data['status_text']))

        if 'message' in data["response_json"]:
            print("Pass -- Validated that the json key \"message\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"message\" was NOT present within the response.")

        if 'Invalid Payload' in data["response_json"]["message"]:
            print("Pass -- Validated that the error message \"Invalid Payload\" was present within the response.")
        else:
            print("Fail -- Validated that the error message \"Invalid Payload\" was NOT present within the response.")

        if 'errors' in data["response_json"]:
            print("Pass -- Validated that the json key \"errors\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"errors\" was NOT present within the response.")

        if "Must be one of" in data["response_json"]["errors"][0]["reason"]:
            print("Pass -- Validated that the reason field value matched the expected result.")
        else:
            print("Fail -- Validated that the reason field value did NOT match the expected result.")

    @staticmethod
    def validate_empty_answer_referral_post(data):
        if data['status_code'] == 400:
            print("Pass -- Validated that the request status code = 400")
        else:
            print("Fail -- Validated that the request status code != 400..\n The status code received was: " + str(
                data['status_code']) + " " + str(data['status_text']))

        if 'message' in data["response_json"]:
            print("Pass -- Validated that the json key \"message\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"message\" was NOT present within the response.")

        if 'Invalid Payload' in data["response_json"]["message"]:
            print("Pass -- Validated that the error message \"Invalid Payload\" was present within the response.")
        else:
            print("Fail -- Validated that the error message \"Invalid Payload\" was NOT present within the response.")

        if 'errors' in data["response_json"]:
            print("Pass -- Validated that the json key \"errors\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"errors\" was NOT present within the response.")

        if "Must not be empty" in data["response_json"]["errors"][0]["reason"]:
            print("Pass -- Validated that the reason field value \"Must not be empty\" matched the expected result.")
        else:
            print(
                "Fail -- Validated that the reason field value \"Must not be empty\" did NOT match the expected result.")

        if "encounter" in data["response_json"]["errors"][0]["path"][2]:
            print("Pass -- Validated that the json value \"encounter\" was present within the response.")
        else:
            print("Fail -- Validated that the json value \"encounter\" was NOT present within the response.")

        if "answer" in data["response_json"]["errors"][0]["path"][7]:
            print("Pass -- Validated that the json value \"answer\" was present within the response.")
        else:
            print("Fail -- Validated that the json value \"answer\" was NOT present within the response.")

    @staticmethod
    def validate_bad_response_referral_post(data):
        if data['status_code'] == 400:
            print("Pass -- Validated that the request status code = 400")
        else:
            print("Fail -- Validated that the request status code != 400..\n The status code received was: " + str(
                data['status_code']) + " " + str(data['status_text']))

        if 'message' in data["response_json"]:
            print("Pass -- Validated that the json key \"message\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"message\" was NOT present within the response.")

        if 'Invalid Payload' in data["response_json"]["message"]:
            print("Pass -- Validated that the error message \"Invalid Payload\" was present within the response.")
        else:
            print("Fail -- Validated that the error message \"Invalid Payload\" was NOT present within the response.")

        if 'errors' in data["response_json"]:
            print("Pass -- Validated that the json key \"errors\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"errors\" was NOT present within the response.")

        if len(data["response_json"]["errors"]) == 2:
            print("Pass -- Validated that the number of errors within the response was 2.")
        else:
            print("Fail -- Validated that the number of errors within the response was NOT 2")

        if "Required attribute" in data["response_json"]["errors"][0]["reason"]:
            print("Pass -- Validated that the reason field one value matched the expected result.")
        else:
            print("Fail -- Validated that the reason field value one did NOT match the expected result.")

        if "Required attribute" in data["response_json"]["errors"][1]["reason"]:
            print("Pass -- Validated that the reason field two value matched the expected result.")
        else:
            print("Fail -- Validated that the reason field value two did NOT match the expected result.")

    @staticmethod
    def validate_empty_telecom_period_referral_post(data):
        if data['status_code'] == 400:
            print("Pass -- Validated that the request status code = 400")
        else:
            print("Fail -- Validated that the request status code != 400..\n The status code received was: " + str(
                data['status_code']) + " " + str(data['status_text']))

        if 'message' in data["response_json"]:
            print("Pass -- Validated that the json key \"message\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"message\" was NOT present within the response.")

        if 'Invalid Payload' in data["response_json"]["message"]:
            print("Pass -- Validated that the error message \"Invalid Payload\" was present within the response.")
        else:
            print("Fail -- Validated that the error message \"Invalid Payload\" was NOT present within the response.")

        if 'errors' in data["response_json"]:
            print("Pass -- Validated that the json key \"errors\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"errors\" was NOT present within the response.")

        if "Must not be empty" in data["response_json"]["errors"][0]["reason"]:
            print("Pass -- Validated that the reason field value \"Must not be empty\" matched the expected result.")
        else:
            print(
                "Fail -- Validated that the reason field value \"Must not be empty\" did NOT match the expected result.")

        if "telecom" in data["response_json"]["errors"][0]["path"][2]:
            print("Pass -- Validated that the json value \"telecom\" was present within the response.")
        else:
            print("Fail -- Validated that the json value \"telecom\" was NOT present within the response.")

        if "period" in data["response_json"]["errors"][0]["path"][4]:
            print("Pass -- Validated that the json value \"period\" was present within the response.")
        else:
            print("Fail -- Validated that the json value \"period\" was NOT present within the response.")

    @staticmethod
    def validate_empty_line_referral_post(data):
        if data['status_code'] == 400:
            print("Pass -- Validated that the request status code = 400")
        else:
            print("Fail -- Validated that the request status code != 400..\n The status code received was: " + str(
                data['status_code']) + " " + str(data['status_text']))

        if 'message' in data["response_json"]:
            print("Pass -- Validated that the json key \"message\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"message\" was NOT present within the response.")

        if 'Invalid Payload' in data["response_json"]["message"]:
            print("Pass -- Validated that the error message \"Invalid Payload\" was present within the response.")
        else:
            print("Fail -- Validated that the error message \"Invalid Payload\" was NOT present within the response.")

        if 'errors' in data["response_json"]:
            print("Pass -- Validated that the json key \"errors\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"errors\" was NOT present within the response.")

        if "Must not be empty" in data["response_json"]["errors"][0]["reason"]:
            print("Pass -- Validated that the reason field value \"Must not be empty\" matched the expected result.")
        else:
            print(
                "Fail -- Validated that the reason field value \"Must not be empty\" did NOT match the expected result.")

        if "line" in data["response_json"]["errors"][0]["path"][4]:
            print("Pass -- Validated that the json value \"line\" was present within the response.")
        else:
            print("Fail -- Validated that the json value \"line\" was NOT present within the response.")

    @staticmethod
    def validate_empty_address_referral_post(data):
        if data['status_code'] == 400:
            print("Pass -- Validated that the request status code = 400")
        else:
            print("Fail -- Validated that the request status code != 400..\n The status code received was: " + str(
                data['status_code']) + " " + str(data['status_text']))

        if 'message' in data["response_json"]:
            print("Pass -- Validated that the json key \"message\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"message\" was NOT present within the response.")

        if 'Invalid Payload' in data["response_json"]["message"]:
            print("Pass -- Validated that the error message \"Invalid Payload\" was present within the response.")
        else:
            print("Fail -- Validated that the error message \"Invalid Payload\" was NOT present within the response.")

        if 'errors' in data["response_json"]:
            print("Pass -- Validated that the json key \"errors\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"errors\" was NOT present within the response.")

        if "Must not be empty" in data["response_json"]["errors"][0]["reason"]:
            print("Pass -- Validated that the reason field value \"Must not be empty\" matched the expected result.")
        else:
            print(
                "Fail -- Validated that the reason field value \"Must not be empty\" did NOT match the expected result.")

        if "address" in data["response_json"]["errors"][0]["path"][2]:
            print("Pass -- Validated that the json value \"address\" was present within the response.")
        else:
            print("Fail -- Validated that the json value \"address\" was NOT present within the response.")

    @staticmethod
    def validate_empty_alt_trials_id_referral_post(data):
        if data['status_code'] == 400:
            print("Pass -- Validated that the request status code = 400")
        else:
            print("Fail -- Validated that the request status code != 400..\n The status code received was: " + str(
                data['status_code']) + " " + str(data['status_text']))

        if 'message' in data["response_json"]:
            print("Pass -- Validated that the json key \"message\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"message\" was NOT present within the response.")

        if 'Invalid Payload' in data["response_json"]["message"]:
            print("Pass -- Validated that the error message \"Invalid Payload\" was present within the response.")
        else:
            print("Fail -- Validated that the error message \"Invalid Payload\" was NOT present within the response.")

        if 'errors' in data["response_json"]:
            print("Pass -- Validated that the json key \"errors\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"errors\" was NOT present within the response.")

        if "Must not be empty" in data["response_json"]["errors"][0]["reason"]:
            print("Pass -- Validated that the reason field value \"Must not be empty\" matched the expected result.")
        else:
            print(
                "Fail -- Validated that the reason field value \"Must not be empty\" did NOT match the expected result.")

        if "alternateTrials" in data["response_json"]["errors"][0]["path"][2]:
            print("Pass -- Validated that the json value \"alternateTrials\" was present within the response.")
        else:
            print("Fail -- Validated that the json value \"alternateTrials\" was NOT present within the response.")

    @staticmethod
    def validate_empty_encounter_referral_post(data):
        if data['status_code'] == 400:
            print("Pass -- Validated that the request status code = 400")
        else:
            print("Fail -- Validated that the request status code != 400..\n The status code received was: " + str(
                data['status_code']) + " " + str(data['status_text']))

        if 'message' in data["response_json"]:
            print("Pass -- Validated that the json key \"message\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"message\" was NOT present within the response.")

        if 'Invalid Payload' in data["response_json"]["message"]:
            print("Pass -- Validated that the error message \"Invalid Payload\" was present within the response.")
        else:
            print("Fail -- Validated that the error message \"Invalid Payload\" was NOT present within the response.")

        if 'errors' in data["response_json"]:
            print("Pass -- Validated that the json key \"errors\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"errors\" was NOT present within the response.")

        if "Must not be empty" in data["response_json"]["errors"][0]["reason"]:
            print("Pass -- Validated that the reason field value \"Must not be empty\" matched the expected result.")
        else:
            print("Fail -- Validated that the reason field value \"Must not be empty\" did NOT match the expected result.")

        if "encounter" in data["response_json"]["errors"][0]["path"][2]:
            print("Pass -- Validated that the json value \"encounter\" was present within the response.")
        else:
            print("Fail -- Validated that the json value \"encounter\" was NOT present within the response.")

    @staticmethod
    def validate_empty_response_referral_post(data):
        if data['status_code'] == 400:
            print("Pass -- Validated that the request status code = 400")
        else:
            print("Fail -- Validated that the request status code != 400..\n The status code received was: " + str(
                data['status_code']) + " " + str(data['status_text']))

        if 'message' in data["response_json"]:
            print("Pass -- Validated that the json key \"message\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"message\" was NOT present within the response.")

        if 'Invalid Payload' in data["response_json"]["message"]:
            print("Pass -- Validated that the error message \"Invalid Payload\" was present within the response.")
        else:
            print("Fail -- Validated that the error message \"Invalid Payload\" was NOT present within the response.")

        if 'errors' in data["response_json"]:
            print("Pass -- Validated that the json key \"errors\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"errors\" was NOT present within the response.")

        if "Must not be empty" in data["response_json"]["errors"][0]["reason"]:
            print("Pass -- Validated that the reason field value \"Must not be empty\" matched the expected result.")
        else:
            print("Fail -- Validated that the reason field value \"Must not be empty\" did NOT match the expected result.")

        if "encounter" in data["response_json"]["errors"][0]["path"][2]:
            print("Pass -- Validated that the json value \"encounter\" was present within the response.")
        else:
            print("Fail -- Validated that the json value \"encounter\" was NOT present within the response.")

        if "response" in data["response_json"]["errors"][0]["path"][4]:
            print("Pass -- Validated that the json value \"response\" was present within the response.")
        else:
            print("Fail -- Validated that the json value \"response\" was NOT present within the response.")

    @staticmethod
    def validate_empty_given_name_referral_post(data):
        if data['status_code'] == 400:
            print("Pass -- Validated that the request status code = 400")
        else:
            print("Fail -- Validated that the request status code != 400..\n The status code received was: " + str(
                data['status_code']) + " " + str(data['status_text']))

        if 'message' in data["response_json"]:
            print("Pass -- Validated that the json key \"message\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"message\" was NOT present within the response.")

        if 'Invalid Payload' in data["response_json"]["message"]:
            print("Pass -- Validated that the error message \"Invalid Payload\" was present within the response.")
        else:
            print("Fail -- Validated that the error message \"Invalid Payload\" was NOT present within the response.")

        if 'errors' in data["response_json"]:
            print("Pass -- Validated that the json key \"errors\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"errors\" was NOT present within the response.")

        if "Must not be empty" in data["response_json"]["errors"][0]["reason"]:
            print("Pass -- Validated that the reason field value \"Must not be empty\" matched the expected result.")
        else:
            print("Fail -- Validated that the reason field value \"Must not be empty\" did NOT match the expected result.")

        if "name" in data["response_json"]["errors"][0]["path"][2]:
            print("Pass -- Validated that the json value \"name\" was present within the response.")
        else:
            print("Fail -- Validated that the json value \"name\" was NOT present within the response.")

        if "given" in data["response_json"]["errors"][0]["path"][4]:
            print("Pass -- Validated that the json value \"given\" was present within the response.")
        else:
            print("Fail -- Validated that the json value \"given\" was NOT present within the response.")

    @staticmethod
    def validate_empty_telecom_referral_post(data):
        if data['status_code'] == 400:
            print("Pass -- Validated that the request status code = 400")
        else:
            print("Fail -- Validated that the request status code != 400..\n The status code received was: " + str(
                data['status_code']) + " " + str(data['status_text']))

        if 'message' in data["response_json"]:
            print("Pass -- Validated that the json key \"message\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"message\" was NOT present within the response.")

        if 'Invalid Payload' in data["response_json"]["message"]:
            print("Pass -- Validated that the error message \"Invalid Payload\" was present within the response.")
        else:
            print("Fail -- Validated that the error message \"Invalid Payload\" was NOT present within the response.")

        if 'errors' in data["response_json"]:
            print("Pass -- Validated that the json key \"errors\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"errors\" was NOT present within the response.")

        if "Must not be empty" in data["response_json"]["errors"][0]["reason"]:
            print("Pass -- Validated that the reason field value \"Must not be empty\" matched the expected result.")
        else:
            print("Fail -- Validated that the reason field value \"Must not be empty\" did NOT match the expected result.")

        if "telecom" in data["response_json"]["errors"][0]["path"][2]:
            print("Pass -- Validated that the json value \"telecom\" was present within the response.")
        else:
            print("Fail -- Validated that the json value \"telecom\" was NOT present within the response.")

    @staticmethod
    def validate_empty_referral_post(data):
        if data['status_code'] == 400:
            print("Pass -- Validated that the request status code = 400")
        else:
            print("Fail -- Validated that the request status code != 400..\n The status code received was: " + str(
                data['status_code']) + " " + str(data['status_text']))

        if 'message' in data["response_json"]:
            print("Pass -- Validated that the json key \"message\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"message\" was NOT present within the response.")

        if 'Invalid Payload' in data["response_json"]["message"]:
            print("Pass -- Validated that the error message \"Invalid Payload\" was present within the response.")
        else:
            print("Fail -- Validated that the error message \"Invalid Payload\" was NOT present within the response.")

        if 'errors' in data["response_json"]:
            print("Pass -- Validated that the json key \"errors\" was present within the response.")
        else:
            print("Fail -- Validated that the json key \"errors\" was NOT present within the response.")

        if "Must not be empty" in data["response_json"]["errors"][0]["reason"]:
            print("Pass -- Validated that the reason field value \"Must not be empty\" matched the expected result.")
        else:
            print("Fail -- Validated that the reason field value \"Must not be empty\" did NOT match the expected result.")

    @staticmethod
    def validate_two_referral_post(data,site_data):
        if data['status_code'] == 202:
            print("Pass -- Validated that the request status code = 202")

            if len(data['response_json']["id"]) > 0:
                print("Pass -- Validated that the id of: " + str(data['response_json']["id"]) + " exists within the response data.")
            else:
                print("Fail -- Validated that the id does not exist within the response data.")

            if len(data["response_json"]["payload"]["referral"]) == 2:
                print("Pass -- Validated that the response data contains 2 referrals.")
            else:
                print("Fail -- Validated that the response data does NOT contain 2 referrals.")

            if data["response_json"]["payload"]["referral"][0]["subjectId"] in site_data["subjectId"]:
                print("Pass -- The primary subject id: " + str(data["response_json"]["payload"]["referral"][0]["subjectId"])
                      + " matches the primary subject id:  " + site_data["subjectId"] + " generated during the test.")
            else:
                print("Pass -- The primary subject id: " + str(data["response_json"]["payload"]["referral"][0]["subjectId"])
                      + " does NOT match the primary subject id:  " + site_data["subjectId"] + " generated during the test.")

            if data["response_json"]["payload"]["referral"][1]["subjectId"] in site_data["alternatesubjectId"]:
                print("Pass -- The alternate subject id: " + str(data["response_json"]["payload"]["referral"][0]["subjectId"])
                      + " matches the alternate subject id:  " + site_data["alternatesubjectId"] + " generated during the test.")
            else:
                print("Fail -- The alternate subject id: " + str(data["response_json"]["payload"]["referral"][0]["subjectId"])
                      + " does NOT match the alternate subject id:  " + site_data["alternatesubjectId"] + " generated during the test.")
        else:
            print("Fail -- Validated that the request status code != 202..\n The status code received was: " + str(
                data['status_code']) + " " + str(data['status_text']))


    @staticmethod
    def validate_referral_update(data,site_data):
        if data['status_code'] == 202:
            print("Pass -- Validated that the request status code = 202")

            if len(data['response_json']["id"]) > 0:
                print("Pass -- Validated that the id of: " + str(data['response_json']["id"]) + " exists within the response data.")
            else:
                print("Fail -- Validated that the id does not exist within the response data.")

            if data["response_json"]["subjectId"] in site_data["subjectId"]:
                print("Pass -- The primary subject id: " + str(data["response_json"]["subjectId"])
                      + " matches the primary subject id:  " + site_data["subjectId"] + " generated during the test.")
            else:
                print("Pass -- The primary subject id: " + str(data["response_json"]["subjectId"])
                      + " does NOT match the primary subject id:  " + site_data[
                          "subjectId"] + " generated during the test.")
        else:
            print("Fail -- Validated that the request status code != 202..\n The status code received was: " + str(
                data['status_code']) + " " + str(data['status_text']))


    @staticmethod
    def validate_rpi_reporting_events(data,site_data):
        if data['status_code'] == 200:
            print("Pass -- Validated that the request status code = 200")

            if len(data["response_json"]["pagination"]) > 0:
                print("Pass -- Validated that the response contains: " + str(len(data["response_json"]["pagination"])) + " \"pagination\" properties within it.")
            else:
                print("Fail -- Validated that the response does NOT contain \"pagination\" properties within it.")

            if len(data["response_json"]["events"]) > 0:
                print("Pass -- Validated that the response contains: " + str(len(data["response_json"]["events"])) + " \"events\" properties within it.")
            else:
                print("Fail -- Validated that the response does NOT contain \"events\" properties within it.")

            # Defined variables for total counts.
            v1patientType = 0
            nonv1patientType = 0
            trialId_match = 0
            nontrial_match = 0
            published_is_greater = 0
            collection_is_greater = 0
            for index, event in enumerate(data["response_json"]["events"]):
                if "v1.patient.created" in str(event["eventType"]):
                    v1patientType += 1
                else:
                    nonv1patientType += 1

                if site_data["trial_id"] in data["response_json"]["events"][index]["message"]["trialId"]:
                    trialId_match += 1
                else:
                    if len(site_data["alternate_sponsor_site_id"]) > 0:
                        if site_data["alternate_sponsor_site_id"] in data["response_json"]["events"][index]["message"]["trialId"]:
                            trialId_match += 1
                        else:
                            nontrial_match += 1
                if Utilities.is_publishedTime_greater_than_collectionTime(str(event["publishedTime"]),str(site_data["collection_start_time"])) == 1:
                    published_is_greater += 1
                else:
                    collection_is_greater += 1

            if nonv1patientType == 0:
                print("Pass -- Validated that all " + str(v1patientType) + " events had v1.patent.created events associated to them.")
            else:
                print("Fail -- Validated that: " + str(v1patientType) + " out of: " + str(v1patientType + nonv1patientType) + " events had v1.patent.created events associated to them.")

            if nontrial_match == 0:
                print("Pass -- Validated that all " + str(trialId_match) + " created events trialId's associated to them.")
            else:
                print("Fail -- Validated that: " + str(trialId_match) + " out of: " + str(trialId_match + nontrial_match) + " created events trialId's associated to them.")

            if collection_is_greater == 0:
                print("Pass -- Validated that all " + str(published_is_greater) + " published times were greater than the collection start times.")
            else:
                print("Fail -- Validated that: " + str(published_is_greater) + " out of: " + str(published_is_greater + collection_is_greater) + " published times were greater than the collection start times.")
        else:
            print("Fail -- Validated that the request status code != 200..\n The status code received was: " + str(
                data['status_code']) + " " + str(data['status_text']))


    @staticmethod
    def validate_rpi_reporting_events_with_limit(data):
        if data['status_code'] == 200:
            print("Pass -- Validated that the request status code = 200")
            if len(data["response_json"]["pagination"]) > 0:
                print("Pass -- Validated that the response contains: " + str(len(data["response_json"]["pagination"])) + " \"pagination\" properties within it.")

                if data["response_json"]["pagination"]["hasNextPage"] == True:
                    print("Pass -- Validated that the response contains \"hasNextPage\" properties within it.")
                else:
                    print("Fail -- Validated that the response does NOT contain \"hasNextPage\" properties within it.")
            else:
                print("Fail -- Validated that the response does NOT contain \"pagination\" properties within it.")

            if len(data["response_json"]["events"]) > 0:
                print("Pass -- Validated that the response contains \"events\" properties within it.")
                if len(data["response_json"]["events"]) == 1:
                    print("Pass -- Validated that the response contains: " + str(len(data["response_json"]["events"])) + " \"events\" properties within it.")
                else:
                    print("Fail -- Validated that the response contained: " + str(len(data["response_json"]["events"])) + " \"events\" properties within it. It should have only had 1.")
            else:
                print("Fail -- Validated that the response does NOT contain \"events\" properties within it.")

            if len(data["response_json"]["pagination"]['nextPage']) > 0:
                print("Pass -- Validated that the response contains \"nextPage\" properties within it.")
                if data["response_json"]["events"][0]["id"] in data["response_json"]["pagination"]['nextPage']:
                    print("Pass -- Validated that the \"eventId\" matches the \"nextPage id\" value.")
                else:
                    print("Fail -- Validated that the  \"eventId\" " + str(data["response_json"]["events"][0]["id"]) + " does NOT match the \"nextPage id\" " + str(data["response_json"]["pagination"]['nextPage']))
            else:
                print("Fail -- Validated that the response does NOT contain \"events\" properties within it.")

        else:
            print("Fail -- Validated that the request status code != 200..\n The status code received was: " + str(
                data['status_code']) + " " + str(data['status_text']))



    @staticmethod
    def get_pagination_url(data):
        if len(data["response_json"]["pagination"]["nextPage"]) > 0:
            return str(data["response_json"]["pagination"]["nextPage"])













