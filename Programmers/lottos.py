def solution(lottos, win_nums):
    lottos = [i for i in lottos if i > 0]
    unknown = 6 - len(lottos)
    win = 0
    for i in lottos:
        if i in win_nums:
            win += 1
    lotto_table = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    answer = [lotto_table[unknown + win], lotto_table[win]]
    return answer
