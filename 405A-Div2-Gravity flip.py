if __name__ == '__main__':
    col = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    for item in lst:
        print(item, end=" ")
