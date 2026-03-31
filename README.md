📚 Sistema de Gestión de Estudiantes

📌 Descripción

Este proyecto es un sistema desarrollado en Python que permite gestionar estudiantes desde la consola.
Incluye funcionalidades básicas como registrar, consultar, buscar, actualizar y eliminar estudiantes, utilizando un archivo JSON para almacenar la información.

---

🚀 Características

- ✅ Registro de estudiantes
- 📋 Listado de estudiantes
- 🔍 Búsqueda por ID o nombre
- ✏️ Actualización de datos
- ❌ Eliminación de estudiantes
- 💾 Persistencia de datos con JSON

---

🧱 Estructura del Proyecto

codigo/
│
├── proyecto/
│   ├── main.py
│   ├── servicios/
│   │   ├── estudiantes.py
│   │   └── archivo.py
│   └── ui/
│       └── menu.py
│
└── datos/
    └── estudiantes.json

---

⚙️ Cómo Funciona

El programa sigue un flujo sencillo:

1. Carga los datos desde un archivo JSON
2. Muestra un menú interactivo
3. Ejecuta la opción seleccionada por el usuario
4. Guarda los cambios automáticamente

Todo esto se ejecuta en un ciclo hasta que el usuario decide salir.

---

🧠 Módulos del Sistema

🔹 "main.py"

Controla el flujo principal del programa:

- Ejecuta el menú
- Llama a las funciones según la opción
- Mantiene el ciclo del programa

---

🔹 "menu.py"

Se encarga de mostrar las opciones al usuario.

---

🔹 "archivo.py"

Gestiona el almacenamiento de datos:

- Cargar datos desde JSON
- Guardar datos en JSON

---

🔹 "estudiantes.py"

Contiene la lógica principal del sistema:

- Registro
- Consulta
- Búsqueda
- Actualización
- Eliminación

---

💾 Estructura de los Datos

Cada estudiante se representa como un diccionario:

{
    "id": 1,
    "nombre": "Juan",
    "grado": "10A",
    "edad": 15,
    "estado": True
}

---

▶️ Instalación y Uso

1. Clona el repositorio:

git clone https://github.com/tu-usuario/tu-repositorio.git

2. Entra en la carpeta del proyecto:

cd tu-repositorio

3. Ejecuta el programa:

python main.py

---

🛠️ Tecnologías

- Python 3
- JSON

---

📌 Recomendaciones

- Asegúrate de tener Python instalado
- No modificar manualmente el archivo JSON mientras el programa está en ejecución


