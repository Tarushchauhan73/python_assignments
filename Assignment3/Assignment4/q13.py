def print_number_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


rows = int(input("Enter number of rows: "))
print_number_pattern(rows)