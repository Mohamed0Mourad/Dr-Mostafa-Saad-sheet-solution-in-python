l, b = map(int, input().split())
cnt = 0
while True:
    l = 3 * l
    b = 2 * b
    cnt += 1
    if l > b:
        print(cnt)
        break
