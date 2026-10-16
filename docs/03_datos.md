# Fase 3 - Preparacion de los datos

## Lo que hicimos

Bajamos 3000 registros del portal datos.gov.co y los pasamos a un csv con
nombres de columnas en espanol para trabajar mas facil. El codigo esta en
el notebook 01 y las funciones en src/limpieza.py.

Al revisar encontramos 499 filas con datos vacios, casi todas por la columna
de internet que venia sin responder. Esas filas se quitaron porque para la
hipotesis 2 las necesitabamos completas. No habia filas repetidas. Quedaron
2501 filas limpias, que igual es bastante para el analisis.

Los puntajes venian como texto en el csv original, asi que hubo que pasarlos
a numero antes de calcular. Eso lo hace el notebook solo al leer el archivo.

## Variables que dejamos

Nos quedamos con 12 columnas: genero, zona, departamento, municipio,
estrato, educacion de la madre, educacion del padre, internet, matematicas,
lectura, puntaje global y periodo. Quitamos codigos internos del ICFES como
los Dane y los consecutivos, porque para el analisis no aportan nada.

## Dimensiones y metricas

Las dimensiones son las que sirven para agrupar: zona, genero, estrato,
departamento e internet. Las metricas son los numeros que se miden:
promedios de matematicas, lectura y puntaje global, mas conteos y
porcentajes para los KPIs.
