
def swap(s, i , j):
    t = list(s)
    t[i], t[j] = t[j], t[i]
    return "".join(t)

def perm_stack(s):
    st = []

    st.append((s,0))

    while not len(st)==0:

        t = st.pop()
        if t[1]==len(s):
            print t[0]
        else:
            for i in range(t[1], len(s)):
                s1 = swap(t[0], t[1], i)
                st.append((s1, t[1]+1))
                

print(perm_stack("abc"))

#http://www.pythontutor.com/visualize.html#togetherjs=2NHsgGGsBy