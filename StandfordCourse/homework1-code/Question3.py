array=[]
def find(L,R,A,B):
    if L == R:
        if A[L] ==L:
            B.append(L)
            return
        else:
            return
    find(L,(int)((L+R)/2),A,B)
    find((int)((L + R) / 2)+1,R, A,B)

A=[0,4,56,3,567,6789,6,678,678,9,789,8]
B=[]
find(0,len(A)-1,A,B)
print(B)