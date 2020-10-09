from sys import stdin
input = stdin.readline

n = int(input())
pre = str(input().rstrip('\n'))
ans = list(pre)
for _ in range(n-1):
    text = str(input().rstrip('\n'))
    for i,t in enumerate(text):
        if pre[i] != t:
            ans[i] = '?'
print(''.join(ans))
