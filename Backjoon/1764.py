import sys

n, m = map(int,sys.stdin.readline().split())
inp = []
inp1 = []
ans = []
for i in range(n):
    inp.append(sys.stdin.readline().rstrip('\n'))
for i in range(m):
    inp1.append(sys.stdin.readline().rstrip('\n'))
tmp = set(inp+inp1)
tmp1 = set(inp)-set(inp1)
tmp2 = set(inp1)-set(inp)
ans = list(tmp-tmp1-tmp2)
ans.sort()
print(len(ans))
for _,v in enumerate(ans):
    print(v)
