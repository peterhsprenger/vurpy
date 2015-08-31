import os
import subprocess
import re
sejda = 'C:\\sejda-console-1.0.0.M9-bin\\bin\\sejda-console.bat'

# escholar = ['C:\\Users\\PeterH\\Documents\\UTB\\9783647595283.pdf', 'C:\\Users\\PeterH\\Documents\\UTB\\9783647595290.pdf', 'C:\\Users\\PeterH\\Documents\\UTB\\9783647595306.pdf', 'C:\\Users\\PeterH\\Documents\\UTB\\9783647595313.pdf', 'C:\\Users\\PeterH\\Documents\\UTB\\9783647595320.pdf', 'C:\\Users\\PeterH\\Documents\\UTB\\9783647595337.pdf', 'C:\\Users\\PeterH\\Documents\\UTB\\9783647595344.pdf', 'C:\\Users\\PeterH\\Documents\\UTB\\9783647595351.pdf', 'C:\\Users\\PeterH\\Documents\\UTB\\9783647595412.pdf']
escholar = ['C:\\Users\\PeterH\\Documents\\UTB\\9783647460581.pdf', 'C:\\Users\\PeterH\\Documents\\UTB\\9783647490601.pdf', 'C:\\Users\\PeterH\\Documents\\UTB\\9783647402505.pdf']
# escholar = os.listdir('C:\\Users\\PeterH\\Documents\\UTB\\')
print escholar

# durchlaufe die Dateien im Verzeichnis und call sejda tools and split document

splitted = []

targetpath_tmp = 'C:\\Users\\PeterH\\Documents\\UTB\\TMP'
'''
for pdf in escholar:
    call = sejda
    call += ' splitbybookmarks'
    call += ' -f '
    call += pdf
    call += ' -o '
    call += targetpath_tmp
    call += ' -l 1'
    call += ' -e ^Table.*'
    print '\n', call
    subprocess.call(call)
    print '\nsejda-console has completed.\n\n'
'''
parts = os.listdir(targetpath_tmp)
print parts
for part in parts:
    if part == 'Thumbs.db':
        parts.remove(part)
    else:
        parts.remove
        part = 'C:\\Users\\PeterH\\Documents\\UTB\\TMP\\' + part
        parts.append(part)
print "Parts", parts

'''
targetpath_iv = 'C:\\Users\\PeterH\\Documents\\UTB\\IV'

for part in parts:
    call = sejda
    call += ' splitbybookmarks'
    call += ' -f '
    call += part
    call += ' -o '
    call += targetpath_iv
    call += ' -l 1'
    call += ' -e ^Body.*'
    print '\n', call
    subprocess.call(call)
    print '\nsejda-console has completed.\n\n'

splitted = os.listdir(targetpath_iv)
print splitted
'''
'''
for s in splitted:
    if s == 'Thumbs.db':
        del s
    else:
        s.replace(s, 'C:\\Users\\PeterH\\Documents\\UTB\\TMP\\' + s)
print "Splitted", splitted
'''
'''
for s in splitted:
    s = re.findall('[0-9]_(.*)',s)
    s.replace(part, 'C:\\Users\\PeterH\\Documents\\UTB\\TMP\\' + s)
print "splitted", splitted
'''