
class RPIEndPointConstants:
    sites = '/rpi/sites'
    reporting_events = '/rpi/events?'
    base_url = 'https://testing.api.studyteamapp.com'

class RPIApiUrls(object):
    @staticmethod
    def get_authentication_url(environment):
        return 'https://' + environment + '.api.studyteamapp.com/oauth/token'

    @staticmethod
    def get_sites():
        return RPIEndPointConstants.base_url + RPIEndPointConstants.sites

    @staticmethod
    def get_sites_by_site_id(site_id):
        return RPIEndPointConstants.base_url + RPIEndPointConstants.sites + "/" + site_id

    @staticmethod
    def get_referral_by_site_id(site_id):
        return RPIEndPointConstants.base_url + RPIEndPointConstants.sites + "/" + site_id + "/referrals"

    @staticmethod
    def set_referral_subject_by_site_id_and_subject_id(site_id,subject_id):
        return RPIEndPointConstants.base_url + RPIEndPointConstants.sites + "/" + site_id + "/referrals/subjects/" + subject_id

    @staticmethod
    def get_reporting_events_by_collection_start_date(collection_start_time):
        return RPIEndPointConstants.base_url + RPIEndPointConstants.reporting_events + 'eventTypes=v1.patient.created&since=' + collection_start_time

    @staticmethod
    def get_reporting_events_by_collection_start_date_with_limit(collection_start_time):
        return RPIEndPointConstants.base_url + RPIEndPointConstants.reporting_events + 'eventTypes=v1.patient.created&limit=1&since=' + collection_start_time

    @staticmethod
    def get_reporting_events_pagination(pagination_url):
        return pagination_url

    @staticmethod
    def get_reporting_events_by_collection_start_date_and_trial_id(collection_start_time,alternate_trial_id):
        return RPIEndPointConstants.base_url + RPIEndPointConstants.reporting_events + 'eventTypes=v1.patient.created&since=' + collection_start_time + "&trialids=" + alternate_trial_id

    @staticmethod
    def get_reporting_events_with_bad_event():
        return RPIEndPointConstants.base_url + RPIEndPointConstants.reporting_events + 'eventTypes=foobar'

    @staticmethod
    def get_reporting_events_with_no_event(collection_start_time):
        return RPIEndPointConstants.base_url + RPIEndPointConstants.reporting_events + 'since=' + collection_start_time

    @staticmethod
    def get_reporting_events_by_with_bad_trial_id():
        return RPIEndPointConstants.base_url + RPIEndPointConstants.reporting_events + 'eventTypes=v1.patient.created&trialIds=foobar'

    @staticmethod
    def set_sites_401():
        return RPIEndPointConstants.base_url + RPIEndPointConstants.sites

    @staticmethod
    def set_sites_404():
        return RPIEndPointConstants.base_url + RPIEndPointConstants.sites + '/404'


class RPIApiHeaders(object):

    @staticmethod
    def get_401_header():
        headers = {}
        return headers

    @staticmethod
    def get_auth_header(auth_token):
        headers = {
            'Authorization': 'Bearer ' + auth_token
        }
        return headers

    @staticmethod
    def get_token_header():
        headers = {
            'content_type': 'application/json'
        }
        return headers

    @staticmethod
    def get_referral_auth_header(auth_token):
        headers = {'content_type': 'application/json',
                   'Authorization': 'Bearer ' + auth_token}
        return headers

    @staticmethod
    def get_update_auth_header(auth_token):
        headers = {'content_type': 'application/json',
                   'Authorization': 'Bearer ' + auth_token}
        return headers