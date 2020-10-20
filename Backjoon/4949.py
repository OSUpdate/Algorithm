from sys import stdin

input = stdin.readline

while True:
    text = str(input().rstrip('\n'))
    if text == '.':
        break
    stack = []
    for ch in text:
        if ch == '.':
            break
        if ch == '(' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == ']':
            if stack:
                if (stack[-1] == '(' and ch == ')') or (stack[-1] == '[' and ch == ']'):
                    stack.pop()
                else:
                    stack.append(ch)

            else:
                stack.append(ch)
    if not stack:
        print('YES')
    else:
        print('NO')