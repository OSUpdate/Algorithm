def solution(n, delivery):
    answer = ''
    arr = [-1]*n
    delivery.sort(key=lambda x: x[2], reverse=True)
    for v1,v2,check in delivery:
        if check == 1:
            arr[v1-1] = 1
            arr[v2-1] = 1
        else:
            if arr[v1-1] == 1 and arr[v2-1] == -1:
                arr[v2-1] = 0
            elif arr[v1-1] == -1 and arr[v2-1] == 1:
                arr[v1-1] = 0
    for v in arr:
        if v == 1:
            answer += 'O'
        elif v == -1:
            answer += '?'
        else:
            answer += 'X'

    return answer

arr = [[1,3,1],[3,5,0],[5,4,0],[2,5,0]]
print(solution(6,arr))