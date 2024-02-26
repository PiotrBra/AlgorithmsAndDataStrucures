from math import inf

def merge(T, p, q, r):
    n1 = q-p+1
    n2 = r-q
    L = [0]*(n1+1)
    R = [0]*(n2+1)
    for i in range(n1):
        L[i] = T[p+i]
    for j in range(n2):
        R[j] = T[q+j+1]
    L[-1] = inf
    R[-1] = inf
    i = j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1

def mergesort(a,p,r):
    if p < r:
        m = (p+r)//2
        mergesort(a,p,m)
        mergesort(a,m+1,r)
        merge(a,p,m,r)

t = [1,2,5,7,2,4,31,5]
mergesort(t,0,len(t)-1)
print(t)