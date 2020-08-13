import sys
s = int(sys.stdin.readline())
tmp = 0
ans = []
i = 0
t = 0
while t < s:
    i += 1
    t += i
    ans.append(i)
l = t - s
if l in ans:
    ans.remove(l)
print(len(ans))