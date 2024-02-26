def partition(A, p, r, k):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j][k] <= x[k]:
            i += 1
            A[i], A[j] = A[j], A[i]
        A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def qs(A, p, r, k):
    if p < r:
        q = partition(A, p, r, k)
        qs(A, p, q-1, k)
        qs(A, q+1, r, k)


def radixsort(a,k): #for strings
    #k dlugosc stringa (wszystkie takie same)
    for i in range(k-1,-1,-1):
        qs(a,0,len(a)-1 ,i)

a = [
    "ads",
    "ggs",
    "dah",
    "dag",
    "ags",
    "qra",
    "sga",
    "dpa",
]
print(a)
radixsort(a,2)
print(a)