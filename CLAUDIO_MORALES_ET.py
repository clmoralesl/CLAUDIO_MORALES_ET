import csv
import random
diccionario_trabajadores = {}
trabajadores = ["Juan Perez", "Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]

def sueldos_totales():
    suma_total=0
    for valores in diccionario_trabajadores.values():
        suma_total+=valores
    return suma_total
def imprimir_sueldo(sueldo):
    print('Nombre Empleado\t\tSueldo\n')
    for nombres in sueldo:
        print(f'{nombres}',end="")
        print(f'\t\t${diccionario_trabajadores[nombres]}')
def sueldos_aleatorios():
    print ('-----Asignar sueldos aleatorios-----')
    if diccionario_trabajadores:
        print('No se pueden volver a asignar lo sueldos, volviendo al menú principal')
        return
    for nombres in trabajadores:
        sueldo_aleatorio=random.randint(300000,2500000)
        diccionario_trabajadores [nombres] = sueldo_aleatorio
    print ('Sueldos asignados exitosamente, volviendo al menú principal')
def clasificar_sueldos():
    print ('-----Clasificar sueldos-----')    
    sueldos_bajos=[]
    sueldos_medios=[]
    sueldos_altos=[]
    for clave, valor in diccionario_trabajadores.items():
        if valor <= 800000:
            sueldos_bajos.append(clave)
        elif valor <2000000:
            sueldos_medios.append(clave)
        else :
            sueldos_altos.append(clave)
    print(f'Sueldos menores a $800.000 TOTAL:{len(sueldos_bajos)}')
    imprimir_sueldo(sueldos_bajos)
    print(f'\nSueldos entre $800.000 y $2.000.000 TOTAL:{len(sueldos_medios)}')
    imprimir_sueldo(sueldos_medios)
    print(f'\nSueldos superiores a $2.000.000 TOTAL:{len(sueldos_altos)}')
    imprimir_sueldo(sueldos_altos)
    print(f'\nTOTAL SUELDOS: ${sueldos_totales()}')
def ver_estadistica():
    print ('-----Ver estadísticas-----')  
    sueldo_alto=0
    sueldo_bajo=2500001
    promedio_sueldos=(sueldos_totales()/10)
    media_geometrica=1
    for sueldos in diccionario_trabajadores.values():
        if sueldos>sueldo_alto:
            sueldo_alto=sueldos
        if sueldos<sueldo_bajo:
            sueldo_bajo=sueldos
        media_geometrica*=sueldos
    media_geometrica=(media_geometrica**(1/10))
    print(f'- Sueldo más alto : ${sueldo_alto}')
    print(f'- Sueldo más bajo : ${sueldo_bajo}')
    print(f'- Promedio de sueldos : ${promedio_sueldos}')
    print(f'- Media geométrica : ${media_geometrica}')
def reporte_de_sueldos():
    print ('-----Reporte de sueldos-----')  
    matriz_sueldos=[]
    for nombres,sueldos in diccionario_trabajadores.items():
        lista_sueldos=[]
        descuento_salud=(round((sueldos*0.07),3))
        descuento_afp=(round((sueldos*0.12),3))
        sueldo_liquido=(round(((sueldos)-(descuento_afp)-(descuento_salud)),3))
        lista_sueldos.append(nombres)
        lista_sueldos.append(sueldos)
        lista_sueldos.append(descuento_salud)
        lista_sueldos.append(descuento_afp)
        lista_sueldos.append(sueldo_liquido)
        matriz_sueldos.append(lista_sueldos)
    print('Nombre empleado\t\tSueldo Base\t\tDescuento Salud\t\tDescuento Afp\t\tSueldo Líquido')
    for datos in matriz_sueldos:
        print(f'{datos[0]}\t\t${datos[1]}  \t\t${datos[2]}\t\t${datos[3]}\t\t${datos[4]}')
    importar_datos(matriz_sueldos)
def importar_datos(matriz):
    with open('reporte_trabajadores.csv', 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido'])
        for filas in matriz:
            escritor_csv.writerow(filas)
        print('\nDatos exportados exitosamente al archivo "reporte_trabajadores.csv"')
def salir_programa():
    print('Finalizando programa…\nDesarrollado por Claudio Morales\nRUT 19.328.881-2')
def mostrar_menu():
    print('''
   Seleccione una opción:
1. Asignar sueldos aleatorios
2. Clasificar sueldos
3. Ver estadísticas.
4. Reporte de sueldos
5. Salir del programa
''')
print("Bienvenido al registro de Empresas DC")
while True:
    mostrar_menu ()
    try:
        opc_menu = int(input())
        if opc_menu <1 or opc_menu >5:
            print('Opción inválida, vuelva a intentar')
            continue
    except ValueError:
        print('Error de dato, vuelva a intentar')
        continue
    match opc_menu: 
        case 1:
            sueldos_aleatorios()
        case 2:
            clasificar_sueldos()
        case 3:
            ver_estadistica()
        case 4:
            reporte_de_sueldos()
        case 5:
            salir_programa()
            break

    
