n=int(input())
a=list(map(int,input().split()))
k=[]
for i in range(n):
    if a[i]%2!=0:
        k.append(i)
print(k.pop())