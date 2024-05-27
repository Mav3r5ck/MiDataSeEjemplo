import psutil
import datetime
import time

def obtener_info_memoria():
    memoria = psutil.virtual_memory()
    return {
        'etiqueta_tiempo': datetime.datetime.now().strftime("%H:%M:%S"),
        'porcentaje': memoria.percent
    }

def guardar_encabezado(archivo):
    with open(archivo, 'w') as file:
        file.write("Marca de tiempo,Uso de memoria (%)\n")

def guardar_info_memoria(info_memoria, archivo):
    with open(archivo, 'a') as file:
        file.write(f"{info_memoria['etiqueta_tiempo']},{info_memoria['porcentaje']}\n")

if __name__ == "__main__":
    duracion = 300
    intervalo = 1
    nombre_archivo = 'uso_memoria.txt'
    guardar_encabezado(nombre_archivo)
    tiempo_inicio = time.time()
    while (time.time() - tiempo_inicio) < duracion:
        info_memoria = obtener_info_memoria()
        guardar_info_memoria(info_memoria, nombre_archivo)
        time.sleep(intervalo)

    print(f"Información registrada en '{nombre_archivo}' durante {duracion} segundos.")
