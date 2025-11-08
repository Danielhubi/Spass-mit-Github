#Temperaturen auswerten

temperature = [14, 18, 21, 20, 19, 16, 15, 1, 99, 23]

average = sum(temperature) / len(temperature)
print("Durchschnittstemperatur:", average)

print("Höchste Temperatur:", max(temperature))
print("Niedrigste Temperatur:", min(temperature))

  
if average > 20:
     print("Woche war warm!")
else:
    print("Woche war eher kühl")

def counttempOver18(input_list:list):
     return len([x for x in input_list if x > 18])

print(counttempOver18(temperature))