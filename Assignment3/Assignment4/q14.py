class PatternGenerator:

    def star_triangle(self, rows):
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end=" ")
            print()

    def inverted_triangle(self, rows):
        for i in range(rows, 0, -1):
            for j in range(i):
                print("*", end=" ")
            print()

    def number_triangle(self, rows):
        for i in range(1, rows + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()


pattern = PatternGenerator()

print("Star Triangle:")
pattern.star_triangle(5)

print("\nInverted Triangle:")
pattern.inverted_triangle(5)

print("\nNumber Triangle:")
pattern.number_triangle(5)