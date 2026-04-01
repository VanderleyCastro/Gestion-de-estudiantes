from servicios.archivo import save_student

def registro_estudiantes(estudiantes):
    while True:      
        try: 
            id_estudi = int(input("Ingrese el numero de identificacion: "))
            if id_estudi <= 0:
                print("¡No negativos!")
                continue  

            if any(e["id"] == id_estudi for e in estudiantes):
                print("Esta identificacion ya existe")
                continue  

            break
        except ValueError:
            print("Identificacion invalida")

    nombre_estudi = input("Ingrese el nombre: ")
    grado = input("Ingrese el curso: ")

    while True:
        try:
            edad = int(input("Ingrese edad: "))
            if edad <= 0:
                print("Edad invalida")
                continue
            break
        except ValueError:
            print("Edad invalida")
    while True:  
     estado = input("Estado (activo/inactivo): ").lower()
     if any (c.isdigit()for c in estado):
        print("\nNo se permiten numeros. Intente nuevamente!")
        continue
    
     if estado not in ["activo","inactivo"]:
         print("\nSolo puedes escribir 'activo' o 'inactivo'")
         continue
     break
    

    estadoBoo = True if estado == "activo" else False

    estudiante = {
        "id": id_estudi,
        "nombre": nombre_estudi,
        "grado": grado,
        "edad": edad,
        "estado": estadoBoo
    }

    estudiantes.append(estudiante)   
    save_student(estudiantes)

    print("Estudiante agregado con EXITO")

def consultar_estudiantes(estudiantes):
    if not estudiantes:
        print("\n¡NO HAY ESTUDIANTES!")
        return

    print("\n---- Lista de Estudiantes ----")
    for e in estudiantes:
        print (f"Estudiante: {e['nombre']} | Identificacion: {e['id']} | Grado: {e['grado']} | Edad: {e['edad']} | Estado: {e['estado']} ")

def buscar_estudiante(estudiantes):
    buscar = input("Ingrese el nombre o la identificacion del estudiante: ").lower()
    
    for e in estudiantes:
        if str(e["id"]) == buscar or e["nombre"].lower() == buscar:
            print (f"Estudiante: {e['nombre']} | Identificacion: {e['id']} | Grado: {e['grado']} | Edad: {e['edad']} | Estado: {e['estado']} ")
            return
        
    print("\nNo se encontro el estudiantes con la identificacion suministrada")

def update_student(estudiantes):
    print("\n------ Update Student ------")
    
    buscar = input("Ingrese la identificacion del estudiante: ").strip()
    
    for e in estudiantes: 
        if str(e["id"]) == buscar:

            print("Dejar vacío si no desea cambiar")

            new_name = input(f"Nombre ({e['nombre']}): ")
            new_age = input(f"Edad ({e['edad']}): ")
            new_grade = input(f"Grado ({e['grado']}): ")
            new_status = input(f"Estado ({e['estado']}): ")

            if new_name != "":
                e["nombre"] = new_name

            if new_age != "":
                try:
                    e["edad"] = int(new_age)
                except ValueError:
                    print("Edad invalida")

            if new_grade != "":
                e["grado"] = new_grade

            if new_status != "":
                e["estado"] = True if new_status == "activo" else False

            save_student(estudiantes)
            print("Estudiante actualizado")
            return

    print("\nNo se encontro el estudiantes con la identificacion suministrada")

def delete_student(estudiantes):
    print("\n---- Delete Student -----")

    try:   
        buscar = int(input("Ingrese la identificacion del estudiante a eliminar: "))
    except ValueError:
        print("Identificacion invalida")
        return
         
    for e in estudiantes:
        if e["id"] == buscar:
            estudiantes.remove(e)
            save_student(estudiantes)
            print("Eliminado con exito")
            return
             
    print("\nNo se encontro el estudiantes con la identificacion suministrada")
