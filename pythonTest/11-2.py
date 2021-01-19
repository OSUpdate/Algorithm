from sys import stdin

input = stdin.readline

s = list(map(int,input().rstrip('\n')))
res = s[0]
check = False
if s[0] == 0 or s[0] == 1:
    check = True

for i in range(1,len(s)):
    if s[i] == 0 or s[i] == 1:
        check = True
    if check:
        res += s[i]
        check = False
    else:
        res *= s[i]
print(s,res)