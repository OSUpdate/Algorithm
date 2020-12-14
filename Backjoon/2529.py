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
<<<<<<< HEAD
print(tmp)
'''
for i in range(0,10):
    answer[0] = i
    numCheck = [False] * 10
    curCheck = 1
    numCheck[i] = True
    for j in range(1,n+1):

        for k in range(0,10):
            if not numCheck[k] and ((arr[j-1] == '<' and answer[j-1] < k) or (arr[j-1] == '>' and answer[j-1] > k)):
                print(answer,j,k,numCheck)
                answer[j] = k
                numCheck[k] = True
                curCheck += 1
            if curCheck == n+1:
                break
    print(answer)
'''

=======
print(tmp[-1])
print(tmp[0])
>>>>>>> 7f6ccc3c1851cb2367899ce36e72f9db9a74f802
