def solution(board, moves):
    answer = 0
    board_arr = []
    board_res = []
    size = len(board)
    for i in range(size):
        board_arr.append(
            [board[j][i] for j in range(size) if board[j][i] != 0])
    for i in moves:
        if len(board_arr[i - 1]):
            cur = board_arr[i - 1].pop(0)
            if board_res and board_res[-1] == cur:
                board_res.pop(-1)
                answer += 2
            else:
                board_res.append(cur)
    return answer
