import os
import uuid
from http import HTTPStatus

import pytest
import json

from assertpy import assert_that

from api_dto.user_create_or_update_request import UserRequest
from api_dto.user_response import *
from api_dto.users_response import UsersResponse
from api_requests.requests_builder import RequestsBuilder
from helpers.environment_urls import LIST_USERS_URL, USER_URL, CREATE_USER_URL

base_path = os.path.dirname(__file__)

@pytest.fixture
def actual_get_user_response():
    req_builder = RequestsBuilder(USER_URL)
    return req_builder.execute_get_request()

@pytest.fixture
def actual_get_users_response():
    req_builder = RequestsBuilder(LIST_USERS_URL)
    return req_builder.execute_get_request()

@pytest.fixture
def actual_post_user_response(request):
    user_request = request.param
    req_builder = RequestsBuilder(USER_URL)
    return req_builder.execute_post_request(user_request)

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

@pytest.fixture
def create_user(created_new_random_user_dto):
    req_builder = RequestsBuilder(CREATE_USER_URL)
    response = req_builder.execute_post_request(created_new_random_user_dto.to_dict())
    assert_that(response.status_code).is_equal_to(HTTPStatus.CREATED)
    return response

@pytest.fixture()
def created_new_random_user_dto():
    name = f"name_{uuid.uuid4().hex}"
    job = f"job_{uuid.uuid4().hex}"
    return UserRequest(name, job)


