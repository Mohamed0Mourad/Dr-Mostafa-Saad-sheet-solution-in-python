rows = int(input())
lst = [0] * rows
for row in range(rows):
    lst[row] = list(map(int, input().split()))
lsty = [sum(row) >= 2 for row in lst]
print(lsty.count(True))
