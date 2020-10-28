from sys import stdin
input = stdin.readline

n1,m1 = map(int,input().split())
arr1,arr2 = [],[]
ans = []
for _ in range(n1):
    arr1.append(list(map(int,input().split())))

n2,m2 = map(int, input().split())
for _ in range(n2):
    arr2.append(list(map(int,input().split())))

for v1 in arr1:
    tmp = [0]*m2
    
    for i in range(m2):
        v = 0
        for j in range(n2):
            v += v1[j]*arr2[j][i]
        tmp[i] = v
    ans.append(tmp)
for i in ans:
    for p in i:
        print(p, end =' ')
    print()
[print(p) for p in [i for i in ans]]