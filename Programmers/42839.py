ans = []
def dfs(numbers,visit,answer,cnt):
    global ans
    if cnt == len(numbers) and int(''.join(ans)) not in answer:
        answer.append(int(''.join(ans)))
    for i,v in enumerate(numbers):
        if not visit[i]:
            visit[i] = True
            ans.append(str(v))
            dfs(numbers,visit,answer,cnt+1)
            visit[i] = False
            ans.pop()
def prime(num):
    if num == 1 or num == 0:
        return 0
    for i in range(2,num):
        if num%i == 0:
            return 0
    return 1
        
def solution(numbers):
    numbers = list(numbers)
    visit = [False] * len(numbers)
    answer = []
    for i in range(len(numbers)):
        dfs(numbers,visit,answer,i)
    print(answer)
    cnt = 0
    for v in answer:
        cnt += prime(v)
    print(cnt)
    return answer

solution('17')
solution('011')