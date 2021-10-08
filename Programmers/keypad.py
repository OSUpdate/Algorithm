def solution(numbers, hand):
    L = [1, 4, 7]
    R = [3, 6, 9]
    left = (3,0)
    right = (3,2)
    matrix = {
        1:(0,0),
        2:(0,1),
        3:(0,2),
        4:(1,0),
        5:(1,1),
        6:(1,2),
        7:(2,0),
        8:(2,1),
        9:(2,2),
        0:(3,1)
    }
    answer = ''
    for i in numbers:
        if i in L:
            answer += "L"
            left = matrix[i]
        elif i in R:
            answer += "R"
            right = matrix[i]
        else:
            check = matrix[i]
            left_size = abs(check[0] - left[0]) + abs(check[1] - left[1])
            right_size = abs(check[0] - right[0]) + abs(check[1] - right[1])
            if left_size > right_size:
                answer += "R"
                right = matrix[i]
            elif left_size < right_size:
                answer += "L"
                left = matrix[i]
            else:
                if hand == "right":
                    answer += "R"
                    right = matrix[i]
                else:
                    answer += "L"
                    left = matrix[i]

    return answer
