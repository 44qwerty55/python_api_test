from http import HTTPStatus

from assertpy import assert_that

from api_dto.user_create_or_update_request import UserRequest
from api_requests.requests_builder import RequestsBuilder
from helpers.environment_urls import USER_URL


def test_user_update(create_user):
    request = UserRequest(create_user.json().get('name'), create_user.json().get('job'))
    actual_response =  RequestsBuilder(USER_URL).execute_put_request(request.to_dict())
    assert_that(actual_response.status_code).is_equal_to(HTTPStatus.OK)
    assert_that(actual_response.json()).contains_entry({"name": request.get_name()})
    assert_that(actual_response.json()).contains_entry({"job": request.get_job()})
    assert_that(actual_response.json()["updatedAt"]).matches(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z")