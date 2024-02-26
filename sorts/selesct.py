

def partition(a,p,r):
    x = a[r]
    i = p-1
    for j in range(p,r):
        if a[j] <= x:
            i+=1
            (a[i], a[j]) = (a[j], a[j])
    (a[i+1], a[r])=(a[r], a[i+1])
    return i+1

def select(a,k):
    p = 0
    r = len(a)-1
    q = partition(a,p,r)
    if q == k:
        return q
    if p < r:
        q = partition(a,p,r)
        partition(a,q+1,q)
        partition(a,p,q-1)

t = [2,1,4,3,5]
print(select(t,3))