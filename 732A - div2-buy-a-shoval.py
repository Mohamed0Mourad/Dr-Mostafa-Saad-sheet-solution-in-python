k, r = map(int, input().split())
cnt = 1

while True:
    if (k * cnt) % 10 == r or (k * cnt) % 10 == 0:
        break
    else:
        cnt += 1
print(cnt)
