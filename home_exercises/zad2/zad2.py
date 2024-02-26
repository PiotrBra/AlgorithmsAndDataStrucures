#Piotr Branewski
from zad2testy import runtests
"""Program sortuje otrzymana tablice malejaco za pomoca quicksorta,
nastepnie w petli while przechodzimy po kolejnych elementach tabliy i dodajemy je do zebranego sniegu odejmujac dzien zebrania.
jesli wartosc sniegu - dzien <=0 konczymy petle i zwracamy wartosc zebranego sniegu. Zlozonosc algorytmu to O(nlogn)"""


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def qs(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        qs(array, low, pi - 1)
        qs(array, pi + 1, high)


def snow( s ):
    day = 0
    taken = 0 #zebrany snieg
    qs(s, 0, len(s)-1)
    i = len(s) - 1
    while i >= 0:
        if s[i] - day <= 0:
            break
        taken += s[i] - day
        i -= 1
        day += 1
    return taken

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
