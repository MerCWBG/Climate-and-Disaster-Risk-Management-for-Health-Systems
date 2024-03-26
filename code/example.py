# import pyprind
# import time

# n = 100
# bar = pyprind.ProgBar(n)
# for i in range(n):
#     bar2 = pyprind.ProgBar(n)
#     for i in range(100):
#         time.sleep(0.2)
#         bar2.update()
#     bar.update()


from tqdm import tqdm
import time

# Número total de subtareas
num_subtasks = 10

# Configuración de la barra de progreso principal
main_bar = tqdm(total=num_subtasks * 100, desc="Tarea principal")

# Simulación de la tarea con subtareas
for subtask in range(num_subtasks):
    subtask_bar = tqdm(total=100, desc=f"Subtarea {subtask + 1}", leave=False)
    for _ in range(10):  # Simulamos 10 etapas para cada subtarea
        time.sleep(0.1)  # Simulamos una pequeña espera
        subtask_bar.update(10)  # Avanzamos 10 unidades en cada etapa
        main_bar.update(
            10
        )  # Avanzamos también la barra principal en cada etapa de subtarea
    subtask_bar.close()  # Cerramos la barra de progreso de la subtarea

# Cerramos la barra de progreso principal
main_bar.close()
