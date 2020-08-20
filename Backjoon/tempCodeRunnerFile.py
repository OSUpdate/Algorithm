import sys

string = str(sys.stdin.readline())
string.lower()
alpha = [0]*26
for i in range(97,123):
    for j in string:
        if j == chr(i):
            alpha[ord(j)-97] +=1
if alpha.count(max(alpha)) >= 2:
    print("?")
else:   
    print(max(alpha))