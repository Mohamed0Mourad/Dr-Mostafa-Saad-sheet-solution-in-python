s = list(map(int, input().split()))
st = set()
for item in s:
    st.add(item)

print(4 - len(st))
