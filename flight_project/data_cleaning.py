#Limpia los datos

def data_clear(df):
    df_clean = df[
        (df["Altitud"] != 0) &
        (df["Velocity"] > 0) &
        (df["Fuel_flow"] > 0)
    ]
    removed = len(df) - len(df_clean)
    print('\nTabla limpiada:    \n', df_clean)
    return (df_clean, removed)

