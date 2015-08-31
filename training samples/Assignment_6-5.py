# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
# Convert the extracted value to a floating point number and print it out.

# VARIANTE 1: erstes Leerzeichen von rechts finden
text = "X-DSPAM-Confidence:    0.8475"
startpos = text.rfind(' ')
number = text[startpos+1:]
print float(number)

# VARIANTE 2: Doppelpunkt finden, Leerzeichen ab Doppelpunkt loeschen
startpos = text.find(':')
text2 = text[startpos+1:]
text2.lstrip()
print float(text2)