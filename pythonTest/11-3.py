from sys import stdin

input = stdin.readline

s = list(map(int,input().rstrip('\n')))
zero = 0
one = 0
for i in range(1,len(s)-1):
    if s[i] != s[i-1]:
        continue
    if s[i] == 0:
        zero += 1
    else:
        one += 1
print(min(zero,one))