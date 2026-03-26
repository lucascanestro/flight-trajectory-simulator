import matplotlib.pyplot as plt
import numpy as np

def plot_altitud(df_clean):
    fig, ax = plt.subplots()
    plt.title('Altura vs Tiempo')
    plt.bar(df_clean['Time'], df_clean['Altitud'])
    plt.xlabel('Tiempo')
    plt.ylabel('Altura')
    plot_a = plt.show()
    return(plot_a)

def plot_velocity(df_clean):
    fig, ax = plt.subplots()
    plt.title('Velocidad vs Tiempo')
    plt.bar(df_clean['Time'], df_clean['Velocity'])
    plt.xlabel('Tiempo')
    plt.ylabel('Velocidad')
    plot_v = plt.show()
    return(plot_v)

def plot_fuel(df_clean):
    fig, ax = plt.subplots()
    plt.title('Fuel flow vs Tiempo')
    plt.bar(df_clean['Time'], df_clean['Fuel_flow'])
    plt.xlabel('Tiempo')
    plt.ylabel('Fuel flow')
    plot_ff = plt.show()
    return(plot_ff)

#def plot_efic(df_clean):

