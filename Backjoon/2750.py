import sys

n = int(sys.stdin.readline())
ans = []
for i in range(n):
    ans.append(int(sys.stdin.readline()))
ans.sort()
for i in ans:
    print(i)