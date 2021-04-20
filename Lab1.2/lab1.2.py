from matplotlib import pyplot
from openpyxl import load_workbook

#dir.load_workbook()
wb = load_workbook('data_analysis_lab.xlsx') # Загрузить таблицу Excel из файла в переменную wb
sheet = wb['Data'] # Загрузить лист с именем "Data" в переменную sheet
sheet['A'][1:] # Получить содержимое колонки A в виде списка
