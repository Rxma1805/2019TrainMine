
def findRecursion(L,R,A):
    if L == R:
        return A[L]
    mid = (int)((L + R) / 2)
    
    if A[mid] > A[mid+1]:
        return findRecursion(L, mid, A)
    else:
        return findRecursion(mid + 1, R, A)

input = [1,3,5,7,9,11,5,3,4]
print(input)
print(findRecursion(0,len(input)-1,input))
