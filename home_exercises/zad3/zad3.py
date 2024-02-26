#Piotr Branewski
from zad3testy import runtests
"""Pogram najpierw sprawdza czy wyraz jest leksykograficznie wiekszy od jego odrwotnosci jest tak to wyrazowi przypisuje jego odwrotnosc.
Nastepnie za pomoca mergesorta sortuje tablice, a potem przechodze liniowo po posortowanej tablicy i szukam maksa takich samych wyrazow.
"""

def merge(arr, l, m, r):

    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(a, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(a, l, m)
        mergeSort(a, m + 1, r)
        merge(a, l, m, r)


def strong_string(t):
    for i in range(len(t)):
        if t[i]>t[i][::-1]:
            t[i] = t[i][::-1]
    mergeSort(t,0,len(t)-1)
    i, j =0, 1
    cnt = 1
    maks = 0
    while j<len(t):
        if t[i] == t[j]:
            cnt+=1
            j+=1
        else:
            if maks<cnt:
                maks = cnt
            cnt = 1
            i=j
            j+=1
    return maks

# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
