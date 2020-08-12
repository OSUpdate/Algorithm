import sys
def a(n,i):
    j = 1
    for m in range(i):
        j*=10
    t = n%j
    return n - t + b(t,i)

def b(n,i):
    j = 1
    for m in range(1,i):
        j*=10
    if n>=5*j:
        return 10*j
    return 0
n = int(sys.stdin.readline())

if n> 10:
    i = 100
    j = 1
    m = a(n,j)
    while m > i:
        j+=1
        m = a(m,j)
        i *= 10
    print(m)
else:
    print(n)