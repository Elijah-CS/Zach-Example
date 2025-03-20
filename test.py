
from example import get_age_of_user

# @test
def test_age_of_john():
    result = get_age_of_user(None, "john")

    assert(result, 16) # assert that the result is the expected value

# @test
def test_age_of_alice():
    result = get_age_of_user(None, "alice")

    assert(result, 24) # assert that the result is the expected value

# @test
def test_age_of_None():
    result = get_age_of_user(None, None)

    assert(result, None) # assert that the result is the expected value

# @test
def test_age_of_Empty():
    result = get_age_of_user(None, "")

    assert(result, None) # assert that the result is the expected value