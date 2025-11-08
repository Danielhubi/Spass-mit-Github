#Temperaturen auswerten

temperature = [14, 18, 21, 20, 19, 16, 15]

average = sum(temperature) / len(temperature)
print("Durchschnittstemperatur:", average)

print("Höchste Temperatur:", max(temperature))
print("Niedrigste Temperatur:", min(temperature))

def check_temperature(temperatures):
    average = sum(temperatures) / len(temperatures)
    
    if average > 20:
        print("Woche war warm!")
    else:
        print("Woche war eher kühl")
