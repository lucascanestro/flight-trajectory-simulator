import math
import numpy as np
import matplotlib.pyplot as plt

g = 9.81 #gravedad

def calcular_componentes_vel(v0, angle0):
    angle = math.radians(angle0)
    vx = v0 * math.cos(angle)
    vy = v0 * math.sin(angle)
    return (vx, vy)

def parametros(vx, vy):
    time_of_flight = 2 * vy/g
    range_distance = vx * time_of_flight
    max_height = (vy**2)/(2*g)
    t = np.linspace(0,time_of_flight,100)
    x = vx * t
    y = vy * t - 0.5 * g * t**2
    return (time_of_flight, range_distance, max_height,x,y)

def main():
    print('Simulacion de trayectoria.')

    v0 = float(input('Velocidad inicial (m/s): '))
    angle0 = float(input('Angulo de lanzamiento (grados): '))

    if angle0 <0 or angle0>90:
        print('Angulo fuera de rango')
        exit()
    vx, vy = calcular_componentes_vel(v0, angle0)
    time_of_flight,range_distance,max_height,x,y = parametros(vx,vy)

    plt.plot(x, y)
    plt.title("Trayectoria del proyectil")
    plt.xlabel("Distancia (m)")
    plt.ylabel("Altura (m)")
    plt.grid()
    max_index_x = np.argmax(x) #marca punto maximo de eje
    max_index_y = np.argmax(y)
    min_index_x = np.argmin(x)
    min_index_y = np.argmin(y)
    plt.scatter(x[max_index_x], y[max_index_x])
    plt.scatter(x[max_index_y], y[max_index_y])
    plt.scatter(x[min_index_x], y[min_index_y])
    plt.show()

main()
