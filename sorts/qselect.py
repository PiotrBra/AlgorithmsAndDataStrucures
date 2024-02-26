
def partition(t, p, r):
    pivot = t[r]
    i = p - 1
    for j in range(p,r):
        if t[j] < pivot:
            i+=1
            t[j], t[i] = t[i], t[j]
    t[i+1], t[r] = t[r], t[i+1]
    return i+1


def quickselect(t,p,r,x):
    if p == r:
        return t[p]
    q = partition(t,p,r)
    if x == q:
        return t[x]
    elif x < q:
        return quickselect(t,p,q-1,x)
    else:
        return quickselect(t,q+1,r,x)


t =[1,2,4,3,6,6]
print(quickselect(t,0,5,3))