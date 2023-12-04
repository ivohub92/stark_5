import json
import csv
import os

# Punto 1.1: leer archivo 
def leer_archivo(archivo_ingresado):
    try: #intenta esto
        # abrir archivo en  codificacion utf-8
        with open(archivo_ingresado, 'r', encoding='utf-8') as archivo:
            # Lee  archivo y  almacena en 'contenido'
            contenido = archivo.read()         
        
    except Exception as e:
        #mensaje_error
        print(f'Error al leer el archivo {archivo_ingresado}: {str(e)}')
        # Devuelve False para indicar que ha ocurrido un error
        contenido= False
    return contenido
    

# Punto 1.2 guardar contenido en un archivo
def guardar_archivo(archivo_guardar, contenido):
    try:
        # Intenta abrir el archivo en modo escritura ('w') con codificación utf-8
        with open(archivo_guardar, 'w', encoding='utf-8') as archivo:
            # Escribe el contenido en el archivo
            archivo.write(contenido)
        # mensaje que indica que se creo con exito el archivo
        print(f"Se creó el archivo: {archivo_guardar}") 
        guardado= True       
        
    except Exception as e:
        # imprime un mensaje de error si falla lo anterior
        print(f"Error al crear el archivo {archivo_guardar}: {str(e)}")
        guardado= False

    return guardado

# Punto 1.3: Generar un archivo CSV
def generar_csv(nombre_archivo, lista_superheroes):   
    if lista_superheroes:
        # agrego encabezados de columnas del archivo csv
        contenido_csv = "nombre,identidad,empresa,altura,peso,genero,color_ojos,color_pelo,fuerza,inteligencia\n"
        
        # recorro lista y agrego cada héroe al CSV
        for heroe in lista_superheroes:
            contenido_csv += f"{heroe['nombre']},{heroe['identidad']},{heroe['empresa']},{heroe['altura']},{heroe['peso']},{heroe['genero']},{heroe['color_ojos']},{heroe['color_pelo']},{heroe['fuerza']},{heroe['inteligencia']}\n"

        # guardamos el archivo
        return guardar_archivo(nombre_archivo, contenido_csv)
    else:        
        print("La lista de superhéroes está vacía.") 
        return False       
        

# Punto 1.4
def leer_csv(nombre_archivo):
    try:
        lista_superheroes = []
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)
            for row in lector_csv:
                lista_superheroes.append(row)
        return lista_superheroes
    except Exception as e:
        print(f"Error al leer el archivo {nombre_archivo}: {str(e)}")
        return False
    

def generar_json(nombre_archivo, lista_superheroes, nombre_lista):
    if lista_superheroes: 
        # Crear un diccionario con una sola clave (nombre_lista)
        diccionario_superheroes = {nombre_lista: lista_superheroes}
        try:
            with open(nombre_archivo, 'w') as archivo_json:
                json.dump(diccionario_superheroes, archivo_json, indent=4) 
            print(f"Se creó el archivo JSON: {nombre_archivo}")
            return True
        except Exception as e:
            print(f"Error al crear el archivo JSON {nombre_archivo}: {str(e)}")
            return False
    else:
        print("La lista de superhéroes está vacía.")
        return False
    
def normalizar_datos(lista_superheroes):
    # Convierte las alturas, pesos y fuerzas de los superhéroes a enteros
    for heroe in lista_superheroes:
        heroe['altura'] = float(heroe['altura'])
        heroe['peso'] = float(heroe['peso'])
        heroe['fuerza'] = float(heroe['fuerza'])


def leer_json(nombre_archivo, nombre_lista):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            retorno = datos.get(nombre_lista, [])
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
        retorno = False
    except Exception as e:
        print(f"Error al leer el archivo {nombre_archivo}: {e}")
        retorno = False
    return retorno


def ordenar_heroes_ascendente(heroes, clave):
    n = len(heroes)
    for i in range(n):
        for j in range(0, n-i-1):
            if float(heroes[j][clave]) < float(heroes[j+1][clave]):
                heroes[j], heroes[j+1] = heroes[j+1], heroes[j]
    return heroes

def ordenar_heroes_descendente(heroes, clave):
    n = len(heroes)
    for i in range(n):
        for j in range(0, n-i-1):
            if float(heroes[j][clave]) > float(heroes[j+1][clave]):
                heroes[j], heroes[j+1] = heroes[j+1], heroes[j]
    return heroes

def ordenar_heroes_por_clave(heroes, clave):
    direccion = input("¿Cómo quieres ordenar los héroes? ('asc' para ascendente, 'desc' para descendente): ").lower()
    
    if direccion == 'asc':
        heroes_ordenados = ordenar_heroes_ascendente(heroes, clave)
    elif direccion == 'desc':
        heroes_ordenados = ordenar_heroes_descendente(heroes, clave)
    else:
        print("Opción no válida. Se devolverá la lista sin ordenar.")   

    return heroes_ordenados