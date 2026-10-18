# Registro de ejecucion

Fecha: 17 de octubre de 2026.
Fuente: datos.gov.co, Resultados unicos Saber 11, periodo 20224.

## Notebook 01 - limpieza

Se leyeron 3000 filas con 12 columnas. 499 filas tenian al menos un vacio
(estrato 466, educacion madre 443, educacion padre 434, internet 442). Los
vacios se trataron con la categoria "No informado" y no se borro ninguna
fila. 0 repetidas. Quedaron 3000 filas sin vacios en
data/datos_limpios.csv.

Promedios de la tabla limpia: matematicas 49.7, lectura 52.2, global 246.9.

## Notebook 02 - hipotesis

Hipotesis 1 (prueba t de Welch, rural vs urbana en puntaje global):
rural 224.8 (691 estudiantes), urbana 253.5 (2309 estudiantes),
t = -13.678, p < 0.001. Se rechaza H0.

Hipotesis 2 (chi cuadrado, zona vs internet, solo quienes respondieron):
rural 351 sin internet y 261 con internet; urbana 486 sin internet y 1460
con internet. Chi = 220.252, p < 0.001. Se rechaza H0.

## Notebook 03 - KPIs

1. Puntaje global promedio: 246.9
2. Promedio matematicas: 49.7
3. Promedio lectura critica: 52.2
4. Brecha rural-urbana: 28.7 puntos
5. Hogares con internet: 67.3 % (sobre los 2558 que respondieron)
