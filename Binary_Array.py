n=int(input())
l=[int(i) for i in input().split()]
flag=0
for ele in l:
    if ele!=0 and ele!=1:
        flag=1
        break
if flag==0:
    print("True")
else:
    print("False")