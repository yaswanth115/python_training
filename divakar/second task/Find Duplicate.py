def duplicate_characters(text):
    duplicates = []

    for char in text:
        if text.count(char) > 1 and char not in duplicates:
            duplicates.append(char)

    print("Duplicate characters:", duplicates)


text = "programming"
duplicate_characters(text)