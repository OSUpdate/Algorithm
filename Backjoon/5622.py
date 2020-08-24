import sys

n = str(sys.stdin.readline().rstrip('\n'))
ans = 0
temp = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
for ch in n:
    init = 3
    for st in temp:
        if ch in st:
            ans += init
        else:
            init += 1
print(ans)