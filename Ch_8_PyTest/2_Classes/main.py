class weather:

    def __init__(self, temp:float):
        self.temp = temp


    def weather_check(self)-> str:
        if self.temp < 0:
            return "It's Freezing"
        elif self.temp < 15:
            return "It's Cold"
        else:
            return "It's Moderate"
        
    def rain_check(self, rain_chance:float)-> str:
        if rain_chance > 0.5:
            return "It's Raining"
        else:
            return "It's Not Raining"