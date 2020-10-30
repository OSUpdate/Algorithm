from sys import stdin

input = stdin.readline

n,b = map(int,input().split())
arr = []
def matrix(num):
    global arr,n
    if num == 1:
        for i in range(n):
            for j in range(n):
                arr[i][j] %= 1000
        return arr
    elif num % 2 == 1:
        tmp = [[0]*n for _ in range(n)]
        t = matrix(num -1)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    tmp[i][j] += t[i][k] * arr[k][j]
                tmp[i][j] %= 1000

    else:
        tmp = [[0]*n for _ in range(n)]
        t = matrix(num //2)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    tmp[i][j] += t[i][k] * t[k][j]
                tmp[i][j] %= 1000

    return tmp
        
for _ in range(n):
    arr.append(list(map(int,input().split()))) 
ans = matrix(b)
for i in range(n):
    for j in range(n):
        print(ans[i][j], end=" ")
    print()
'''
from sys import stdin

input = stdin.readline

n,b = map(int,input().split())
arr = []
def pow(a,b):
    global n 
    ans = [[0 for _ in range(n)] for _ in range(n)]
    print(a,b)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans[i][j] += a[i][k] * b[k][j]
            ans[i][j] %= 1000
    print(ans)
    return ans
def matrix(b):
    global arr,n
    res = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
    while b>0:

        if b % 2 == 1:
            b -=1
            res = pow(res,arr)
        else:
            b //=2
            arr = pow(arr,arr)
        
    return res
for _ in range(n):
    arr.append(list(map(int,input().split()))) 
print(matrix(b))
'''
