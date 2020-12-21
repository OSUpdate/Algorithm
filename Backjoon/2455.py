from sys import stdin

input = stdin.readline
answer = 0
tmp = 0
for i in range(4):
    down, up = map(int,input().split())
    tmp -= down
    tmp += up
    answer = max(answer,tmp)
    print(answer)

print(answer)