import pandas as pd
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV que contiene las variantes genéticas organizadas
csv_path = "variantes_geneticas_organizadas.csv"


df1 = pd.read_csv(csv_path)



# Agrupar y contar las frecuencias por tipo de variante y por cada ID de secuencia
frecuencias = df1.groupby(['Tipo de Variante', 'ID de Secuencia']).size().unstack(fill_value=0)

# Agregar una fila adicional para mostrar la suma total de variantes por tipo
frecuencias.loc['Total'] = frecuencias.sum()

# Mostrar las frecuencias calculadas
print("Frecuencias de Variantes por Tipo y Población:")
print(frecuencias)



df = pd.read_csv(csv_path)

# Definir los IDs de secuencia de interés
ids_jabalies = ['FJ237001.1', 'FJ237002.1', 'FJ237003.1']
ids_cerdos_domesticos = ['NC_012095.1', 'AP003428.1']

# Filtrar las variantes por grupo (jabalíes y cerdos domésticos)
jabalies = df[df['ID de Secuencia'].isin(ids_jabalies)]
cerdos_domesticos = df[df['ID de Secuencia'].isin(ids_cerdos_domesticos)]

# Calcular frecuencias de variantes por tipo
frecuencia_jabalies = jabalies['Tipo de Variante'].value_counts().reindex(['Inserción', 'Sustitución', 'Deleción']).fillna(0)
frecuencia_cerdos_domesticos = cerdos_domesticos['Tipo de Variante'].value_counts().reindex(['Inserción', 'Sustitución', 'Deleción']).fillna(0)

# Crear la tabla de contingencia (matriz de frecuencias observadas)
tabla_contingencia = pd.DataFrame({
    'Jabalíes': frecuencia_jabalies,
    'Cerdos Domésticos': frecuencia_cerdos_domesticos
})

# Mostrar la tabla de contingencia
print("Tabla de Contingencia (Frecuencias Observadas):")
print(tabla_contingencia)
print()

# Realizar la prueba de chi-cuadrado
chi2, p_valor, dof, expected = chi2_contingency(tabla_contingencia)

# Mostrar los resultados de la prueba
print(f"Valor de chi-cuadrado: {chi2}")
print(f"Valor p: {p_valor}")
print()

# Interpretar los resultados
alpha = 0.05
if p_valor < alpha:
    print("Hay evidencia suficiente para rechazar la hipótesis nula (H0)")
else:
    print("No hay suficiente evidencia para rechazar la hipótesis nula (H0)")



# Mostrar la tabla de contingencia utilizando Matplotlib
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('off')  # Ocultar ejes

# Mostrar la tabla como tabla de texto
ax.table(cellText=tabla_contingencia.values,
         rowLabels=tabla_contingencia.index,
         colLabels=tabla_contingencia.columns,
         cellLoc='center', loc='center')

# Guardar la figura como imagen
plt.savefig('tabla_contingencia.png')
plt.close()


# Crear una figura y ejes invisibles para la tabla
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('off')  # Ocultar ejes

# Mostrar la tabla como tabla de texto
tabla = ax.table(cellText=frecuencias.values,
                 rowLabels=frecuencias.index,
                 colLabels=frecuencias.columns,
                 cellLoc='center', loc='center')

# Guardar la figura como imagen
plt.savefig('tabla_frecuencias.png')
plt.close()