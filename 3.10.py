Rzymskie = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
    "IV" : 4,
    "IX" : 9,
    "XL" : 40,
    "XC" : 90,
    "CD" : 400,
    "CM" : 900
}
x = input("Podaj liczbe rzymska: ")


def roman2arab(liczba):
    result = 0
    for x in range(len(liczba)):
        if x+1 < len(liczba):
            if Rzymskie[liczba[x]] >= Rzymskie[liczba[x+1]]:
                y = Rzymskie[liczba[x]]
                result += y
            else:
                y = Rzymskie[liczba[x]]
                result -= y
        else:
            y = Rzymskie[liczba[x]]
            result += y    
    return result

print(roman2arab(x))

