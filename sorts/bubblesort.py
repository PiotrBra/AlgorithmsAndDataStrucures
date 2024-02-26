

def bubblesort(t):
    swapped = False
    for n in range(len(t)-1, 0, -1):
        for i in range(n):
            if t[i] > t[i + 1]:
                swapped = True
                t[i], t[i + 1] = t[i + 1], t[i]
        if not swapped:
            return


t = [11,12,2423,242,121,111,423,4267,7,56,46,353,7452,24,22,42,524246,5462]
bubblesort(t)
print(t)