print("Witaj w konwerterze jednostek \n Wybierz jednostkę wejściową: \n -cm \n -m \n -in \n -kg \n -lb")
unit = input("Podaj jednostkę: ")
if unit == "cm" or unit == "centymetr" or unit == "centymetry":
    cm = int(input("Podaj wartość: "))
    metres = cm/100
    inches = cm/0.394
    print("Długość {} {} to {:.3f} metrów lub {:.3f} cali".format(cm, unit, metres, inches))
elif unit == "m" or unit == "metr" or unit == "metry":
    m = int(input("Podaj wartość: "))
    centimetres = m/0.01
    inches = m*39.370
    print("Długość {} {} to {:.2f} centymetrów lub {:.3f} cali".format(m, unit, centimetres, inches))
elif unit == "in" or unit == "inches" or unit == "cale":
    inch = int(input("Podaj wartość: "))
    centimetres = inch/0.39370
    metres = inch/39.370
    print("Długość {} {} to {:.2f} centymetrów lub {:.3f} metrów".format(inch, unit, centimetres, metres))
elif unit == "kg" or unit =="kilogram" or unit == "kilogramy":
    kilogram = int(input("Podaj wartość: "))
    lb = kilogram*2.2046
    print("Waga {} {} to {.3f} funtów".format(kilogram, unit, lb))
elif unit == "lb" or unit == "funt" or unit == "funty":
    funt = int(input("Podaj wartość: "))
    kg = funt*2.2046
    print("Waga {} {} to {:.3f} kilogramów".format(funt, unit, kg))
else:
    print("Wybrano niepoprawną jednostkę")