#Leer el CSV
#Inspeccionar los datos
#Validarlos
#Analizarlos
#Generar métricas nuevas

import pandas as pd
import numpy as np


#           --- LECTURA CSV ---
df = pd.read_csv("flight_data_anallysis.csv", index_col=None, na_values=["NA"])
data_Altitud = df["Altitud"]
#print('\nSolo Altitud\n',data_Altitud)
#print('\nPRIMERAS FILAS\n', df.head()) #mostramos las primeras filas
#print('\nULTIMAS FILAS\n',df.tail()) #mostramos las ultimas filas

selection_zero = df[(df == 0).any(axis=1)]
selection_negatives = df[df['Velocity'] < 0]
#print ("\nVALORES CON CERO: \n",selection_zero)
#print ("\nVALORES NEGATIVOS: \n",selection_negatives)
#FILTRAMOS DATOS NO VALIDOS
filter_df = df[
    (df['Velocity']     >=0)    &
    (df['Altitud']      >=0)    &
    (df['Fuel_flow']    >=0)    
]

#CONTAMOS CUANTOS DATOS ELIMINAMOS
invalid_velocity = df[df['Velocity']<0]
velocity_data = filter_df['Velocity']  #tomo solo los valores de velocidad
fuel_flow_data = filter_df['Fuel_flow']
mean_filter_df   = filter_df.mean()
mean_velocity = velocity_data.mean()
percentage = len(invalid_velocity)/len(velocity_data) *100 #calculo porcentaje eliminado
eficience = velocity_data / fuel_flow_data
eficience_max       = eficience.max()
eficience_max_id    = eficience.idxmax()
eficience_min       = eficience.min()
eficience_min_id    = eficience.idxmin()
mean_eficience      = eficience.mean()
#MOSTRAMOS DATAREFS FILTRADO, CANTIDAD DE DATOS DE VEL ELIMINADOS Y PROMEDIO
print('\nDataRef filtrados: \n', filter_df)
print('\nCantidad de valores invalidos filtrados: \n', len(invalid_velocity))
print('\nPromedio de datos filtrados:   \n', mean_filter_df)
print('\nPromedio de velocidad:    \n', mean_velocity)
print('\nPorcentaje de valores de velocidad:    \n', percentage)
print('\nPromedio de la eficiencia:    \n', mean_eficience,
      '\nMaxima eficiencia:    \n', eficience_max, '    ID:', eficience_max_id,
      '\nMinima eficiencia:    \n', eficience_min, '    ID: ', eficience_min_id
)

#puedo comparar datos si quiero, tomar los datos del 
#df sin filtrar y agarrar el df_filter
#luego puedo obtener sus valores y compararlos para sacar conclusiones y demas.