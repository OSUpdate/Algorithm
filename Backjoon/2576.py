import sys

arr = []

for i in range(7):
    n = int(sys.stdin.readline())
    if n%2 == 1:
        arr.append(n)
if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)