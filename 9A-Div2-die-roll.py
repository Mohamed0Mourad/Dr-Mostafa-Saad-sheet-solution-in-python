a, b = map(int, input().split())
dot = max(a, b)
prob_lst = ['1/6', '1/3', '1/2', '2/3', '5/6', '1/1']
print(prob_lst[6-dot])
