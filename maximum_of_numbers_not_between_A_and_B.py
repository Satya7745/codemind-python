n=int(input())
l=[int(i) for i in input().split()]
A,B=[int(i) for i in input().split()]
temp=[]
for ele in l:
    if ele<A or ele>B:
        temp.append(ele)
if len(temp)==0:
    print(-1)
else:
    print(max(temp))   