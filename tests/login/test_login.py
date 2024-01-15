import time

import pytest

from utils.settings import EMAIL, PASSWORD


@pytest.mark.parametrize("email, password",
                         [
                             ('invalid_email', 'invalid_pass'),
                             (EMAIL, PASSWORD)
                         ]
                         )
def test_user_login(user_login_fixture, email, password):

    # перехід на стронку з формою
    user_login_fixture.login_btn()

    # очікування зникнення банера про помилку
    time.sleep(4)

    # передача даних в форму
    user_login_fixture.input_email(email)
    user_login_fixture.input_password(password)

    # підтвердження форми
    user_login_fixture.login_btn()


# працездатність кнопки входу
def test_login_btn(user_login_fixture):
    user_login_fixture.login_btn()
