peliculas = {
    "Drama": [],
    "Comedia": [],
    "Suspenso": [],
    "Terror": []
}

def cargar_pelicula():
    genero = input("Ingrese el género de la película (Drama, Comedia, Suspenso, Terror): ")
    nombre_pelicula = input("Ingrese el nombre de la película: ")
    
    if genero in peliculas:
        peliculas[genero].append(nombre_pelicula)
        print("Película cargada exitosamente en la categoría " + genero)
    else:
        print("Género no válido. Por favor, elija un género válido.")

def mostrar_peliculas():
    for genero, lista_peliculas in peliculas.items():
        if lista_peliculas:
            print(genero + ":")
            for pelicula in lista_peliculas:
                print("- " + pelicula)
        else:
            print("No hay películas en la categoría " + genero)

def menu():
    while True:
        print("\nMenú:")
        print("1. Cargar película")
        print("2. Mostrar películas")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cargar_pelicula()
        elif opcion == "2":
            mostrar_peliculas()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción valida.")