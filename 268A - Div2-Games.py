n = int(input())
cnt = 0
lsth = []
lstg = []
for i in range(n):
    h, g = map(int, input().split())
    lsth.append(h)
    lstg.append(g)
for i in range(n):
    for j in range(n):
        if lsth[i] == lstg[j]:
            cnt += 1
print(cnt)
