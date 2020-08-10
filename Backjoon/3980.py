import sys

c = int(sys.stdin.readline())

res = []
for i in range(c):
    inp = []
    ans = [[0 for t in range(11)]for row in range(c)]
    for j in range(11):
        arr = list(map(int,sys.stdin.readline().split()))
        inp.append(arr)
    for a in range(11):
        temp = []
        for b in range(11):
            temp.append(inp[a][b])
        ans[i][a] = max(temp)
    res.append(sum(ans[i]))
print(max(res))

