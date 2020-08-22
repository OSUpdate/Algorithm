import sys
import math
def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

n = str(sys.stdin.readline().rstrip('\n'))
cnt = [0]*10
for i,v in enumerate(n):
    num = int(v)
    if num == 0 and i ==0:
        cnt[num] += 1
        break
    cnt[num] += 1
    
cnt[6] += cnt[9]
cnt[9] = 0
cnt[6] = int(normal_round(float(cnt[6])/2))
print(max(cnt))

