import math
import numpy as np
import matplotlib.pyplot as plt

g = 9.81

def calcular_componentes(v0, angle0):
    angle = math.radians(angle0)
    vx = v0 * math.cos(angle)
    vy = v0 * math.sin(angle)
    return (vx, vy)

def generar_trayectoria(vx, vy):
    time_of_flight = 2 * vy/g
    range_distance = vx * time_of_flight
    max_height = (vy**2)/(2*g)
    t = np.linspace(0,time_of_flight,100)
    x = vx * t
    y = vy * t - 0.5 * g * t**2
    return (time_of_flight, range_distance, max_height,x,y)

def encontrar_puntos_clave(x, y):
    max_index_x = np.argmax(x) #marca punto maximo de eje
    max_index_y = np.argmax(y)
    min_index_x = np.argmin(x)
    min_index_y = np.argmin(y)
    plt.scatter(x[max_index_x], y[max_index_x])
    plt.scatter(x[max_index_y], y[max_index_y])
    plt.scatter(x[min_index_x], y[min_index_y])
    plt.plot(x, y)
    plt.title("Trayectoria del proyectil")
    plt.xlabel("Distancia (m)")
    plt.ylabel("Altura (m)")
    plt.grid()
    fig = plt.show()
    return(fig)

def graficar_trayectoria():
    
    while True:
        v0 = float(input('Velocidad inicial (m/s): '))
        if (v0 < 0):
            print('Velocidad no puede ser negativa.')
        else:
            break

    while True:
        angle0 = float(input('Angulo de lanzamiento (grados): '))
        if (angle0 > 90 or angle0 < 0):
            print('El angulo tiene que estar en el rango de [0-90]')
        else:
            break
    vx, vy = calcular_componentes(v0,angle0)
    time_of_flight, range_distance, max_height,x, y = generar_trayectoria(vx,vy)
    fig = encontrar_puntos_clave(x,y)

graficar_trayectoria()