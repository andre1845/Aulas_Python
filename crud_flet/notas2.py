import pandas as pd

# Carregar o arquivo Excel
file_path = 'C:/Users/Aluno Manhã/Documents/Aluno_tarde/Turma_Python_IA_Vesp/Aulas_Python/crud_flet/notas_excel.xlsx'  # Substitua pelo caminho do arquivo
df = pd.read_excel(file_path)

# Função para separar cada bloco de dados
def process_row(row):
    candidatos = row.split(" / ")
    data = []
    for candidato in candidatos:
        data.append(candidato.split(", "))
    return data

# Aplicar a função de separação nas linhas
all_data = []
for row in df.iloc[:, 0]:  # Assumindo que a coluna com os dados está na primeira posição
    all_data.extend(process_row(row))

# Criar novo DataFrame
columns = ["ID", "Nome", "Nota1", "Peso1", "Nota2", "Peso2", "Nota3", "Peso3", "Nota4", "Peso4", "Nota5", "Peso5", "Nota6", "Peso6", "Nota7", "Peso7", "Nota8", "Peso8", "Total"]
organized_df = pd.DataFrame(all_data, columns=columns)

# Exportar para um novo arquivo Excel
output_file = "dados_organizados.xlsx"
organized_df.to_excel(output_file, index=False)

print(f"Dados organizados foram exportados para {output_file}")

