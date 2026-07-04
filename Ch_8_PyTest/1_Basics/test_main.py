from main import weathercheck

#Test cases for weathercheck function
def test_weather_check():
    assert weathercheck(35) == "Hot"
    assert weathercheck(10) == "Cold"
    assert weathercheck(20) == "Moderate"

if __name__ == "__main__":
    test_weather_check()
