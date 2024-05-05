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

def evaluacion(datos):
    estudiantes= []
    for x in range(len(datos)):
        if x==0:
            pass
        elif (datos[x][1]>16) and (datos[x][2]== 'F') and (datos[x][4]<3):
                estudiantes.append(datos[x])
    return estudiantes

def crear_archivo():
    archivo= open('archivo_estudiantes.txt', 'w')
    archivo.close()
    
def agg_datos(arc,data):
    arch= open(arc, 'a')
    arch.write(data)
    arch.close()
    
def read(arc):
    archivo= open(arc, 'r')
    contenido= archivo.read()
    archivo.close()
    return contenido


validacion= evaluacion(data)
print(validacion)
crear_archivo()
agg_datos('archivo_estudiantes.txt', 'Nombre de los estudiantes de sexo femenino, mayores a 16 y sisben inferior a 3\n')
for x in validacion:
    new_list=  list(x)
    agg_datos('archivo_estudiantes.txt', f'Nombre: {x[0]} \nEdad: {x[1]} \nSexo: {x[2]} \nResidencia: {x[3]} \nSisben: {x[4]} \n\n')
