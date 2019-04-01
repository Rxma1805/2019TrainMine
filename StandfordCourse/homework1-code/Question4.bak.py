import time

inverse = 0

def mergesort_nopop(ls):
    global inverse
    if len(ls) <= 1:
        return ls
    else:
        i = len(ls)//2
        ls1 = mergesort_nopop(ls[:i])
        ls2 = mergesort_nopop(ls[i:])
        ls = []
        i = 0
        j = 0
        while True:
            if ls1[i] <= ls2[j]:
                ls.append(ls1[i])
                i += 1
            else:
                ls.append(ls2[j])
                j += 1
                inverse += len(ls1) - i
            if len(ls1) == i:
                ls += ls2[j:]
                break
            if len(ls2) == j:
                ls += ls1[i:]
                break
        return ls


file = open("IntegerArray.txt","r")
# ls = file.readlines()
ls = []
for line in file:
    ls.append(int(line))


start = time.time()
mergesort_nopop(ls)
# mergesort_nopop([1,3,5,2,4,6])
print("count:",inverse)
end = time.time()
print("total time:",end-start)