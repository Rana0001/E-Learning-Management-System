from home import *
import pytest


@pytest.fixture(scope="module")
def setup():
    print("<------------- Setup -------------->")
    db = sqlite3.connect("registration.db")
    yield db
    print("<------------- Teardown -------------->")
    db.close()


# @pytest.mark.parametrize("user,password", [("root","root"), ("abc", "abc"), ("1654", "546")])
def test_login(setup):
    db = show_login_result("123456", "123456")
    assert db == "Pass"
    # assert False


def test_check_first(setup):
    db = show_login_result("root", "root")
    assert db == "Pass"


def test_check_second(setup):
    db = show_login_result("1535", "8545")
    if db == "Pass":
        assert True
    else:
        raise ValueError("Please! Enter Correct Username and Password")


def test_insert_data(setup):
    db = data_insert("Prashant", "Rana", "hello", "123")
    assert db == None
