miarka = ""
liczba = int(input("podaj maksymalna liczbe na miarce(liczba calkowita): "))
liczba1 = liczba*5 +1 #6 bo liczymy od 0
i = 0
for i in range(liczba1):
    if (i == '0') or ((i % 5) == 0):
        miarka += "|"
        #print(miarka)
    else:
        miarka += "."
miarka += "\n"
num = 0
j=0
for num in range(liczba+1):
    if num < 9:
        miarka += str(num)+"    "
    else:
       miarka += str(num)+"   "
print(miarka)
