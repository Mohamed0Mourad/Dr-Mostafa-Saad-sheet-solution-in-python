def read_matrix():
    lst = [0] * 5
    for i in range(5):
        lst[i] = list(map(int, input().split()))

    return lst


if __name__ == '__main__':
    lst_2d = read_matrix()
    for i in range(5):
        for j in range(5):
            if lst_2d[i][j] == 1:
                x = i
                y = j
                break
    print(abs(x - 2) + abs(y - 2))
