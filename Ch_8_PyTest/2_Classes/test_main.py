from main import weather

# Test cases for the weathercheck function
def test_weather_check():
     w=weather()
     assert w.weather_check(-5) == "It's Freezing"
     
     assert w.weather_check(10) == "It's Cold"

     assert w.weather_check(20) == "It's Moderate"    

def test_rain_check():
    w=weather()
    assert w.rain_check(0.6) == "It's Raining"
    assert w.rain_check(0.4) == "It's Not Raining"