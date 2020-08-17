import sys

n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
cnt = 0

for _,v in enumerate(nums):
    if v == n:
        cnt +=1
print(cnt)
