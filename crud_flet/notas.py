
import pandas as pd
import re

# Passo 1: Ler os dados a partir do arquivo Excel
#file_path = 'notas_excel.xls'  # Altere para o caminho do seu arquivo
file_path = 'C:/Users/Aluno Manhã/Documents/Aluno_tarde/Turma_Python_IA_Vesp/Aulas_Python/crud_flet/notas_excel.xlsx'

df = pd.read_excel(file_path, header=None)

# Passo 2: Tratar a sequência linear de dados separada por vírgulas
# Converter a única célula com dados em uma lista dividida por vírgula
data = df[0].iloc[0]  # Primeiro (e único) valor da célula
dados_separados = re.split(r',\s*', data)  # Usando regex para separar com mais precisão

# Passo 3: Organizar os dados em grupos
# Supondo que o padrão seja: Candidato, Nota, Classificação
# Se os dados forem diferentes, ajuste o número por grupo

n_colunas = 3  # Número de campos por registro (ex: candidato, nota, classificação)
dados_grupos = [dados_separados[i:i + n_colunas] for i in range(0, len(dados_separados), n_colunas)]

# Passo 4: Criar um DataFrame com os dados tratados
df_final = pd.DataFrame(dados_grupos, columns=['Candidato', 'Nota', 'Classificação'])  # Modifique conforme a estrutura dos dados

# Passo 5: Salvar em um novo arquivo Excel
df_final.to_excel('dados_tratados.xlsx', index=False)

print("Dados tratados e exportados com sucesso!")
