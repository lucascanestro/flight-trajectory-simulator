import pandas as pd
import numpy as np


def data_values(time):  #Generamos los datos

    velocity = 200
    fuel_flow = 100 - .5*velocity

    data ={                     #Genero columnas de datos
        "Time"      :   time,
        "Altitud"   :   1000    + (0.5*np.sin(time/50)),
        "Velocity"  :   velocity,
        "Fuel_flow" :   fuel_flow       
    }                    
    df = pd.DataFrame(data) #Hacemos un dataframe con los datos
    return(df)

def mean_values(df):    #funcion para promedios
    
    mean_altitud = print('Altura promedio:    ',      df['Altitud'].mean())
    mean_velocity = print('Velocidad promedio:  ',  df['Velocity'].mean())
    mean_fuel_flow = print('Consumo promedio:   ',  df['Fuel_flow'].mean())
    return(mean_altitud,mean_velocity,mean_fuel_flow)

def filter_parameters(df):
    alto = df[df["Altitud"] < 1100]
    return alto


def main():
    time = np.arange(1,100,1) #Genero un tiempo de 0 a 100 segundos con un paso de 1 segundo
    df = data_values(time) #calculo data y df con la funcion
    mean_altitud,mean_velocity,mean_fuel_flow = mean_values(df)
    alto = filter_parameters(df)
    print("-Valores del DataFrame")
    print(df.head())
    print ("-Altura menos a 1100")
    print(alto.head())
    df.to_csv("flight_data_anallysis.csv", index=False) #False evita que se guarden los numeros iniciales innecesarios


main()