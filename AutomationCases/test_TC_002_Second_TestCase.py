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
def test_002_registration_test_case(fixture_code):
    print("\nRegistration test case")
