# Registro de ejecucion

Fecha: 16 de octubre de 2026.
Fuente: datos.gov.co, Resultados unicos Saber 11, periodo 20224.

## Notebook 01 - limpieza

Se leyeron 3000 filas con 12 columnas. Se quitaron 499 filas con vacios
(casi todas por internet sin responder) y 0 repetidas. Quedaron 2501 filas
limpias en data/datos_limpios.csv.

Promedios de la tabla limpia: matematicas 50.4, lectura 52.7, global 250.3.

## Notebook 02 - hipotesis

Hipotesis 1 (prueba t, rural vs urbana en puntaje global):
rural 226.5, urbana 257.7, t = -12.731, p = 0.0. Se rechaza H0.

Hipotesis 2 (chi cuadrado, zona vs internet):
rural 344 sin internet y 253 con internet; urbana 476 sin internet y 1428
con internet. Chi = 217.994, p = 0.0. Se rechaza H0.

## Notebook 03 - KPIs

1. Puntaje global promedio: 250.3
2. Promedio matematicas: 50.4
3. Promedio lectura critica: 52.7
4. Brecha rural-urbana: 31.3 puntos
5. Hogares con internet: 67.2 %
