from http import HTTPStatus

from assertpy import assert_that


def test_users_validation(actual_get_users_response, expected_users_response):
    assert_that(actual_get_users_response.status_code).is_equal_to(HTTPStatus.OK)
    assert_that(actual_get_users_response.json()).is_equal_to(expected_users_response.to_dict())
