import sys

n, m = map(str,sys.stdin.readline().split())
s = int(n[::-1])
s1 = int(m[::-1])
print(max(s,s1))
