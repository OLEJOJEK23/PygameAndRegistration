import pytest
from src.Inteface import login_check


@pytest.mark.parametrize(
    "login, password, result",
    [
        ('test', 'test', True)
    ]
)
def test_login_check(login: str, password: str, result: bool):
    assert login_check(login, password) == result
