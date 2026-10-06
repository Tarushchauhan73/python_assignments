def find_largest(a, b, c):
    largest = a

    if b > largest:
        largest = b

    if c > largest:
        largest = c

    return largest


print(find_largest(10, 25, 40))