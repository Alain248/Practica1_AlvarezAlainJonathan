import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

#Generar datos de estatura 

np.random.seed(42)
stature = np.random.uniform(1.4, 2.0, 100)
peso2 = []  

#generar pesos aleatorios según la estatura
for estat2 in stature:
    #Peso mínimo y máximo segun el imc y modificandolo para sacar un peso mejor con la formula
    pesoMin = 19.5 * (estat2 ** 2)  
    pesoMax = 24.9 * (estat2 ** 2)  
    #peso entre el peso mínimo y máximo
    peso = np.random.uniform(pesoMin, pesoMax)
    peso2.append(peso)

#DataFrame con los datos de estatura y peso
datos = pd.DataFrame({
    'ESTATURA (M.)': stature,
    'PESO (kg)': peso2
})

#Obtener la pendiente y la intersección de la recta 

es = datos['ESTATURA (M.)']
pe = datos['PESO (kg)']
m = np.sum((es - np.mean(es)) * (pe - np.mean(pe))) / np.sum((es - np.mean(es)) ** 2)
b = np.mean(pe) - m * np.mean(es)

#fórmula de la recta
Strai = m * es + b

#Grafica de los datos

plt.scatter(datos['ESTATURA (M.)'], datos['PESO (kg)'], color='green', label='Valores')
plt.plot(es, Strai, color='red', label='Linea')
plt.title('ESTATURA CON PESO')
plt.xlabel('ESTATURA (M.)')
plt.ylabel('PESO (kg)')
plt.legend()
plt.show()