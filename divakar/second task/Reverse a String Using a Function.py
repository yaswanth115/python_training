def reverse_string(text):
    reverse = ""

    for i in text:
        reverse = i + reverse

    return reverse


print(reverse_string("Python"))