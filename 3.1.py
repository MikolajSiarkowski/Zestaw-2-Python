x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
# ^ jest dobrze, chociaz srednik jest potrzbeny tylko w 1 linijce gdzie rozdziela komendy
for i in "qwerty": if ord(i) < 100: print (i)
# ^ mysle ze jest blad skladniowy, if powinno byc w kolejnej linicje poprzedzone tabulacja
for i in "axby": print (ord(i) if ord(i) < 100 else i)
#^ mysle ze jest dobrze
