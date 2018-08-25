print("Witaj w kalkulatorze zapotrzebowania kalorycznego")
sex = input("Podaj swoją płeć: ")

if sex == "kobieta" or sex == "Kobieta" or sex == "K" or sex == "k":
    ageK = float(input("Podaj swój wiek: "))
    heightK = float(input("Podaj swój wzrost(cm): "))
    weightK = int(input("Podaj swoją wagę(kg): "))
    S = -161
    PPM_K = 10*weightK + 6.25*heightK - 5*ageK + S
    active = input("Wybierz numer określający rodzaj aktywności fizycznej: \n 1. Praca siedząca, brak dodatkowej aktywności \n 2. Praca niefizyczna, mało aktywny tryb życia \n 3. Lekka praca fizyczna, regularne ćwiczenia 3-4 razy w tygodniu \n 4. Praca fizyczna, regularne ćwiczenia od 5 razy w tygodniu \n 5. Praca fizyczna ciężka, regularne ćwiczenia 7 razy w tygodniu \n Twój wybór: \n")
    if active == "1" or active == "1.":
        PPM_K = PPM_K * 1.2
        print("Dzienne zapotrzebowanie kaloryczne wynosi:", PPM_K, "kcal")
    elif active == "2" or active == "2.":
        PPM_K = PPM_K * 1.4
        print("\n Dzienne zapotrzebowanie kaloryczne wynosi: ", PPM_K, "kcal")
    elif active == "3" or active == "3.":
        PPM_K = PPM_K * 1.6
        print("\n Dzienne zapotrzebowanie kaloryczne wynosi: ", PPM_K, "kcal")
    elif active == "4" or active == "4.":
        PPM_K = PPM_K * 1.8
        print("\n Dzienne zapotrzebowanie kaloryczne wynosi: ", PPM_K, "kcal")
    elif active == "5" or active == "5.":
        PPM_K = PPM_K * 2.0
        print("\n Dzienne zapotrzebowanie kaloryczne wynosi: ", PPM_K, "kcal")
    else:
        print("Nie ma takiej aktywności!")
elif sex == "mezczyzna" or sex == "Mezczyzna" or sex == "M" or sex == "m" or sex == "mężczyzna" or sex == "Mężczyzna":
    ageM = float(input("Podaj swój wiek: "))
    heightM = float(input("Podaj swój wzrost(cm): "))
    weightM = int(input("Podaj swoją wagę(kg): "))
    S = 5
    PPM_M = 10*weightM + 6.25*heightM - 5*ageM + S
    active = input("Wybierz numer określający rodzaj aktywności fizycznej: \n 1. Praca siedząca, brak dodatkowej aktywności \n 2. Praca niefizyczna, mało aktywny tryb życia \n 3. Lekka praca fizyczna, regularne ćwiczenia 3-4 razy w tygodniu \n 4. Praca fizyczna, regularne ćwiczenia od 5 razy w tygodniu \n 5. Praca fizyczna ciężka, regularne ćwiczenia 7 razy w tygodniu \n Twój wybór: \n")
    if active == "1" or active == "1.":
        PPM_M = PPM_M * 1.2
        print("Dzienne zapotrzebowanie kaloryczne wynosi:", PPM_M, "kcal")
    elif active == "2" or active == "2.":
        PPM_M = PPM_M * 1.4
        print("\n Dzienne zapotrzebowanie kaloryczne wynosi: ", PPM_M, "kcal")
    elif active == "3" or active == "3.":
        PPM_M = PPM_M * 1.6
        print("\n Dzienne zapotrzebowanie kaloryczne wynosi: ", PPM_M, "kcal")
    elif active == "4" or active == "4.":
        PPM_M = PPM_M * 1.8
        print("\n Dzienne zapotrzebowanie kaloryczne wynosi: ", PPM_M, "kcal")
    elif active == "5" or active == "5.":
        PPM_M = PPM_M * 2.0
        print("\n Dzienne zapotrzebowanie kaloryczne wynosi: ", PPM_M, "kcal")
    else:
        print("Nie ma takiej aktywności!")
else:
    print("Nie wiem kim jesteś! Nie mogę wyliczyć dziennego zapotrzebowania kalorycznego")