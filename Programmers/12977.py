import math
data = []
answer = []
def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if (num % i == 0): return False
    return True
def dfs(arr, visit, cnt):
    global data, answer
    if (len(arr) == cnt and is_prime(sum(arr))):
        answer.append([*arr])
        return
    for i,v in enumerate(data):
        if not visit[i] and len(arr) < cnt:
            visit[i] = True
            arr.append(v)
            dfs(arr, visit, cnt)
            del arr[-1]
            visit[i] = False
def solution(nums):
    global answer, data
    data = nums
    cnt = len(nums)
    visit = [False] * cnt
    dfs([], visit, 3)
    for arr in answer:
        arr.sort()
    answer = list(set(map(tuple, answer)))

    return len(answer)
