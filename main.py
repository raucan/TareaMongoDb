import random
import pymongo

con = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = con.list_database_names()

db = con["db"]
col = db["diccionario"]

def principal():
    menu = """
1) Agregar nueva palabra
2) Editar palabra
3) Eliminar palabra 
4) Ver listado de palabras
5) Buscar significado
6) Salir
Elige: """
    eleccion = ""
    while eleccion != "6":
        eleccion = input(menu)
        if eleccion == "1":
            palabra = input("Ingresa la palabra: ")
            posible_significado = buscar_significado_palabra(palabra)
            if posible_significado:
                print(f"La palabra '{palabra}' ya existe")
            else:
                significado = input("Ingresa el significado: ")
                agregar_palabra(palabra, significado)
                print("Palabra agregada")
        if eleccion == "2":
            palabra = input("Ingresa la palabra que quieres editar: ")
            nuevo_significado = input("Ingresa el nuevo significado: ")
            editar_palabra(palabra, nuevo_significado)
            print("Palabra actualizada")
        if eleccion == "3":
            palabra = input("Ingresa la palabra a eliminar: ")
            eliminar_palabra(palabra)
        if eleccion == "4":
            print("=== Lista de palabras ===")
            palabras = obtener_palabras()

        if eleccion == "5":
            palabra = input(
                "Ingresa la palabra de la que quieres saber el significado: ")
            significado = buscar_significado_palabra(palabra)

def agregar_palabra(palabra, significado):
    palabras = {"_id": random.randint(0, 9999), "palabra": palabra, "significado": significado}
    resultado = col.insert_one(palabras)

def eliminar_palabra(palabra):
    query = {"palabra": palabra}
    col.delete_one(query)

def obtener_palabras():
    for palabra in col.find():
            print(palabra)
            pass

def buscar_significado_palabra(palabra):

    query = {"palabra" : palabra}
    resultado = col.find(query)
    for r in resultado:
        print("Encontrado")
        print((resultado))
        print(r)

def editar_palabra(palabra, nuevo_significado):
    query = {"palabra": palabra}
    col.delete_one(query)
    palabras = {"_id": random.randint(0, 9999), "palabra": palabra, "significado": nuevo_significado}
    resultado = col.insert_one(palabras)

if __name__ == '__main__':
    principal()


