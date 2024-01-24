if __name__ == '__main__':
    s = input()
    cnt_up = 0
    cnt_lo = 0
    for c in s:
        if c.isupper():
            cnt_up += 1
        else:
            cnt_lo += 1
    if cnt_lo < cnt_up:
        print(s.upper())
    else:
        print(s.lower())
