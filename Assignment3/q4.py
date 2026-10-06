def count_vowels(text):
    count = 0

    for char in text:
        if char in "aeiouAEIOU":
            count += 1

    return count


result = count_vowels("Tarush chauhan")

print("Number of vowels:", result)