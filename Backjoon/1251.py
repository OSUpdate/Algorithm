import sys

text = sys.stdin.readline().rstrip('\n')
index = 1
ans = []
for a in range(1,len(text)-1):
    for b in range(a+1,len(text)):
        front = text[:a][::-1]
        center = text[a:b][::-1]
        end = text[b:len(text)][::-1]
        ans.append(front+center+end)
ans.sort()
print(ans[0])