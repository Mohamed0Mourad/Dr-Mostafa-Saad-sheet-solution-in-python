n = int(input())
cards = list(map(int, input().split()))

sereja_points = 0
dima_points = 0

for i in range(n):
    if i % 2 == 0:
        sereja_points += max(cards[0], cards[-1])
    else:
        dima_points += max(cards[0], cards[-1])

    if cards[0] > cards[-1]:
        cards.pop(0)
    else:
        cards.pop()

print(sereja_points, dima_points)
