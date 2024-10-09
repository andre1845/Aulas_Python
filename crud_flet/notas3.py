import pandas as pd

# Especifique o caminho correto do arquivo
file_path = "C:/Users/Aluno Manhã/Documents/Aluno_tarde/Turma_Python_IA_Vesp/Aulas_Python/crud_flet/notas_excel.xlsx"  # Ajuste conforme necessário

# Carregar o arquivo Excel
df = pd.read_excel(file_path)

# Função para separar cada bloco de dados
def process_row(row):
    if isinstance(row, str):  # Verifica se a linha é uma string
        candidatos = row.split(" / ")
        data = []
        for candidato in candidatos:
            data.append(candidato.split(", "))
        return data
    else:
        return []  # Retorna uma lista vazia se não for uma string

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
