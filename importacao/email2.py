import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailAut:
    def __init__(self, destinatario, assunto, conteudo):
        self.destinatario = destinatario
        self.assunto = assunto
        self.conteudo = conteudo
        
    def envio(self):
        msg = MIMEMultipart()
        msg.add_header("Content-Type", "text/html")
        
        msg['From'] = 'andrebaumgratz@gmail.com'
        password = "dstqloknybzxffbr"
        
        msg['Subject'] = self.assunto
        msg['To'] = self.destinatario
        msg.attach(MIMEText(self.conteudo, "plain"))
        
        # Conectar ao servidor SMTP
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        
        # Fazer login
        s.login(msg['From'], password)
        
        # Enviar o e-mail
        s.sendmail(msg["From"], msg["To"], msg.as_string())
        s.quit()  # Fechar a conexão
        
        print(f"E-mail enviado para {self.destinatario}.")

# Bloco principal fora da classe
if __name__ == "__main__":
    enviando = EmailAut(
        destinatario="fernanda.lobao@aluno.senai.br",
        assunto="Teste com Gmail",
        conteudo="testando email com gmail"
    )
    
    enviando.envio()
