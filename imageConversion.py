import PIL
from PIL import Image
import os
from os import listdir
from os.path import join, getsize

sources = dict()

for root, files in os.walk('F:\UTBeScholars\LIEFERUNG\CoverJPG2D'):
    sources = sources(root,files)
    print sources
    '''
    for r, f in sources.items():
        sources[r] = root
        for file in files:
            print file
#            sources[f] = file
#    print sources
'''    
    '''
    sources = sources.items()
    print sources.items()
    
    for f in files:
        print f
        img = Image.open(f)
        print img
        basewidth = 400
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        img.save('F:\UTBeScholars\LIEFERUNG\CoverJPG2D\9783847000709_resized.jpg')
'''