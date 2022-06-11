def r(s):
    st=list()
    for i in range(len(s)):
        if s[i]!=" ":
            st.append(s[i])
        else:
            while len(st)>0:
                print(st[-1],end="")
                st.pop()
            print(end=" ")
    while len(st)>0:
        print(st[-1],end="")
        st.pop()
s=input()
r(s)