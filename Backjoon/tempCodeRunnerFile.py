import sys

n = list(map(int,sys.stdin.readline().split()))
ans = ""
rev = 8
cnt = [0,0]
for i,v in enumerate(n):
    if i+1 == v:
        cnt[0] += 1
    elif rev == v:
        cnt[1] += 1
        rev -= 1
       
    else:
        ans = "mixed"
        break
if cnt[0] == 8:
    ans = "ascending"
if cnt[1] == 8:
    ans = "descending"
print(ans)