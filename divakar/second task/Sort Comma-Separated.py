def sort_words(text):
    words = text.split(",")

    words.sort()

    return ",".join(words)


text = "without,hello,bag,world"

result = sort_words(text)

print(result)