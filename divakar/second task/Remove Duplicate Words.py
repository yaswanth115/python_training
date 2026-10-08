def remove_duplicates_and_sort(text):
    words = text.split()

    unique_words = set(words)

    result = sorted(unique_words)

    return " ".join(result)


text = "hello world practice makes perfect and hello world again"

print(remove_duplicates_and_sort(text))