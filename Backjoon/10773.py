from sys import stdin
input = stdin.readline

n = int(input())
ans = []
for i in range(n):
    tmp = int(input())
    if tmp == 0:
        ans.pop()
    else:
        ans.append(tmp)
print(sum(ans))
