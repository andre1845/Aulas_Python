import smtplib
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

class EmailAut:
    def __init__(self, destinatario, assunto, conteudo):
        self.destinatario = destinatario
        self.assunto = assunto
        self.conteudo = conteudo
        
    def envio(self):
        msg = MIMEMultipart()
        msg.add_header("Content-Type", "text/html")
        
        msg['From'] = 'andrino.senac@gmail.com'
        password = "Comandos@12"
        
        msg['Subject'] = self.assunto
        msg['To'] = self.destinatario
        msg.attach(MIMEText(self.conteudo, "plain"))
        
        s = smtplib.SMTP("smtp.hotmail.com: 587")
        s.starttls()
        s.login(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
        print(f"E-mail enviado para {self.destinatario}.")
        
        if __name__ == "__main__":
            enviando = EmailAut(
                destinatario="andrebaumgratz@gmail.com",
                assunto="Assunto que deseja tratar no e-email",
                conteudo="Texto que deseja colocar no corpo do email"
            )
            
            enviando.envio()