from funciones import *
import json
import csv 
import os
from data_stark import lista_personajes



normalizado= False
nombre_archivo_csv=""

while True:
    print("\nMenú:")
    print("1- Normalizar datos")
    print("2- Generar CSV")
    print("3- Listar héroes del archivo CSV ordenados por altura ascendente")
    print("4- Generar JSON")
    print("5- Listar héroes del archivo JSON ordenados por peso descendente")
    print("6- Ordenar lista por fuerza")
    print("7- Salir")

    opcion = input("Ingresa la opción deseada: ")

    if opcion == '1':
        # Normalizar datos
        normalizar_datos(lista_personajes)
        normalizado=True
        print("Datos normalizados correctamente")
    
    elif opcion == '2' and normalizado:
        # Generar CSV
        nombre_archivo_csv = "heroes.csv"
        lista_generada=generar_csv(nombre_archivo_csv, lista_personajes)           

    elif opcion == '3'and normalizado:
        # Listar héroes del archivo CSV ordenados por altura ASC
        
        lista_personajes_csv = leer_csv(nombre_archivo_csv)
        if lista_personajes_csv:
            lista_personajes_csv = ordenar_heroes_ascendente(lista_personajes_csv, "altura")
            print("Lista de héroes ordenados por altura ASC:")
            for heroe in lista_personajes_csv:
                print(heroe)
        else:
            print('generar archivo con opcion 2')

    elif opcion == '4'and normalizado:
        # Generar JSON
        nombre_archivo_json = "heroes.json"
        generar_json(nombre_archivo_json, lista_personajes, "heroes")            

    elif opcion == '5'and normalizado:
        # listar héroes del archivo json ordenados por peso descendebte
        nombre_archivo_json = "heroes.json"
        lista_personajes_json = leer_json(nombre_archivo_json, "heroes")
        if lista_personajes_json:
            lista_personajes_json = ordenar_heroes_descendente(lista_personajes_json, "peso")
            print("Lista de héroes ordenados por peso DESC:")
            for heroe in lista_personajes_json:
                print(heroe)

    elif opcion == '6'and normalizado:
        # ordenar lista por fuerza (preguntar al usuario)
        lista = ordenar_heroes_por_clave(lista_personajes, "fuerza")
        for heroe in lista:
                print(heroe)

    elif opcion == '7'and normalizado:
        # Salir        
        break
    elif int(opcion)>7 or int(opcion)<1:        
        print("Opción no válida. Ingresa un número del 1 al 7.")  
    elif normalizado== False:
        print('Error: Debe normalizar')
    else: 
        print('Opcion no valida')

    
    
    