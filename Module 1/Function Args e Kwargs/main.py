def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f'Sum: {sum_total}')


def presentation(**data):
    for key, value in data.items():
        print(f'{key}: {value}')


sum(5, 7, 3, 1, 0)

presentation(name='John', age=25, city='San Francisco')