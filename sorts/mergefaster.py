from math import inf
def merge(t,p,q,r):
    l1 = t[p:q+1]
    r1 = t[q+1:r+1]
    l1.append(inf)
    r1.append(inf)
    i = j = 0
    for k in range(p, r+1):
        if l1[i] <= r1[j]:
            t[k] = l1[i]
            i += 1
        else:
            t[k] = r1[j]
            j+=1


def mergesort(t,p,r):
    if len(t)<=1:
        return t
    elif p < r:
        q = (p+r)//2
        mergesort(t,p,q)
        mergesort(t,q+1,r)
        merge(t,p,q,r)


t = [1,5,2,5,34,6,1]
mergesort(t,0,len(t)-1)
print(t)