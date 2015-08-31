def reverse(text):
    l = len(text) - 1
    reverse = str()
    for letter in text:
        reverse += text[l]
        l = l - 1
    return reverse
