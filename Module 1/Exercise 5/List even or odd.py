def even_odd(list):
    odd = []
    even = []
    for i in list:
        if i % 2 == 0:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


print(even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
