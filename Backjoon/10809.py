import sys

n = list(map(str,sys.stdin.readline()))
ans = []
for i in range(97,123):
    cur = -1
    if chr(i) in n:
        cur = n.index(chr(i))
    ans.append(cur)
for i in ans:
    print(i, end=' ')