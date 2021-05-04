

class RPIConnectionProperties(object):
    @staticmethod
    def get_connection_properties(environment):
        connection_data = {'base_url': 'https://' + environment + '.api.studyteamapp.com',
                           'audience': 'https://' + environment + '.api.studyteamapp.com/api/rvi',
                           'grant_type': 'client_credentials',
                           'realm': 'Vendor',
                           'client_id': 'qYNAyXVOl8aFW3I2OPuwxiY84sMIvFCn',
                           'client_secret': '6gnDeAcUSFx0f6MS6FIBfRpOMWQNs3YxnIdPK6ix_eoDH2xoOw7BQXkgKNgywAgi'
                           }
        return connection_data

