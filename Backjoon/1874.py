from sys import stdin

input = stdin.readline

n = int(input())
arr = []
stack = []
[arr.append(int(input())) for _ in range(n)]
ans = []
check = False
idx, end = 0,len(arr)
l = 1
while idx != end:
    if stack and arr[idx] == stack[-1]:
        stack.pop()
        idx += 1
        ans.append('-')
    elif l <= arr[idx]:
        while l <= arr[idx]:
            stack.append(l)
            l+=1
            ans.append('+')
    else:
        check = True
        print("NO")
        break
if not check:
    [print(ch) for ch in ans]