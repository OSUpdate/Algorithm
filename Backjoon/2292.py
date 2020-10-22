from sys import stdin

input = stdin.readline

n = int(input())
cnt = 1
tot = 1
if n == 1:
    print(1)
else:
    while True:
        if tot >= n:
            break
        tot += 6*cnt
        cnt += 1
    print(cnt)
