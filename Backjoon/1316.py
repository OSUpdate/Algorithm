import sys

n = int(sys.stdin.readline())
ans = 0
data = []
checker = [False]*26
for i in range(n):
    data.append(sys.stdin.readline().rstrip('\n'))
for st in data:
    tmp = ""
    check = 0
    for ch in st:
        tmp1 = ord(ch)-97
        if tmp == "":
            tmp = tmp1
            checker[tmp] = True
        if tmp != tmp1 and not checker[tmp1]:
            checker[tmp1] = True
            tmp = tmp1
            continue
        if tmp != tmp1 and checker[tmp1]:
            check = 1
            break
    if check != 1:
        ans += 1
    
    checker = [False]*26
print(ans)