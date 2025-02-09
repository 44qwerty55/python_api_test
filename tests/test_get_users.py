import requests
from assertpy import assert_that
import pytest
import helpers.environment_urls as urls

@pytest.fixture(scope="module")
def users_list_response():
    response = requests.get(urls.USERS_URL_WITH_ENV)
    return response


def test_users_status(users_list_response):
    assert users_list_response.status_code == 200
    assert_that(users_list_response.status_code == 200).is_true()
    assert_that(users_list_response.status_code).is_equal_to(200)


def test_users_response_ok(users_list_response):
    assert_that(users_list_response.ok).is_true()


def test_users_response_reason(users_list_response):
    assert_that(users_list_response.reason).is_equal_to('OK')