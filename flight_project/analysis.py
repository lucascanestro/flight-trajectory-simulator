#Metricas, promedio


def mean_values(df_clean):
    mean_altitud_clean = df_clean["Altitud"].mean()
    mean_velocity_clean = df_clean["Velocity"].mean()
    mean_fuel_flow_clean = df_clean['Fuel_flow'].mean()
    print("\nValores promedios:\n",
          "\nAltitud ->",mean_altitud_clean,
          "\nVelocity ->", mean_velocity_clean,
          "\nFuel_flow ->",mean_fuel_flow_clean)
    
    return(mean_altitud_clean,mean_velocity_clean,mean_fuel_flow_clean)