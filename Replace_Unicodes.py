# -*- coding: iso-8859-1, utf-8 -*-
import re


files_to_change = 'F:\VLBGoldFiles\isbnlist9783525.txt'

input = open(files_to_change)

for line in input:
    line = re.sub(r'\xc3\xa4', '�', line)
#    replace_oe
#    replace_ue
#    replace_AE
#    replace_OE
#    replace_UE
#    replace_sz
#    \xc3\xbc    �
#    \xc3\x96    �
#    \xc3\xa4    �
#    \xc3\xb6    �

