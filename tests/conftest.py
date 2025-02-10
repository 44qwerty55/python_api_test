import os

import pytest
import json

from api_dto.user_response import *
from api_dto.users_response import UsersResponse
from api_requests.requests_builder import RequestsBuilder
from helpers.environment_urls import USERS_URL, USER_URL

base_path = os.path.dirname(__file__)

@pytest.fixture
def actual_user_response():
    req_builder = RequestsBuilder(USER_URL)
    return req_builder.execute_get_request()

@pytest.fixture
def actual_users_response():
    req_builder = RequestsBuilder(USERS_URL)
    return req_builder.execute_get_request()

@pytest.fixture
def expected_user_response():
    file_path = os.path.join(base_path, '../data_jsons/user_response_data.json')
    with open(file_path, 'r') as file:
        data_json_from_file = json.load(file)
        return UserResponse.from_json(data_json_from_file)

@pytest.fixture
def expected_users_response():
    file_path = os.path.join(base_path, '../data_jsons/users_response_data.json')
    with open(file_path, 'r') as file:
        data_json_from_file = json.load(file)
        return UsersResponse.from_json(data_json_from_file)
