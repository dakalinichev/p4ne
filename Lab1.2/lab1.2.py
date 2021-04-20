from matplotlib import pyplot
from openpyxl import load_workbook

#dir.load_workbook()
#!!!Нужно как-то добавить путь чтобы не писать полный путь.
wb=load_workbook('C:\\Users\\Kalinichev\\Documents\\VisualStudioCode_local\\dakalinichev_p4ne\\p4ne\Lab1.2\\data_analysis_lab.xlsx')# Загрузить таблицу Excel из файла в переменную wb
sheet = wb['Data'] # Загрузить лист с именем "Data" в переменную sheet #type(sheet)
sheet.values['A'][1:] # Получить содержимое колонки A в виде списка

def getvalue(x):
    return x.value
dir(map)

list(map(getvalue, sheet['A'][1:]))
map(getvalue, sheet['A'][1:]) # Преобразовать содержимое колонки A в список, содержащий только значения (без форматирования и т. п.)
List1=map(getvalue, sheet['A'][1:])

list_x=list(map(getvalue, sheet['A'][1:]))
list_y=list(map(getvalue, sheet['C'][1:]))
pyplot.plot(list_x, list_y, label="Метка") # Построить график по точкам, в первом списке значения по оси X, во втором — значения по оси Y 
pyplot.show() # показать график
