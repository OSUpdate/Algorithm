if i[0] != 1 and i[1] == 1:
        ans = arr[i[2]-1][i[3]-1] - arr[i[0]-2][i[3]-1]
        print(ans)
        continue
    if i[0] == 1 and i[1] != 1:
        ans = arr[i[2]-1][i[3]-1] - arr[i[2]-1][i[1]-2]
        print(ans)
        continue