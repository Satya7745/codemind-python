s=input()
l=0
r=0
rst=0
for s_str in s:
    if s_str=='L':
        l+=1
    elif s_str=='R':
        r+=1
    if l==r:
        rst+=1
        l=0
        r=0
print(rst)