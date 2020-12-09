from sys import stdin

input = stdin.readline

n = int(input())
arr = input().rstrip('\n').split()
tmp = []
visit = [False] * 10
answer = ""
mx, mn = "", ""
def check(pre,cur,val):
    if val == '<':
        return pre < cur
    if val == '>':
        return pre > cur

def find(answer,cur,end):
    global arr,tmp,visit
    if cur == end:
        tmp.append(answer)
        return
    for i in range(10):
        if not visit[i]:
            print(answer,cur)
            if cur == 0 or check(answer[-1],str(i),arr[cur-1]):
                visit[i] = True
                find(answer + str(i),cur+1,end)
                visit[i] = False
find(answer,0,n+1)
print(tmp[-1])
print(tmp[0])