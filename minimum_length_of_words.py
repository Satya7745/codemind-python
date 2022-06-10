def fml(w):
    m=99
    for word in w:
        if len(word)<m:
            m=len(word)
    return m
words=input().split(' ')
res=fml(words)
print(res)