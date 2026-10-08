def analyze_numbers(numbers):
    positive = negative = even = odd = zero = 0

    for n in numbers:
        if n > 0:
            positive += 1
        elif n < 0:
            negative += 1
        else:
            zero += 1

        if n % 2 == 0:
            even += 1
        else:
            odd += 1

    return positive, negative, even, odd, zero

result = analyze_numbers([1, -2, 0, 4, -3])
print("Positive, Negative, Even, Odd, Zero:", result)