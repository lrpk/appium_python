import time

import pytest

from utils.settings import EMAIL, PASSWORD


@pytest.mark.parametrize("email, password", [('invalid_email', 'invalid_pass'), (EMAIL, PASSWORD)])
def test_user_login(user_login_fixture, email, password):

    user_login_fixture.login_btn()

    time.sleep(4)

    user_login_fixture.input_email(email)
    user_login_fixture.input_password(password)

    user_login_fixture.login_btn()


def test_login_btn(user_login_fixture):
    user_login_fixture.login_btn()
