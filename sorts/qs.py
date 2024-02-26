def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            (A[i], A[j]) = (A[j], A[i])
    (A[i+1], A[r]) = (A[r], A[i+1])
    return i + 1


def qs(A, p, r):
    if p < r:
        q = partition(A, p, r)
        qs(A, p, q-1)
        qs(A, q+1, r)

a = [2,1,4,3,2,0]
print(a)
qs(a,0,len(a)-1)
print(a)