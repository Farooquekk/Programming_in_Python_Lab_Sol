def recursion(num):
    print(num)
    next = num - 3
    if next > 1:
        recursion(next)

recursion(11)