from main import weathercheck
import pytest

#Test cases for weathercheck function
@pytest.mark.parametrize("temp,expected", [
    (35, "Hot"),
    (10, "Cold"),
    (20, "Moderate")
])
def test_weather_check(temp, expected):
    assert weathercheck(temp) == expected

if __name__ == "__main__":
    pytest.main([__file__])