import sys

n = int(sys.stdin.readline())
fi = [0,1]
tmp = 0
for i in range(n+1):
    tmp = fi[i+1] + fi[i]
    fi.append(tmp)
print(fi[n])