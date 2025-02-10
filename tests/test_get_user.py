from http import HTTPStatus

from assertpy import assert_that


def test_user_validation(actual_user_response, expected_user_response):
    assert_that(actual_user_response.status_code).is_equal_to(HTTPStatus.OK)
    assert_that(actual_user_response.json()).is_equal_to(expected_user_response.to_dict())


