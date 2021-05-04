import json

class RPIPayloads(object):

    @staticmethod
    def get_empty_payload():
        """
        This method generates an empty value to be used within the headers portion of a Python request.
        Using this can force an error to occur within the request response.
        """
        json_data = ''
        return json_data

    @staticmethod
    def get_400_payload():
        """
        This method will return an empty dictionary object that can be used in GET requests or to generate
        404 errors within the request response.
        :return: an empty dictionary object
        """
        json_data = {}
        return json_data

    @staticmethod
    def get_empty_dict_payload():
        """
        This method will return an empty dictionary object that can be used in GET requests.
        :return: an empty dictionary object
        """
        json_data = {}
        return json_data

    @staticmethod
    def create_payload_for_access_token(client_id, client_secret, grant_type, realm, audience):
        """
        Method creates the payload necessary to get bearer access token. The payload generated
        is ideal to be sent with the application/json content_type
        Returns :class:`Dictionary <Dictionary>` object.

        :param client_id: The client id of the app
        :param client_secret: Client secret for the app (can be retrieved like client_id)
        :param grant_type: Client Credentials, Authorization Code, Implicit, and Resource Owner Credentials
        :param realm: The directory or subsection of Auth0 that we are requesting the information from
        :param audience: The api that we are requesting access to
        """
        data = {}
        data.update(client_id=client_id)
        data.update(client_secret=client_secret)
        data.update(grant_type=grant_type)
        data.update(realm=realm)
        data.update(audience=audience)
        return data

    @staticmethod
    def get_referral_payload(subject_id,trial_id,sponsor_site_id):
        """
        This method is used within most generic referral request payloads. We insert the values needed in order to
        process the request.
        :param subject_id:
        :param trial_id:
        :param sponsor_site_id:
        :return: json object used as the data portion of the requests request.
        """
        json_data = """{"referral": [
                {
                "consent": {
                    "verification": {
                    "verificationDate": "2020-04-19T09:45:00Z",
                    "verified": true,
                    "verifiedWith": {
                        "name": "self",
                        "relationship": "ONESELF"
                    }
                },
                "text": "Agrees to site contact."
                },
                    "subjectId":""" + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueString": "42"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_maximal(subject_id,trial_id,sponsor_site_id):
        """
        This method is used within most generic referral request payloads. We insert the values needed in order to
        process the request.
        :param subject_id:
        :param trial_id:
        :param sponsor_site_id:
        :return: json object used as the data portion of the requests request.
        """

        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId":""" + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "gender": "male",
                    "sex": "intersex",
                    "address": [
                        {
                            "country": "us",
                            "city": "Citiville",
                            "district": "Countyton",
                            "postalCode": "111111",
                            "text": "Near the tree",
                            "line": [
                                "100 Street st"
                            ],
                            "type": "both",
                            "use": "home",
                            "state": "ST"
                        }
                    ],
                    "name": [
                        {
                            "use": "official",
                            "text": "Sammy",
                            "given": [
                                "Samuel"
                            ],
                            "suffix": [
                                "Jr"
                            ],
                            "prefix": [
                                "Sir"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com",
                            "rank": 1,
                            "period": {
                                "start": "2019-10-30T02:08:18Z",
                                "end": "2019-10-30T02:08:19Z"
                            }
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "definition": "google.com",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueString": "42"
                                            },
                                            {
                                                "valueString": "42"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_multi_trial(subject_id,trial_id,sponsor_site_id,alternate_trial_id,alternate_sponsor_site_id):
        """
        This method is used within multi trial referral request payloads. We insert the values within the json in order to
        process the request.
        Note that there alternate values for both trial and sponsor sites.
        :param subject_id:
        :param trial_id:
        :param sponsor_site_id:
        :param alternate_trial_id
        :param alternate_sponsor_site_id
        :return: json object used as the data portion of the requests request.
        """
        json_data = """ {"referral": [
                {
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "alternateTrials": [{
                        "id": """ + f'"{alternate_trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{alternate_sponsor_site_id}"' + """
                    }],
                    "birthDate": "2019-09-27",
                    "gender": "male",
                    "address": [
                        {
                            "country": "us",
                            "city": "Citiville",
                            "district": "Countyton",
                            "postalCode": "111111",
                            "text": "Near the tree",
                            "line": [
                                "100 Street st"
                            ],
                            "type": "both",
                            "use": "home",
                            "state": "ST"
                        }
                    ],
                    "name": [
                        {
                            "use": "official",
                            "text": "Sammy",
                            "given": [
                                "Samuel"
                            ],
                            "suffix": [
                                "Jr"
                            ],
                            "prefix": [
                                "Sir"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com",
                            "rank": 1,
                            "period": {
                                "start": "2019-10-30T02:08:18Z",
                                "end": "2019-10-30T02:08:19Z"
                            }
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "definition": "google.com",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueString": "42"
                                            },
                                            {
                                                "valueString": "42"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_minimal(subject_id,trial_id,sponsor_site_id):
        """
        This method is the same as others but only passes the minimum amount of json to the request
        :param subject_id:
        :param trial_id:
        :param sponsor_site_id:
        :return: json object used as the data portion of the requests request.
        """
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueString": "42"
                                            },
                                            {
                                                "valueString": "42"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_blank_address_text(subject_id,trial_id,sponsor_site_id):
        """
        This method will populate
        :param subject_id:
        :param trial_id:
        :param sponsor_site_id:
        :return: json object used as the data portion of the requests request.
        """
        json_data = """{
                "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "address": [
                        {
                            "country": "us",
                            "city": "Citiville",
                            "district": "Countyton",
                            "postalCode": "111111",
                            "text": "",
                            "line": [
                                "100 Street st"
                            ],
                            "type": "both",
                            "use": "home",
                            "state": "ST"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueString": "42"
                                            },
                                            {
                                                "valueString": "42"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_bad_site_id(subject_id,trial_id,sponsor_site_id):
        """
        This method in identical to others but the siteId that gets passed to the json is incorrect.
        :param subject_id:
        :param trial_id:
        :param sponsor_site_id:
        :return: json object used as the data portion of the requests request.
        """
        json_data = """ {
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueString": "42"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_bad_trial_id(subject_id, bad_trial_id, sponsor_site_id):
        """
        This method in identical to others but the trial_Id that gets passed to the json is incorrect.
        :param subject_id:
        :param bad_trial_id:
        :param sponsor_site_id:
        :return: json object used as the data portion of the requests request.
        """
        json_data = """ {
                "referral": [
                    {
                        "consent": {
                            "verification": {
                                "verificationDate": "2020-04-19T09:45:00Z",
                                "verified": true,
                                "verifiedWith": {
                                    "name": "self",
                                    "relationship": "ONESELF"
                                }
                            },
                            "text": "Agrees to site contact."
                        },
                        "subjectId": """ + f'"{subject_id}"' + """,
                        "subjectCreatedAt": "2019-10-30T02:08:18Z",
                        "campaignCode": "FB123456",
                        "primaryTrial": {
                            "id": """ + f'"{bad_trial_id}"' + """,
                            "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                        },
                        "birthDate": "2019-09-27",
                        "name": [
                            {
                                "use": "official",
                                "given": [
                                    "Samuel"
                                ],
                                "family": "Norton"
                            }
                        ],
                        "telecom": [
                            {
                                "use": "home",
                                "system": "email",
                                "value": "samuel.norton@organization.com"
                            }
                        ],
                        "encounter": [
                            {
                                "source": "web",
                                "response": {
                                    "item": [
                                        {
                                            "linkId": "1",
                                            "text": "What is the answer to life?",
                                            "answer": [
                                                {
                                                    "valueString": "42"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                ]
            }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_bad_alternate_trial_id(subject_id, trial_id, sponsor_site_id, bad_alternate_trial_id, alternate_sponsor_site_id):
        """
        This method in identical to others but the alternate_trial_Id that gets passed to the json is incorrect.
        :param subject_id:
        :param trial_id:
        :param sponsor_site_id:
        :param bad_alternate_trial_id:
        :param alternate_sponsor_site_id:
        :return: json object used as the data portion of the requests request.
        """
        json_data = """ {"referral": [
                    {
                        "subjectId": """ + f'"{subject_id}"' + """,
                        "subjectCreatedAt": "2019-10-30T02:08:18Z",
                        "campaignCode": "FB123456",
                        "primaryTrial": {
                            "id": """ + f'"{trial_id}"' + """,
                            "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                        },
                        "alternateTrials": [{
                            "id": """ + f'"{bad_alternate_trial_id}"' + """,
                            "sponsorSiteId": """ + f'"{alternate_sponsor_site_id}"' + """
                        }],
                        "birthDate": "2019-09-27",
                        "gender": "male",
                        "address": [
                            {
                                "country": "us",
                                "city": "Citiville",
                                "district": "Countyton",
                                "postalCode": "111111",
                                "text": "Near the tree",
                                "line": [
                                    "100 Street st"
                                ],
                                "type": "both",
                                "use": "home",
                                "state": "ST"
                            }
                        ],
                        "name": [
                            {
                                "use": "official",
                                "text": "Sammy",
                                "given": [
                                    "Samuel"
                                ],
                                "suffix": [
                                    "Jr"
                                ],
                                "prefix": [
                                    "Sir"
                                ],
                                "family": "Norton"
                            }
                        ],
                        "telecom": [
                            {
                                "use": "home",
                                "system": "email",
                                "value": "samuel.norton@organization.com",
                                "rank": 1,
                                "period": {
                                    "start": "2019-10-30T02:08:18Z",
                                    "end": "2019-10-30T02:08:19Z"
                                }
                            }
                        ],
                        "encounter": [
                            {
                                "source": "web",
                                "response": {
                                    "item": [
                                        {
                                            "linkId": "1",
                                            "definition": "google.com",
                                            "text": "What is the answer to life?",
                                            "answer": [
                                                {
                                                    "valueString": "42"
                                                },
                                                {
                                                    "valueString": "42"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                ]
            }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_integer_answer_value(subject_id, trial_id, sponsor_site_id):
        """
        This method passes json data that contain an answer that is defined as an Integer i.e "valueInteger": 1
        :param subject_id:
        :param trial_id:
        :param sponsor_site_id:
        :return: json object used as the data portion of the requests request.
        """
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId":""" + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId":  """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueInteger": 1
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_uri_value(subject_id, trial_id, sponsor_site_id):
        """
        This method passes json data that contain an answer that is defined as an "valueUri": "www.studyteamapp.com"
        :param subject_id:
        :param trial_id:
        :param sponsor_site_id:
        :return: json object used as the data portion of the requests request.
        """
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId":""" + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id":""" + f'"{trial_id}"' + """,
                        "sponsorSiteId":  """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueUri": "www.studyteamapp.com"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_bad_link_id_value(subject_id, trial_id, sponsor_site_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId":""" + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId":  """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "no-text-no-answer"
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_boolean_value(subject_id, trial_id, sponsor_site_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId":""" + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId":   """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                               "valueBoolean": true
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_coding_value(subject_id, trial_id, sponsor_site_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId":""" + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId":  """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueCoding": {
                                                    "userSelected": true,
                                                    "display": "display",
                                                    "code": "code",
                                                    "version": "version",
                                                    "system": "system"
                                                }
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_decimal_value(subject_id, trial_id, sponsor_site_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId":""" + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id":""" + f'"{trial_id}"' + """,
                        "sponsorSiteId":  """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueDecimal": 1.000000000000001
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_text_value(subject_id, trial_id, sponsor_site_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id":""" + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueString": "42"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_time_value(subject_id, trial_id, sponsor_site_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id":""" + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueTime": "02:08:18"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_time_and_date(subject_id, trial_id, sponsor_site_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId":  """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id":""" + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueDatetime": "2019-10-30T02:08:18Z"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_date(subject_id, trial_id, sponsor_site_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id":""" + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueDate": "2019-10-30"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_bad_email(subject_id, trial_id, sponsor_site_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "bad@example"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueString": "42"
                                            },
                                            {
                                                "valueString": "42"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_bad_coding(subject_id, trial_id, sponsor_site_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueCoding": {}
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_bad_source(subject_id, trial_id, sponsor_site_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "other",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueString": "42"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_empty_answer(subject_id, trial_id, sponsor_site_id):
        json_data ="""{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id":""" + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "other",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_bad_response(subject_id, trial_id, sponsor_site_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id":""" + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1"
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_empty_telecom_period(subject_id, trial_id, sponsor_site_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com",
                            "rank": 1,
                            "period": {}
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueString": "42"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_empty_line(subject_id, trial_id, sponsor_site_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "address": [
                        {
                            "country": "us",
                            "city": "Citiville",
                            "district": "Countyton",
                            "postalCode": "111111",
                            "text": "Near the tree",
                            "line": [],
                            "type": "both",
                            "use": "home",
                            "state": "ST"
                        }
                    ],
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com",
                            "rank": 1
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueString": "42"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_empty_address(subject_id, trial_id, sponsor_site_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "address": [],
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com",
                            "rank": 1
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueString": "42"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_empty_alternate_trial_ids(subject_id, trial_id, sponsor_site_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "alternateTrials": [],
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueString": "42"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_empty_encounters(subject_id, trial_id, sponsor_site_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": []
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_empty_response_item(subject_id, trial_id, sponsor_site_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_empty_given_name(subject_id, trial_id, sponsor_site_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": []
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueString": "42"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_empty_telecom(subject_id, trial_id, sponsor_site_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {}
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueString": "42"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_empty_referral_payload():
        json_data = """{}"""
        
        
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_empty_referral():
        json_data = """{"referral": []} """
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_with_two_referrals(subject_id, trial_id, sponsor_site_id,alternative_subject_id):
        json_data = """{
            "referral": [
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "Samuel"
                            ],
                            "family": "Norton"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "samuel.norton@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueString": "42"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                },
                {
                    "consent": {
                        "verification": {
                            "verificationDate": "2020-04-19T09:45:00Z",
                            "verified": true,
                            "verifiedWith": {
                                "name": "self",
                                "relationship": "ONESELF"
                            }
                        },
                        "text": "Agrees to site contact."
                    },
                    "subjectId": """ + f'"{alternative_subject_id}"' + """,
                    "subjectCreatedAt": "2019-10-30T02:08:18Z",
                    "campaignCode": "FB123456",
                    "primaryTrial": {
                        "id": """ + f'"{trial_id}"' + """,
                        "sponsorSiteId": """ + f'"{sponsor_site_id}"' + """
                    },
                    "birthDate": "2019-09-27",
                    "name": [
                        {
                            "use": "official",
                            "given": [
                                "John"
                            ],
                            "family": "Doe"
                        }
                    ],
                    "telecom": [
                        {
                            "use": "home",
                            "system": "email",
                            "value": "john@organization.com"
                        }
                    ],
                    "encounter": [
                        {
                            "source": "web",
                            "response": {
                                "item": [
                                    {
                                        "linkId": "1",
                                        "text": "What is the answer to life?",
                                        "answer": [
                                            {
                                                "valueString": "42"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_update_subject():
        json_data = """{
            "birthDate": "2019-09-27",
            "name": [
                {
                    "use": "official",
                    "given": [
                        "not",
                        "Samuel"
                    ],
                    "family": "Norton"
                }
            ],
            "telecom": [
                {
                    "use": "home",
                    "system": "email",
                    "value": "samuel.norton@organization.com"
                }
            ],
            "sex": "female",
            "encounter": [
                {
                    "source": "web",
                    "response": {
                        "item": [
                            {
                                "linkId": "1",
                                "text": "What is the answer to life?",
                                "answer": [
                                    {
                                        "valueString": "42"
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_update_subject_blank_address_text():
        json_data = """{
            "birthDate": "2019-09-27",
            "name": [
                {
                    "use": "official",
                    "given": [
                        "not",
                        "Samuel"
                    ],
                    "family": "Norton"
                }
            ],
            "address": [
                {
                    "country": "us",
                    "city": "Huntington",
                    "district": "Suffolk",
                    "postalCode": "11746",
                    "text": "near that church",
                    "line": [
                        "34 Foxhurst Road"
                    ],
                    "type": "both",
                    "use": "home",
                    "state": "NY"
                }
            ],
            "telecom": [
                {
                    "use": "home",
                    "system": "email",
                    "value": "samuel.norton@organization.com"
                }
            ],
            "sex": "female",
            "encounter": [
                {
                    "source": "web",
                    "response": {
                        "item": [
                            {
                                "linkId": "1",
                                "text": "What is the answer to life?",
                                "answer": [
                                    {
                                        "valueString": "42"
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_update_subject_401():
        json_data = """{
            "birthDate": "2019-09-27",
            "name": [
                {
                    "use": "official",
                    "given": [
                        "not",
                        "Samuel"
                    ],
                    "family": "Norton"
                }
            ],
            "telecom": [
                {
                    "use": "home",
                    "system": "email",
                    "value": "samuel.norton@organization.com"
                }
            ],
            "sex": "female",
            "encounter": [
                {
                    "source": "web",
                    "response": {
                        "item": [
                            {
                                "linkId": "1",
                                "text": "What is the answer to life?",
                                "answer": [
                                    {
                                        "valueString": "42"
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_update_subject_empty():
        json_data = """{}"""
        
        
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_update_subject_empty_encounter():
        json_data = """{
            "birthDate": "2019-09-27",
            "name": [
                {
                    "use": "official",
                    "given": [
                        "not",
                        "Samuel"
                    ],
                    "family": "Norton"
                }
            ],
            "telecom": [
                {
                    "use": "home",
                    "system": "email",
                    "value": "samuel.norton@organization.com"
                }
            ],
            "encounter": []
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_update_subject_bad_subject_id():
        json_data = """{
            "birthDate": "2019-09-27",
            "name": [
                {
                    "use": "official",
                    "given": [
                        "not",
                        "Samuel"
                    ],
                    "family": "Norton"
                }
            ],
            "telecom": [
                {
                    "use": "home",
                    "system": "email",
                    "value": "samuel.norton@organization.com"
                }
            ],
            "encounter": [
                {
                    "source": "web",
                    "response": {
                        "item": [
                            {
                                "linkId": "1",
                                "text": "What is the answer to life?",
                                "answer": [
                                    {
                                        "valueString": "42"
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))

    @staticmethod
    def get_referral_payload_update_subject_bad_site_id():
        json_data = """{
            "birthDate": "2019-09-27",
            "name": [
                {
                    "use": "official",
                    "given": [
                        "not",
                        "Samuel"
                    ],
                    "family": "Norton"
                }
            ],
            "telecom": [
                {
                    "use": "home",
                    "system": "email",
                    "value": "samuel.norton@organization.com"
                }
            ],
            "encounter": [
                {
                    "source": "web",
                    "response": {
                        "item": [
                            {
                                "linkId": "1",
                                "text": "What is the answer to life?",
                                "answer": [
                                    {
                                        "valueString": "42"
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        }"""
        return json.dumps(json.loads(json_data))