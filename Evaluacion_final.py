peliculas = {
    "Drama": [],
    "Comedia": [],
    "Suspenso": [],
    "Terror": []
}


def cargar_pelicula():
    genero = input("Ingrese el género de la película (Drama, Comedia, Suspenso, Terror): ")
    nombre_pelicula = input("Ingrese el nombre de la película: ")
    peliculas[genero].append(nombre_pelicula)
    print("Película cargada exitosamente.")


def mostrar_peliculas():
       for genero, lista_peliculas in peliculas.items():
           print("\nPeliculas en el genero", genero)
           for pelicula in lista_peliculas:
               print("-", pelicula)
               
def menu():
    while True:
        print("\nMenu:")
        print("1. Cargar película")
        print("2. Mostrar películas")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")


        if opcion == "1":
            cargar_pelicula()
        elif opcion == "2":
            mostrar_peliculas()
        elif opcion == "3":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
menu()