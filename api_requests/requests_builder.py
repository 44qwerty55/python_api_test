import requests
from assertpy import assert_that

class RequestsBuilder:

    def __init__(self, url: str):
        self.url = url


    def execute_get_request(self):
        return requests.get(self.url)


    def validate_status_code(self, response: requests.Response, status_code: int):
        assert_that(response.status_code).is_equal_to(status_code)


    def validate_reason(self, response: requests.Response, reason: str):
        assert_that(response.reason).is_equal_to(reason)