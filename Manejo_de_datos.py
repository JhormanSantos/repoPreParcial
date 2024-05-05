#Crear un codigo en donde en un archivo txt envie a los estudiantes segun las siguientes condiciones:
#Que sea mayor de 16 años, femenina y su sisben sea inferior a 3

import openpyxl as op

def leer_excel(archivo):
    libro= op.load_workbook(archivo)
    hoja= libro.active
    data= []
    for x in hoja.iter_rows(values_only= True):
        data.append(x)
    libro.close()
    return data

data= leer_excel('Colegio.xlsx')
print(data)