def count_letters_digits(text):
    letters = 0
    digits = 0

    for char in text:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1

    print("LETTERS", letters)
    print("DIGITS", digits)


text = "hello world! 123"

count_letters_digits(text)