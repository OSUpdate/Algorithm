from sys import stdin

input = stdin.readline

n = int(input())

for _ in range(n):
    stack = []
    check = False
    vps = str(input())
    for ch in vps:
        if ch == '(':
            stack.append(ch)
        if ch == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
    
    if not stack:
        print('YES')
    else:
        print('NO')