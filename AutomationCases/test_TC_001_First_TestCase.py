import pytest

userName = "pradeep"


@pytest.fixture(scope="module")
def fixture_code():
    print("\nThis is our fixture and will execute before test case.")
    print("-----------------------")
    yield
    print("\n Close DB connection after TC")
    print("-----------------------")

@pytest.mark.Smoke
@pytest.mark.Regression
def test_001_login_logout_test_case(fixture_code):
    print("\nLogin and logout test case")
    assert userName == "pradeep"


# @pytest.mark.skip("Skipping this test case due to some issue")
@pytest.mark.Sanity
def test_003_login_logout_invalid_credentials(fixture_code):
    print("\nlogin logout validation")
    assert userName == "sahani", "user name not matched"
