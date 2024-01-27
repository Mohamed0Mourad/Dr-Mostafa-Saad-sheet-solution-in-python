lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']
pos = 0
cnt = 0
s = input()
for c in s:
    dif = abs(lst.index(c) - pos)
    if dif < 13:
        cnt += dif
        pos = lst.index(c)
    else:
        cnt += 26 - dif
        pos = lst.index(c)
print(cnt)
