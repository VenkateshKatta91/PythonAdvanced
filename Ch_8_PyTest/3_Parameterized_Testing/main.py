def weathercheck(temp:float)->str:
    if temp>30:
        return "Hot"
    elif temp<15:
        return "Cold"
    else:
        return "Moderate"
    
print(weathercheck(12))