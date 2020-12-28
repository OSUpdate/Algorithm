from sys import stdin

input = stdin.readline
answer = [[(j**i)%10 for i in range(1,5)] for j in range(10)]
print(answer)
t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    a %=10
    if a == 0:
        print(10)
    else:
        print(answer[a][b%4 -1])
