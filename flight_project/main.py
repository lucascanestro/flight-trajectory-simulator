#Orquesta todo. Carga los datos, limpia, analiza, muestra resultados.
import numpy as np
import os
from simulation import data_values  #genera dato
import data_loader #lee dato
from data_cleaning import *
from analysis import mean_values
from visualization import * 

print(os.getcwd())

#Generar los datos
time = np.arange(1,100,1)
df = data_values(time)

#leer los datos
df = data_loader.data_loader("flight_project/data/Flight_data.csv")
print("Archivo leido")

#limpiamos el df.
#data_clear(df)
df_clean, removed = data_clear(df)
df_clean_to_csv = save_to_csv(df_clean)
#metricas, como promedio
mean_altitud_clean,mean_velocity_clean,mean_fuel_flow_clean = mean_values(df_clean)

#grafica de altitud
plot_a = plot_altitud(df_clean)
plot_v = plot_velocity(df_clean)
plot_ff = plot_fuel(df_clean)
plot_a_interpolado = interpolation(df_clean)


