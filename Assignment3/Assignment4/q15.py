class Matrix:

    def display_pattern(self, rows):
        for i in range(rows):
            for j in range(1, rows + 1):
                print(j, end=" ")
            print()

    def display_reverse_pattern(self, rows):
        for i in range(rows):
            for j in range(rows, 0, -1):
                print(j, end=" ")
            print()


matrix = Matrix()

print("Normal Pattern:")
matrix.display_pattern(4)

print("\nReverse Pattern:")
matrix.display_reverse_pattern(4)
print("\n")