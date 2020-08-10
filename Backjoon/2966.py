import sys
def func(data,ans,size):
    count = 0
    for i,a in enumerate(data):

        if(ans[i%size]==a):
            count += 1
    return count

Adrian = ['A','B','C']
Bruno = ['B','A','B','C']
Goran = ['C','C','A','A','B','B']
count = [0,0,0]
n = sys.stdin.readline()
ans = sys.stdin.readline()
count[0] = func(ans,Adrian,3)
count[1] = func(ans,Bruno,4)
count[2] = func(ans,Goran,6)
v = max(count)
print(v)
for i,a in enumerate(count):
    if(i==0 and a==v):
        print("Adrian")
    if(i==1 and a==v):
        print("Bruno")
    if(i==2 and a==v):
        print("Goran")
