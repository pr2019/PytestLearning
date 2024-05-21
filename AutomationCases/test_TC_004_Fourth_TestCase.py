import pytest

userName = "pradeep"


@pytest.fixture(scope="module")
def fixture_code():
    print("\nThis is our fixture and will execute before test case.")
    print("-----------------------")
    yield
    print("\n Close DB connection after TC")
    print("-----------------------")


@pytest.mark.P1
def test_001_login_logout_test_case(fixture_code):
    print("\nLogin and logout test case")


@pytest.mark.P1
# @pytest.mark.skip("Skipping this test case due to some issue")
def test_003_login_logout_invalid_credentials(fixture_code):
    print("\nlogin logout validation")
