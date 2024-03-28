import requests

BASE_URL = 'http://52.200.139.211:8000/tareas'

def get_all_tareas():
    response = requests.get(BASE_URL)
    return response.json()

def add_new_tarea():
    task = input("Ingrese la nueva tarea: ")
    response = requests.post(BASE_URL, json={'tarea': task})
    return response.json()

def update_tarea():
    tarea_id = int(input("Ingrese el ID de la tarea a actualizar: "))
    task = input("Ingrese la nueva descripción de la tarea: ")
    response = requests.put(f"{BASE_URL}/{tarea_id}", json={'tarea': task})
    return response.json()

def delete_tarea():
    tarea_id = int(input("Ingrese el ID de la tarea a eliminar: "))
    response = requests.delete(f"{BASE_URL}/{tarea_id}")
    return response.json()

# Ejemplos de uso
print("Lista de tareas:")
print(get_all_tareas())

print("Agregando una nueva tarea:")
print(add_new_tarea())

print("Actualizando una tarea:")
print(update_tarea())

print("Eliminando una tarea:")
print(delete_tarea())
