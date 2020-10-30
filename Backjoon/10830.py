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