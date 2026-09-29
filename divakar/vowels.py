def count_vowels(word):
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in word:
       if i in vowels:
            count += 1
    return count
word = "programming"
result = count_vowels(word)

print(result)