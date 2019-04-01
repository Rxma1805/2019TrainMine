import numpy as np

def FindMaxTournament(low,high,A):
    if low == high:
        compare = A[low]

        return compare
    compare1 = FindMaxTournament(low,(int)((low+high)/2),A)
    print(compare1)
    print("-------"+str(low)+"："+str((int)((low+high)/2)))
    compare2 = FindMaxTournament((int)((low + high) / 2)+1,high, A)
    print(compare2)
    print("*******"+str((int)((low + high) / 2)+1)+"："+str(high))
    if compare1 > compare2:
        return compare1
    else:
        return compare2

a=[10,1,3,5,9,8,15,7]
Max = FindMaxTournament(0,len(a)-1,a)
#时间复杂度是log n

#然后寻找第二大的


print("&&&&&&&&&&&&&&&&&&&")
print(np.sort(a))
print(Max)