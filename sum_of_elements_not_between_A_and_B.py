n=int(input())
L=[int(i) for i in input().split(" ")]
A,B=[int(i) for i in input().split(" ")]
s=0
for ele in L:
    if ele<A or ele>B:
        s=s+ele
print(s)