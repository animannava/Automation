import pytest

@pytest.mark.skip
def test_firstmethod():
    print("1st method")

@pytest.mark.smoke
def test_secondmethod():
    mes='Hi'
    assert mes=='Hello', "strings are not matching"