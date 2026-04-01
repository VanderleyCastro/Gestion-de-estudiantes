import json
import os

estudiantes = []
save = "datos/estudiantes.json"

def load_student():
    if not os.path.exists(save):
        return []
    with open(save, "r", encoding="utf-8") as file:
        return json.load(file)

def save_student(estudiantes):
    os.makedirs("datos",exist_ok=True)
    with open(save, "w", encoding="utf-8") as file:
        json.dump(estudiantes, file, ensure_ascii=False, indent=4)
