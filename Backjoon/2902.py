import sys

name = sys.stdin.readline().rstrip('\n')
check = False
ans = ""
for ch in name:
    if ans == "":
        ans += ch
    if ch == '-':
        check = True
        continue
    if check:
        check = False
        ans += ch
print(ans)