def anti_vowel(text):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for letter in text:
        if letter in vowels:
            text = text.replace(letter,"")
    print  text
    

anti_vowel("Hallo")