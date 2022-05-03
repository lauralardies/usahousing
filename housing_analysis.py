import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 

df = pd.read_csv("USA_Housing.csv")

df_resumen = df.describe() # Esta función calcula la media, la desviación típica, el mínimo, máximo y los cuartiles de todos los datos de cada columna de nuestro archivo df.
print(df_resumen)

def diagrama (var1, var2, saveas):

    plt.figure()
    sns.lmplot(x = var1, y = var2, data = df)
    plt.savefig(("img/" + saveas + ".png"))

# P R O P O S I C I Ó N   1 :
diagrama("Avg. Area House Age", "Avg. Area Income", "Edad casa - Ingresos")
# Podemos concluir viendo la gráfica que estas dos variables no dependen la una de la otra.

# P R O P O S I C I Ó N   2 :
diagrama("Avg. Area Number of Rooms", "Avg. Area Income", "Habitaciones por casa - Ingresos")

diagrama("Avg. Area Number of Rooms", "Price", "Habitaciones por casa - Precio")

diagrama("Avg. Area Income", "Price", "Ingresos - Precio")

correlation_matrix = df.corr().round(1)
sns.heatmap(data=correlation_matrix, annot=True)
plt.show()

# Descartamos las variables que tienen poca influencia, correlacion <= 0.4
df.pop("Avg. Area Number of Rooms")
df.pop("Avg. Area Number of Bedrooms")

correlation_matrix = df.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True)
plt.show()