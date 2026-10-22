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
t = -13.678, p < 0.001, d de Cohen = 0.548. Se rechaza H0.

Hipotesis 2 (chi cuadrado, zona vs internet, solo quienes respondieron):
rural 351 sin internet y 261 con internet; urbana 486 sin internet y 1460
con internet. Chi = 220.252, p < 0.001, V de Cramer = 0.293. Se rechaza H0.

Hipotesis 3 (prueba t de Welch, con vs sin internet en puntaje global):
con internet 261.8 (1721), sin internet 225.8 (837), t = 17.976,
p < 0.001, d de Cohen = 0.703. Se rechaza H0.

Hipotesis 4 (Kruskal-Wallis, estratos 1 a 6 en puntaje global):
H = 140.414, p < 0.001, epsilon cuadrado = 0.059. Se rechaza H0.

Brecha rural-urbana dentro de cada estrato: 15.8 (estrato 1), 32.2
(estrato 2), 48.1 (estrato 3). Dentro de cada grupo de internet: 11.5 sin
internet, 28.6 con internet.

## Notebook 03 - KPIs

1. Puntaje global promedio: 246.9
2. Promedio matematicas: 49.7
3. Promedio lectura critica: 52.2
4. Brecha rural-urbana: 28.7 puntos
5. Hogares con internet: 67.3 % (sobre los 2558 que respondieron)
