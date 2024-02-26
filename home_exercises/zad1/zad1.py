#Piotr Branewski
from zad1testy import runtests
"""program iteruje od drugiej litery danego wyrazu w pierwszej petli, petla ta przesuwa dopoki i < dlugosci wyrazu - polowa aktualnego maks. 
nastepnie druga petla ma while przesuwa sie po wyrazie w lewo za pomoca l i w prawo za pomoca p, dopóki s[l]!=s[p] 
i zwiksza na biezaco dlugosc palindromu, za pomoca funcki maks sprawdzam czy aktualny palindrom jest wiekszy od poprzedniego
i zwracam ml gdzie jest odpowiedz na zadanie. orientacyjny czas algorytmu to O(n^2)"""
def maks(a,b):
    if a>b:
        return a
    return b

def ceasar( s ):
    n = len(s)
    ml = 1 #odp
    le = 1 #dlugosc aktualnie sprawdzana
    i = 1 #srodek prawdopodobnego palindromu
    while i < n-(ml//2): #idzie po kolejnych literach slowa
        l = i - 1
        r = i + 1
        while l >= 0 and r < n: #przesuwam o 1 w lewo i o 1 w prawo
            if s[l] != s[r]:  #jesli tak bedzie sprawdzam maks(ml,le) i wychodze
                ml = maks(le, ml)
                break
            else:
                le += 2
            l -= 1
            r += 1
        ml = maks(le, ml) #jesli sie zakonczy petle to sprawdzam maks
        i += 1
        le = 1
    return ml



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )