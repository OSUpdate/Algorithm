from sys import stdin

input = stdin.readline

min, max = map(int,input().split())
arr = [i for i in range(min,max+1)]
res = []
for i in range(2,max):
    if max > i**2:
        res.append(i**2)
cnt = 0
for cur in res:
    for i in arr:
        if i%cur == 0:
            cnt+=1
print(max-min-cnt+1)
