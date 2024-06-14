
# Autores:
 - Reyes Ramos Luz María
 - Sanchez Castro Gustavo

## script `alineamiento_análisis.py`

Encuentra variantes genéticas en un archivo FASTA de secuencias alineadas.



1. Lee el archivo FASTA.
2. Identifica variantes (inserciones, deleciones, sustituciones).
3. Crea un DataFrame con información sobre las variantes.
4. Guarda el DataFrame como CSV.
5. Muestra un resumen de las variantes.

**Output** Un archivo CSV `variantes_geneticas_organizadas.csv` con detalles sobre las variantes encontradas.


## Script `análisis_variantes.py`

 Compara frecuencias de variantes genéticas en jabalíes vs. cerdos domésticos.


1. **Cargar datos y calcular frecuencias:**
    * Carga el CSV con variantes.
    * Agrupa por tipo de variante y especie (jabalí/cerdo doméstico).
    * Calcula frecuencias.

2. **Análisis estadístico:**
    * Crea tabla de contingencia (frecuencias observadas).
    * Realiza prueba chi-cuadrado (asociación entre variante y especie).

3. **Visualización:**
    * Genera tablas de frecuencias (PNG).

**Output:**

* Tablas PNG: frecuencias por variante y especie.
* Prueba chi-cuadrado: ¿hay relación entre tipo de variante y especie?


## sCript `diversidad_genetica.py`

 Compara diversidad genética (haplotípica y nucleotídica) entre jabalíes y cerdos domésticos.


1. **Cargar datos y calcular diversidad:**
    * Carga el archivo FASTA de secuencias alineadas.
    * Filtra secuencias por grupo (jabalíes y cerdos domésticos).
    * Calcula diversidad haplotípica (número de haplotipos y Shannon) y nucleotídica (distancia por par de bases) para cada grupo.

2. **Visualización:**
    * Crea dos gráficos:
        * **Barras:** Compara diversidad haplotípica y número de haplotipos entre grupos.
        * **Radar:** Muestra la distribución de la diversidad genética para cada grupo.
    * Guarda las figuras como imágenes PNG.

** Output:**

* Imágenes PNG: diversidad genética comparativa entre jabalíes y cerdos domésticos.
* Valores numéricos de la diversidad para cada grupo.
