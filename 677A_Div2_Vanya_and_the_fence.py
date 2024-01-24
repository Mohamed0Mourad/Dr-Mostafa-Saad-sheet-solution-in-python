n, h = map(int, input().split())
lst = list(map(int, input().split()))
sum = 0
for item in lst:
    if item <= h:
        sum += 1
    else:
        sum += 2
print(sum)
