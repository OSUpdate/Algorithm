import sys
n = []
for i in range(9):
    n.append(int(sys.stdin.readline()))
m = max(n)
print(m)
print(n.index(m)+1)
