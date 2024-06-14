from Bio import AlignIO
import pandas as pd

# Ruta al archivo FASTA alineado
input_file = "sec-alineadas-pig.fasta"

# Leer el archivo FASTA alineado
alignment = AlignIO.read(input_file, "fasta")

# Preparar una lista para almacenar las variantes
variantes = []

# Recorrer cada posición en el alineamiento
for i in range(alignment.get_alignment_length()):
    # Obtener las bases en esa posición para cada secuencia
    bases = {}
    for record in alignment:
        bases[record.id] = record.seq[i]
    
    # Identificar variantes
    base_ref = bases[alignment[0].id]  # Base de referencia (la primera secuencia)
    
    for seq_id, base in bases.items():
        if base != base_ref:
            if base_ref == "-" and base != "-":
                # Inserción en las demás secuencias respecto a la base de referencia
                tipo_variante = "Inserción"
                descripcion = f"Inserción de {base} en posición {i+1}"
            elif base_ref != "-" and base == "-":
                # Deleción en la secuencia actual respecto a la base de referencia
                tipo_variante = "Deleción"
                descripcion = f"Deleción de {base_ref} en posición {i+1}"
            elif base_ref != "-" and base != "-":
                # Sustitución de bases
                tipo_variante = "Sustitución"
                descripcion = f"Sustitución de {base_ref} por {base} en posición {i+1}"
            else:
                continue
            
            # Agregar la variante encontrada a la lista
            variantes.append([i+1, base_ref, seq_id, base, tipo_variante, descripcion])

# Crear un DataFrame de pandas para almacenar las variantes
df_variantes = pd.DataFrame(variantes, columns=["Posición", "Base de Referencia", "ID de Secuencia", "Base", "Tipo de Variante", "Descripción"])

# Guardar el DataFrame como archivo CSV
output_file = "variantes_geneticas_organizadas.csv"
df_variantes.to_csv(output_file, index=False)

print(f"Se ha generado un archivo CSV con variantes organizadas: {output_file}")

# Mostrar una tabla resumida
print(df_variantes.head(10).to_string(index=False))  # Mostrar solo las primeras 10 filas como ejemplo
