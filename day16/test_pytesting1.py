# from pytesting1 import get_weather
# from pytesting1 import add, divide
from pytesting1 import UserManager
import pytest


# 1st
# def test_get_weather():
#     assert get_weather(25) == "Hot"
#     assert get_weather(10) == "Cold"


# 2nd
# def test_add():
#     assert add(2, 3) == 5
#     assert add(-1, 5) == 4
#     assert add(0, 0) == 0


# def test_divide():
#     with pytest.raises(ValueError, match="Cannot divide by zero"):
#         divide(10, 0)


# 3rd
@pytest.fixture
def user_manager():
    """Creates a fresh instance of UserManager before each test."""
    return UserManager()
# user_manager = UserManager()


def test_add_user(user_manager):
    assert user_manager.add_user("John doe", "john@example.com") == True
    assert user_manager.get_user("John doe") == "john@example.com"


def test__add_duplicate_user(user_manager):
    user_manager.add_user("John doe", "john@example.com")
    with pytest.raises(ValueError):
        user_manager.add_user("John doe", "another@example.com")
