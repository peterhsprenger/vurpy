import PyPDF2
from PyPDF2 import *
from PyPDF2.xmp import XmpInformation

pdf = open('C:\Users\PeterH\Documents\UTB\9783647595290.pdf')
ft = pdf.read()
# print ft


handle = ft.XmpInformation.pdf_producer
print handle
