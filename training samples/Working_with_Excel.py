import openpyxl
from openpyxl import load_workbook
from xlsxwriter import table
import tkFileDialog
import tkMessageBox


wb = load_workbook(filename = 'C:/Users/PeterH/Documents/test2.xlsx')
print(wb.get_sheet_names())
sheet_ranges = wb['testblatt']
print(sheet_ranges['C3'].value)
sheet_ranges['D2'] = 'Haus'
wb.save('C:/Users/PeterH/Documents/test2.xlsx')
print(sheet_ranges['D2'].value)
print(table)
tkMessageBox