wires = int(input())
b_on_wires = list(map(int, input().split()))
m = int(input())
while m:
    x, y = map(int, input().split())
    x -= 1
    if x != 0:
        b_on_wires[x - 1] += y - 1
    if x != wires - 1:
        b_on_wires[x + 1] += b_on_wires[x] - y

    b_on_wires[x] = 0
    m -= 1
for i in b_on_wires:
    print(i)
