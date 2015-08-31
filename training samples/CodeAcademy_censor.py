''' Write a function called censor that takes two strings, text and word, as input. 
It should return the text with the word you chose replaced with asterisks.

For example:
censor("this hack is wack hack", "hack") 
should return
"this **** is wack ****"

Assume your input strings won't contain punctuation or upper case letters.
The number of asterisks you put should correspond to the number of letters in the censored word.'''

def censor(text, word):
    l = len(word)
    for part in text:
        text = text.replace(word, "*" * l)
    print text
    
    
t = "im verlag ist das verlagswesen enthalten"
w = "verlag"
censor(t, w)    