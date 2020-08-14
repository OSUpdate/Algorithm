import sys

n, m = map(int,sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split()))
ans = []
for i in range(len(card)):
    for j in range(i+1,len(card)-1):
        for w in range(j+1,len(card)):
            tmp = card[i]+card[j]+card[w]
            if tmp <= m:
                ans.append(tmp)
print(max(ans))