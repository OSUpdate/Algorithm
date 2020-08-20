import sys

n = int(sys.stdin.readline())
m = list(map(int,sys.stdin.readline().split()))

print("%d %d" % (min(m),max(m)))