import pandas as pd
import time
def merge(left,right):
    global count
    result=[]
    i=0
    j=0

    while True:
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            count+=len(left)-i
            result.append(right[j])
            j+=1

        if len(left) == i:
            result += right[j:]
            break
        if len(right) ==j:
            result += left[i:]
            break


    return  result


def merge_sort(A):
    if len(A) ==1:
        return A
    mid = len(A)//2

    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])

    return merge(left,right)


# arr=[1,3,2,4,67,9,10]

count=0
# print(merge_sort(arr))
# print(count)

file = open("IntegerArray.txt","r")
ls = []
for line in file:
    ls.append(int(line))

start = time.time()
print(merge_sort(ls))

print(count)
end = time.time()
print("total time:",end-start)




