def solution(clothes):
    answer = 0
    dic = dict()
    for clothe,kind in clothes:
        if kind in dic:dic[kind] += 1
        else: dic[kind] = 1
    print(dic.values())
    return answer

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])