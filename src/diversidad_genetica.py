from Bio import AlignIO
import matplotlib.pyplot as plt
import numpy as np

def calcular_diversidad_haplotipica(alignment):
    sequences = [str(record.seq) for record in alignment]
    n = len(sequences)
    haplotipos = len(set(sequences))
    freqs = [sequences.count(haplo) / n for haplo in set(sequences)]
    h = (n / (n - 1)) * (1 - sum([f**2 for f in freqs]))
    return h, haplotipos

def calcular_diversidad_nucleotidica(alignment):
    n = len(alignment)
    L = len(alignment[0].seq)
    diferencias = 0
    for i in range(n):
        for j in range(i + 1, n):
            seq1 = alignment[i].seq
            seq2 = alignment[j].seq
            diferencias += sum(1 for a, b in zip(seq1, seq2) if a != b)
    
    p = diferencias / (n * (n - 1) / 2 * L)
    return p

# Leer el archivo FASTA alineado
alignment = AlignIO.read("sec-alineadas-pig.fasta", "fasta")

# Definir los IDs de secuencia de interés
ids_jabalies = ['FJ237001.1', 'FJ237002.1', 'FJ237003.1']
ids_cerdos_domesticos = ['NC_012095.1', 'AP003428.1']

# Filtrar las secuencias por grupo
alignment_jabalies = [record for record in alignment if record.id in ids_jabalies]
alignment_cerdos_domesticos = [record for record in alignment if record.id in ids_cerdos_domesticos]

# Calcular diversidad haplotípica y nucleotídica para jabalíes
div_hapl_jabalies, num_haplot_jabalies = calcular_diversidad_haplotipica(alignment_jabalies)
div_nucle_jabalies = calcular_diversidad_nucleotidica(alignment_jabalies)

# Calcular diversidad haplotípica y nucleotídica para cerdos domésticos
div_hapl_cerdos, num_haplot_cerdos = calcular_diversidad_haplotipica(alignment_cerdos_domesticos)
div_nucle_cerdos = calcular_diversidad_nucleotidica(alignment_cerdos_domesticos)

# Imprimir resultados
print("Jabalíes:")
print(f"Diversidad Haplotípica: {div_hapl_jabalies}")
print(f"Número de Haplotipos: {num_haplot_jabalies}")
print(f"Diversidad Nucleotídica: {div_nucle_jabalies}")

print("\nCerdos Domésticos:")
print(f"Diversidad Haplotípica: {div_hapl_cerdos}")
print(f"Número de Haplotipos: {num_haplot_cerdos}")
print(f"Diversidad Nucleotídica: {div_nucle_cerdos}")

# Datos para gráfico de barras
grupos = ['Jabalíes', 'Cerdos Domésticos']
diversidad_haplotipica = [div_hapl_jabalies, div_hapl_cerdos]
numero_haplotipos = [num_haplot_jabalies, num_haplot_cerdos]

# Crear la figura y los ejes para gráfico de barras
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# Gráfico de barras para diversidad haplotípica
ax1.bar(grupos, diversidad_haplotipica, color=['blue', 'green'])
ax1.set_title('Diversidad Haplotípica')
ax1.set_ylabel('Valor')
ax1.set_ylim(0, 1.2)  # Ajustar límites del eje y

# Gráfico de barras para número de haplotipos
ax2.bar(grupos, numero_haplotipos, color=['blue', 'green'])
ax2.set_title('Número de Haplotipos')
ax2.set_ylabel('Cantidad')

# Ajustar el diseño general de la figura
plt.tight_layout()

# Guardar la figura de barras como imagen PNG
plt.savefig('grafica_diversidad_genetica_barras.png', dpi=300)

# Mostrar la figura de barras
plt.show()

# Datos para gráfico de radar
categorias = ['Diversidad Haplotípica', 'Número de Haplotipos', 'Diversidad Nucleotídica']
valores_jabalies = [div_hapl_jabalies, num_haplot_jabalies, div_nucle_jabalies]
valores_cerdos = [div_hapl_cerdos, num_haplot_cerdos, div_nucle_cerdos]

# Ajustes para el gráfico de radar
angulos = np.linspace(0, 2 * np.pi, len(categorias), endpoint=False).tolist()
valores_jabalies += valores_jabalies[:1]
valores_cerdos += valores_cerdos[:1]
angulos += angulos[:1]

# Crear la figura y los ejes para gráfico de radar
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Gráfico de radar para jabalíes
ax.plot(angulos, valores_jabalies, linewidth=1, linestyle='solid', label='Jabalíes')
ax.fill(angulos, valores_jabalies, alpha=0.25)

# Gráfico de radar para cerdos domésticos
ax.plot(angulos, valores_cerdos, linewidth=1, linestyle='solid', label='Cerdos Domésticos')
ax.fill(angulos, valores_cerdos, alpha=0.25)

# Ajustar los ángulos y etiquetas
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_thetagrids(np.degrees(angulos[:-1]), categorias)  # Ajustar aquí quitando el último ángulo

# Ajustar los límites
ax.set_ylim(0, 1.2)

# Añadir leyenda
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Guardar la figura de radar como imagen PNG
plt.savefig('grafica_diversidad_genetica_radar.png', dpi=300)

# Mostrar la figura de radar
plt.show()
