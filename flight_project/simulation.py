#Genera los datos y el csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def data_values(time):  #Generamos los datos
    altitud_ref = 1000
    altitud_base = 1000
    altitud_amplitude = 100    #cuanto sube/baja
    velocity_base = 200
    altitud = altitud_base + altitud_amplitude * np.sin(0.5 * time) #altitud en funcion del tiempo. Frecuencia 0.5 que tan rapido
    velocity = (velocity_base + 10 * (altitud - altitud_ref))
    fuel_flow = 100 + .5*velocity**2
    
    data ={                     #Genero columnas de datos
        "Time"      :   time,
        "Altitud"   :   altitud,
        "Velocity"  :   velocity,
        "Fuel_flow" :   fuel_flow       
    }                    
    df = pd.DataFrame(data) #Hacemos un dataframe con los datos
    plt.plot(time,velocity)
    plt.grid()
    fig = plt.show()
    df_to_csv = df.to_csv("flight_project/data/Flight_data.csv", index=False) #Hacemos el Csv
    return(df, fig, df_to_csv)
