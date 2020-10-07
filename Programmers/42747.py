def solution(citations):
    answer = []
    n = len(citations)
    citations.sort()
    tmp = [n-i for i in range(n)]
    for i in range(n):
        cnt =0
        for j in range(n):
            if tmp[i] <= citations[j]:
                cnt += 1
        if cnt == tmp[i]:
            answer.append(tmp[i])
        else:
            answer.append(min(tmp[i],cnt))
    return max(answer)

