import sys

while(1):
    arr = list(map(int,sys.stdin.readline().split()))
    if(arr[0]==-1):
        sys.exit()
    arr.pop();
    count = 0
    for v in arr:
        if v*2 in arr:
            count +=1
    print(count)