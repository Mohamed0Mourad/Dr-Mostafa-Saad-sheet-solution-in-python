n, b, d = map(int, input().split())
total_oranges = list(map(int, input().split()))
cnt = 0
overflow = 0
for i in total_oranges:
    if i <= b:
        overflow += i
    if overflow > d:
        cnt += 1
        overflow = 0
print(cnt)
