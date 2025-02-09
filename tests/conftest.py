import pytest
from api_requests.requests_builder import RequestsBuilder
from helpers.environment_urls import USERS_URL


@pytest.fixture
def users_list_response():
    req_builder = RequestsBuilder(USERS_URL)
    return req_builder.execute_get_request()

@pytest.fixture
def users_list_with_init():
    return RequestsBuilder("https://reqres.in/api/users?page=2")