from assertpy import assert_that
from api_requests.requests_builder import RequestsBuilder
from http import HTTPStatus
import helpers.environment_urls  as urls


def test_users_status_with_init(users_list_response):
    req_builder = RequestsBuilder(urls.USERS_URL_WITH_ENV)
    req_builder.validate_status_code(users_list_response, HTTPStatus.OK)


def test_users_status_with_fixture(users_list_with_init):
    response = users_list_with_init.execute_get_request()
    users_list_with_init.validate_status_code(response, HTTPStatus.OK)


def test_users_response_ok(users_list_response):
    assert_that(users_list_response.ok).is_true()


def test_users_response_reason(users_list_response):
    assert_that(users_list_response.reason).is_equal_to('OK')