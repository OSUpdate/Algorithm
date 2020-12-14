from sys import stdin

input = stdin.readline

n,m,k = map(int,input().split())
arr = list(map(int,input().split()))
answer = 0
cur = 0
arr.sort(reverse=True)
for i in range(1,m+1):
    if i%(k+1)==0:
        print(i,k,arr[cur+1])
        answer += arr[cur+1]
    else:
        print(i,k,arr[cur])
        answer += arr[cur]
print(answer)