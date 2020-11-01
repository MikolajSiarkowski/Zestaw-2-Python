L = [3, 5, 4] ; G = L.sort() #w tym przypadku zostanie zwrocone "none" zamiast posortowanej listy
x, y = 1, 2, 3 #brakuje 3 zmiennej do przypisania jej w tym wypadku "3"
X = 1, 2, 3 ; X[1] = 4 # nie mozna zmieniac wartosci przypisanej juz wczesniej
X = [1, 2, 3] ; X[3] = 4 #blad w indeksowaniu, X[0]=1,X[1]=2,X[2]=3, indeks o numerze 3 jest poza zasiegiem
X = "abc" ; X.append("d") #komenda append nie dziala do napisu
L = list(map(pow, range(8))) #pow nie ma arugmentow, powinno miec przynajmniej 2
