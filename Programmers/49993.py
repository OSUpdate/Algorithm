
def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        pre = -1
        check = False
        nxt = False
        end = False
        for i,sk in enumerate(skill):
            for j,tr in enumerate(tree):
                print(sk,tr,pre,check,nxt)
                if sk == tr:
                    if not nxt and pre < j:
                        check = True
                        pre = j
                        break
                    else:
                        end = True
                        break
                else:
                    check = False
            if not check:
                nxt = True
        if not end:
            answer += 1

    return answer
print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))