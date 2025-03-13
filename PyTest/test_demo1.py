import pytest

@pytest.mark.xfail
def test_secondmethod():
    print("2nd method")
@pytest.mark.smoke
def test_thirdmethod():
    print("3rd method")