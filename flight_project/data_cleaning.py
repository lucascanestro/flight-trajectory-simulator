#Limpia los datos
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def data_clear(df):
    df_clean = df[
        (df["Altitud"] != 0) &
        (df["Velocity"] > 0) &
        (df["Fuel_flow"] > 0)
    ]
    removed = len(df) - len(df_clean)
    print('\nTabla limpiada:    \n', df_clean)
    return (df_clean, removed)

def save_to_csv(df_clean):
    df_clean_to_csv = df_clean.to_csv("flight_project/data/Flight_data_clean.csv")
    return df_clean_to_csv

def interpolation(df_clean):
    #tiempo
    #df_interpolado_time = np.arange(1,100,1)
    time_min = df_clean['Time'].min()
    time_max = df_clean['Time'].max()
    df_interpolado_time = np.arange(time_min, time_max + 1, 1)
    df_clean = df_clean.set_index('Time') #convertimos la columna en un indice
    df_interpolado = df_clean.reindex(df_interpolado_time) #le añadimos una nueva
    df_interpolado = df_interpolado.interpolate() #interpolamos
    df_interpolado = df_interpolado.reset_index() #Restablece el orden de las filas/columnas (0,1,2,...)

    fig, ax = plt.subplots()
    
    plt.title('Altura vs Tiempo NUEVA')
    plt.bar(df_interpolado['Time'], df_interpolado['Altitud'])
    plt.xlabel('Tiempo NUEVO')
    plt.ylabel('Altura NUEVO')
    plot_a_interpolado = plt.show()

    plt.title('Velocidad vs Tiempo NUEVA')
    plt.bar(df_interpolado['Time'], df_interpolado['Velocity'])
    plt.xlabel('Tiempo NUEVO')
    plt.ylabel('Velocidad NUEVO')
    plot_v_interpolado = plt.show()

    plt.title('Fuel flow vs Tiempo NUEVA')
    plt.bar(df_interpolado['Time'], df_interpolado['Fuel_flow'])
    plt.xlabel('Tiempo NUEVO')
    plt.ylabel('Fuel flow NUEVO')
    plot_ff_interpolado = plt.show()

    print(df_interpolado.isna().sum()) #para verificar si tengo algun NaN

    return(df_interpolado, plot_a_interpolado, plot_v_interpolado, plot_ff_interpolado)
