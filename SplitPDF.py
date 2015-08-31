import operator
import os
import subprocess
import sys
import time

import PyPDF2 as pyPdf
from GetPDF_Bookmarks import GetPDFBookmarks

# need to have sejda-console installed
# change this to point to your installation
sejda = 'C:\\sejda-console-1.0.0.M9-bin\\bin\\sejda-console.bat'

if __name__ == '__main__':
    t0= time.time()

    # get the name of the file to split as a command line arg
    pdfname = '9783647595320.pdf' #sys.argv[1]

    # open up the pdf
    pdf = GetPDFBookmarks(open('C:\\Users\\PeterH\\Documents\\UTB\\9783647595320.pdf', 'rb'))

    # build list of (pagenumbers, newFileNames)
    splitlist = [(1,'')] # Customize name of first section

    template = '%-5s  %s'
    print template % ('Page', 'Title')
    print '-'*72
    for t,p in sorted(pdf.getDestinationPageNumbers().iteritems(), key=operator.itemgetter(1)):

        # Customize this to get it to split where you want
        if t.startswith(''): # or t.startswith('Preface') or t.startswith('References'):

            print template % (p+1, t)

            # this customizes how files are renamed
            new = t.replace('Chapter ', 'Chapter')\
                   .replace(':  ', '-')\
                   .replace(': ', '-')\
                   .replace(' ', '_')
            splitlist.append((p+1, new))

    # call sejda tools and split document
    call = sejda
    call += ' splitbypages'
    call += ' -f "%s"'%pdfname
    call += ' -o . C:\\Users\\PeterH\\Documents\\UTB\\'
    call += ' -n '
    call += ' '.join([str(p) for p,t in splitlist[1:]])
    print '\n', call
    subprocess.call(call)
    print '\nsejda-console has completed.\n\n'

    # rename the split files
    for p,t in splitlist:
        old ='./%i_'%p + pdfname
        new = './' + t + '.pdf'
        print 'renaming "%s"\n      to "%s"...'%(old, new),

        try:
            os.remove(new)
        except OSError:
            pass

        try:
            os.rename(old, new)
            print' succeeded.\n'
        except:
            print' failed.\n'

    print '\ndone. Spliting took %.2f seconds'%(time.time() - t0)