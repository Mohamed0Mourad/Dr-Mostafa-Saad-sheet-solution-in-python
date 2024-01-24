start = perf_counter()
n = int(input())
cnt = 1
f_magnit = int(input())
for i in range(1, n):
    s = int(input())
    if f_magnit != s:
        f_magnit = s
        cnt +=1

print(cnt)
