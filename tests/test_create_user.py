from http import HTTPStatus

from assertpy import assert_that

from api_requests.requests_builder import RequestsBuilder
from helpers.environment_urls import CREATE_USER_URL


def test_user_creation(created_new_random_user_dto):
    request = created_new_random_user_dto
    actual_response = RequestsBuilder(CREATE_USER_URL).execute_post_request(request.to_dict())
    assert_that(actual_response.status_code).is_equal_to(HTTPStatus.CREATED)
    assert_that(actual_response.json()).contains_entry({"name": request.get_name()})
    assert_that(actual_response.json()).contains_entry({"job": request.get_job()})
    assert_that(actual_response.json()["createdAt"]).matches(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z")
    assert_that(actual_response.json()["id"]).is_not_none()
