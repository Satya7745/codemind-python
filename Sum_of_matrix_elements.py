
n=int(input())
m=int(input())
e=[]
for i in range(1,n+1):
    l=list(map(int,input().split()))
    s=sum(l)
    e.append(s)
print(sum(e))
