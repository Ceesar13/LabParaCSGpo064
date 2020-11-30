#!/usr/bin/env python3
#Nombre: César Alejandro Rodríguez Pérez - Matricula: 1734223.
#--------------------------------------------
print("Iniciando sesion...")
#---------------------------------------------
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "test.pc.fcfm@gmail.com"
receiver_email = "jose.hernandezsld@uanl.edu.mx"
password = input("Ingresa la contraseña: ")

print("Sesion iniciada!!")

message = MIMEMultipart("alternative")
message["Subject"] = "Buenas, aquí envío un meme para la cuarentena prof, soy del laboratorio de programacion de los sabados de 12:00-2:00 y le envío la pruebsa desde un correo de prueba."
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text=""" 
buenas, esto es una prueba2
"""
html = """
<img id="detailed-item-image-container" src="https://images7.memedroid.com/images/UPLOADED871/5e0d847fb7f4e.jpeg" class="img-responsive" alt="Lo vi en Facebook y me dio gracia - meme">
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
print("Mensaje con meme eviado!!")
print("Adios!!")