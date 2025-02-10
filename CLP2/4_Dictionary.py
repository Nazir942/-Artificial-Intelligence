def count(text):
    words = text.lower().split()
    word_count = {}
    for word in words:
        word = word.strip()
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

text = "Python is fun and coding in Python is great"
store = count(text)
print(store)
