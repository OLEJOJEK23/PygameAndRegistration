import pytest
from src.Inteface import login_check, create_new_user
from pathlib import Path
import os


@pytest.mark.parametrize(
    "login, password, result, path",
    [
        ('test', 'test', True, os.path.abspath(os.path.join(os.path.abspath(os.getcwd()),'..'))),
        ('test', 'test1', False, os.path.abspath(os.path.join(os.path.abspath(os.getcwd()),'..'))),
        ('test1234', 'test', False, os.path.abspath(os.path.join(os.path.abspath(os.getcwd()),'..'))),
        ('test1234', 'test12312', False, os.path.abspath(os.path.join(os.path.abspath(os.getcwd()),'..')))
    ]
)
def test_login_check(login: str, password: str, result: bool, path):
    assert login_check(login, password, path) == result


@pytest.mark.parametrize(
    "password, login, name, surname, result, path",
    [
        ('test1', 'test2', 'test3', 'test4', True, os.path.abspath(os.path.join(os.path.abspath(os.getcwd()),'..'))),
        ('test', 'test2', 'test3', 'test4', False, os.path.abspath(os.path.join(os.path.abspath(os.getcwd()),'..')))
    ]
)
def test_new_user_creating_file(password: str, login: str, name: str, surname: str, result: bool, path: str):
    files_before = len(list(Path(os.path.abspath(os.path.join(os.path.abspath(os.getcwd()), '..') + f"\\users")).iterdir()))
    create_new_user(password, login, name, surname, path)
    files_after = len(list(Path(os.path.abspath(os.path.join(os.path.abspath(os.getcwd()), '..') + f"\\users")).iterdir()))
    assert (files_before < files_after) == result


