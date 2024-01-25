n = int(input())
lst = list(map(int, input().split()))
n_crime = n_hired = 0
for item in lst:
    if item > 0:
        n_hired += item
    elif item < 0 and n_hired > 0:
        n_hired -= 1
    elif item < 0:
        n_crime += 1

print(n_crime)
