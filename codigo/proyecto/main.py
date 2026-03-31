import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from servicios.archivo import load_student
from servicios.estudiantes import (
    registro_estudiantes,
    consultar_estudiantes,
    buscar_estudiante,
    update_student,
    delete_student
)
from ui.menu import show_menu



def main():
    estudiantes = load_student()
    option = ""
    
    while option != "6":
        show_menu()
        option = input("Choose an option: ").strip()
        
        if option == "1":
            registro_estudiantes(estudiantes)
        elif option == "2":
            consultar_estudiantes(estudiantes)
        elif option == "3":
            buscar_estudiante(estudiantes)
        elif option == "4":
            update_student(estudiantes)
        elif option == "5":
            delete_student(estudiantes)
        elif option == "6":
            print("Goodbye....")
        else:
            print("Invalid option")

if __name__ == "__main__":  
    main()