rysunek = ""
print("podaj rozmiar prostokonta:")
dlugosc, szerokosc = int(input("dlugosc: ")),int(input("szerokosc: "))
dlugosc = dlugosc*4+1
szerokosc = szerokosc*2+1
for i in range(szerokosc):
    if i > 0:
        rysunek += "\n"
    for j in range(dlugosc):
        if (i % 2) == 0:
            if (j == '0') or ((j % 4) == 0):
                rysunek += "+"
            else:
                rysunek += "-"
        else:
            if (j == '0') or ((j % 4) == 0):
               rysunek += "|"
            else:
                rysunek += " "

print(rysunek)
