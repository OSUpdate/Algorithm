def solution(people, limit):
    answer = 0
    people.sort()
    f = 0
    l = len(people) - 1
    while f < l:
        if people[f] + people[l] <= limit:
            print(people[f],people[l],f,l)
            l -= 1
            f += 1
        else:
            l -= 1
        answer += 1
    if l == f: 
        answer+=1
    return answer

print(solution([70, 50, 80, 50],100))
print(solution([20, 50, 50, 80], 100))
print(solution(	[70, 80, 50], 100))