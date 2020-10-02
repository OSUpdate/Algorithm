from sys import stdin

input = stdin.readline
stack = []
n = int(input())
for _ in range(n):
    tmp = list(map(str,input().split()))

    if tmp[0] == 'push':
        stack.append(tmp[1])
    if tmp[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    if tmp[0] == 'size':
        print(len(stack))
    if tmp[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    if tmp[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

