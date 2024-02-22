from http import HTTPStatus

import pytest

from GitApiTest.assertions.assertion_base import assert_status_code, assert_response_body_fields
from GitApiTest.main import get_user_info, get_user_repo_list, get_user_followers


class Test:

    @pytest.mark.parametrize("username", ["Strawlll"])
    def test_get_user(self, username, request):
        response = get_user_info(username)
        assert_status_code(response, HTTPStatus.OK)
        assert_response_body_fields(request, response)

    @pytest.mark.parametrize("username", [""])
    def test_get_empty_user(self, username):
        response = get_user_info(username)
        assert_status_code(response, HTTPStatus.NOT_FOUND)

    @pytest.mark.parametrize("username", ["Strawlll"])
    def test_get_repo_list(self, username, request):
        response = get_user_repo_list(username)
        assert_status_code(response, HTTPStatus.OK)
        assert_response_body_fields(request, response, rmv_ids=False, fields_to_ignore=["description", "permissions"])

    @pytest.mark.parametrize("username", ["Strawlll"])
    def test_get_followers(self, username, request):
        response = get_user_followers(username)
        assert_status_code(response, HTTPStatus.OK)
        assert_response_body_fields(request, response, rmv_ids=False)
