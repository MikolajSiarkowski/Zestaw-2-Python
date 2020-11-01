line = "";
while True:
    line = input("podaj liczbe(aby przerwac wpisz stop):")
    if line == "stop":
        break
    elif line.isdigit() == True:
        liczba = float(line)
        print("liczba: ", liczba,"\n3-potega liczby: ", liczba**3)
    else:
        print("wpisz liczbe lub 'stop'")
