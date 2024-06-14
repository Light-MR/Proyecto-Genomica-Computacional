import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos del CSV
df = pd.read_csv("variantes_geneticas_organizadas.csv")

# Crear un gráfico de barras para el tipo de variantes
sns.countplot(data=df, x="Tipo de Variante", hue="ID de Secuencia")
plt.title("Distribución de Variantes Genéticas")
plt.xlabel("Tipo de Variante")
plt.ylabel("Frecuencia")
plt.legend(title="ID de Secuencia", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show() 


