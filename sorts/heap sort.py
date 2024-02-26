from math import floor
#heap na tablice

def left(p):
    return 2*p + 1
def right(p):
    return 2*p + 2
def parent(p):
    return floor(p-1/2)


def heapify(a, i, n):
    l = left(i)
    r = right(i)
    max_ind = i

    if l < n and a[max_ind] < a[l]:
        max_ind = l
    if r < n and a[max_ind] < a[r]:
        max_ind = r
        
    if max_ind != i:
        (a[max_ind], a[i]) = (a[i], a[max_ind])
        heapify(a, max_ind, n)

def buildheap(a):
    n = len(a)
    for i in range(parent(n-1), -1, -1):
        heapify(a, i, n)

def heapsort(a):
    n = len(a)
    buildheap(a)

    for i in range(n-1, 0, -1):
        (a[i], a[0]) = (a[0], a[i])
        heapify(a, 0, i)

a = [12,11,4,7,3,8,9,10]
heapsort(a)
print(a)