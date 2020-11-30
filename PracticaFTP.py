#!/usr/bin/env python3
from ftplib import FTP

try:
  servidor="ftp.webcindario.com"
  usuario="cesar"
  password="Charizard@123@" 
  #No se me ocurrio otra cosa xD, La dejo por si gusta ver los archivos que contiene
  conex= FTP(servidor)
  conex.login(usuario, password)
  print("Se establecio la conexion!!")
except:
	print("No se establecio la conexion")


conex.retrlines("LIST")

fich=open("pruebaFTP.txt", "wb")
conex.retrbinary("RETR pruebaFTP.txt", fich.write)
fich.close()

conex.quit()

