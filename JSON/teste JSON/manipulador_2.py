import json

class Manipulador:
    def criar_arquivo(self, nome_arquivo):
        try:
            usuarios = [
                {
                    'Codigo': 1,
                    'Nome': 'Admin',
                    'CPF': '000.000.000-00',
                    'E-mail': 'admin@admin.com',
                    'Profissao': 'Admininstrador'             
                }
            ]
            
            json_dados = json.dumps(usuarios, ensure_ascii=False)
            with open(f"{nome_arquivo}.json","w", encoding="utf-8") as f:
                f.write(json_dados)
            return f"{nome_arquivo}.json criado."
        except Exception as e:
            return f"Não foi possivel criar o arquivo. {e}"
        
    def abrir_arquivo(self, nome_arquivo):
        with open(f"{nome_arquivo}.json","r", encoding="utf-8") as f:
            dados = json.load(f)
        return dados