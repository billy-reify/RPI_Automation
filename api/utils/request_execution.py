import requests

class ExecuteRPIRequests(object):

    @staticmethod
    def execute_rpi_api_call(method,url,headers,data):
        response = {}
        res = requests.request(method=method, url=url, headers=headers, data=data)
        response['status_code'] = res.status_code
        response['status_text'] = res.text
        if len(res.json()) > 0:
            response['response_json'] = res.json()
        else:
            response['response_json'] = '{}'
        return response

#     Need to add error handling that will allow 200\202\401\404 specific errors



