def ugly(n):
    while n>0:
        flag=0
        if n%5==0:
            n=n//5
            flag=1
        elif n%3==0:
            n=n//3
            flag=1
        elif n%2==0:
            n=n//2
            flag=1
        if flag==0 or n==1:
            break
    if n==1:
        print("Ugly Number")
    else:
        print("Not Ugly Number")
n=int(input())
ugly(n)