
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0 for _ in range(bridge_length)]
    while q:
        q.pop(0)
        answer += 1
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)

    return answer

solution(2,10,[7,4,5,6])
#solution(100,100,[10])
#solution(100,100,[10,10,10,10,10,10,10,10,10,10])