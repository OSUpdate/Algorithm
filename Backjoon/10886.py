from sys import stdin

input = stdin.readline

n = int(input())
ans = [0,0]
for i in range(n):
    tmp = int(input())
    ans[tmp] += 1
if ans[0] > ans[1]:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")