#!/bin/bash
host=$1
port=$2
port2=$3
echo "Nombre: César Alejandro Rodríguez Pérez - Matricula: 1734223"
echo "Materia: Lab.ParaCS - Horario: Sabado 12:00-2:00 pm"
echo "-------------------------------------------------------------"
echo "Verificando los puertos de la ip"
for((i=$port; i<=$port2; i++))
do
   (echo >/dev/tcp/$host/$i)>/dev/null 2>&1 && echo "Puerto $i Abierto"
done
echo "Fin del script!!"
