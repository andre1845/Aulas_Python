import json
import os

class Manipulador:
    def criar_arquivo(self, nome_arquivo):
        try:
             # Diretório atual onde o script está rodando
            diretorio_atual = os.path.dirname(os.path.abspath(__file__))
            
            # Caminho absoluto para o arquivo JSON
            caminho_arquivo = os.path.join(diretorio_atual, f"{nome_arquivo}.json")
            
            usuarios = [
                {
                    'Codigo': 0,
                    'Nome': 'Admin',
                    'CPF': '000.000.000-00',
                    'E-mail': 'admin@admin.com',
                    'Profissao': 'Admininstrador'             
                }
            ]
            
            json_dados = json.dumps(usuarios, ensure_ascii=False)
            with open(caminho_arquivo,"w", encoding="utf-8") as f:
                f.write(json_dados)
            return f"{nome_arquivo}.json criado."
        except Exception as e:
            return f"Não foi possivel criar o arquivo. {e}"
        
    def abrir_arquivo(self, nome_arquivo):
        # Diretório atual onde o script está rodando
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
            
        # Caminho absoluto para o arquivo JSON
        caminho_arquivo = os.path.join(diretorio_atual, f"{nome_arquivo}.json")
            
        with open(caminho_arquivo,"r", encoding="utf-8") as f:
            dados = json.load(f)
        return dados
    
    def salvar_dados(self, usuarios, nome_arquivo):
        try:
            # Diretório atual onde o script está rodando
            diretorio_atual = os.path.dirname(os.path.abspath(__file__))
            
            # Caminho absoluto para o arquivo JSON
            caminho_arquivo = os.path.join(diretorio_atual, f"{nome_arquivo}.json")
            
            with open(caminho_arquivo,"w", encoding="utf-8") as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=4)
            return f"Daddos gravados!"
        except Exception as e:
            return f"Não foi possivel salvar os dados no arquivo. {e}"