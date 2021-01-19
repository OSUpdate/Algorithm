import heapq

def solution(food_times, k):
    q = []
    for i,f in enumerate(food_times):
        heapq.heappush(q,(f,i+1))
    length = len(food_times)
    prev = 0
    minTime = q[0][0]
    while k - ((minTime - prev) * length) >= 0:
        k -= (minTime-prev) * length
        heapq.heappop(q)
        prev = minTime
        length -= 1
        if not q:
            return -1
        minTime = q[0][0]
    idx = k % length
    q.sort(key=lambda x: x[1])
    return q[idx][1]
print(solution([3,1,2],5))
print(solution([4,2,3,6,7,1,5,8],16))
print(solution([4,2,3,6,7,1,5,8],27))