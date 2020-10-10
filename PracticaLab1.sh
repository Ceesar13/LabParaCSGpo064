#!/bin/bash
echo "Nombre: César Alejandro Roriguez Pérez. Grupo: 064"
echo "Laboratorio de programacion para ciberseguridad"
echo "--------------------------------------------"
echo "primera peticion..."
url="http://graph.facebook.com/uanlred"
dato="?fields=id"
curl --request GET $url$dato > Datos.json
echo "--------------------------------------------"
echo "Segunda peticion..."
url2="http://graph.facebook.com/uanlred"
dato2="?fields=name"
curl --request GET $url$dato2 > Datos2.json
echo "---------------------------------------------"
echo "Tercera peticion..."
url3="htp://graph.facebook.com/uanlred"
dato3="?fields=about"
curl --request GET $url$dato3 > Datos3.json
echo "Archivos generados con exito!!"
