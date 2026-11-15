# Fase 3 - Preparacion de los datos

## Lo que hicimos

Bajamos 3000 registros del portal datos.gov.co y los pasamos a un csv con
nombres de columnas en espanol para trabajar mas facil. El codigo esta en
el notebook 01 y las funciones en src/limpieza.py.

Al revisar encontramos 499 filas con al menos un vacio. Los vacios no
estaban todos en una sola columna: estrato tenia 466, educacion de la madre
443, educacion del padre 434 e internet 442. En vez de borrar esas filas,
las tratamos con la funcion tratar_nulos, que les pone el valor "No
informado" en la categoria que falte. Preferimos no borrarlas porque asi no
se pierde la informacion de las demas columnas, y el "No informado" queda a
la vista como categoria propia (por ejemplo, en el dashboard se puede ver
cuantos estudiantes no respondieron). No habia filas repetidas. Quedaron
3000 filas sin ningun vacio en data/datos_limpios.csv.

## Variables que dejamos

Del dataset original del ICFES nos quedamos con 12 columnas: genero, zona,
departamento, municipio, estrato, educacion de la madre, educacion del
padre, internet, matematicas, lectura, puntaje global y periodo. Quitamos
codigos internos del ICFES como los Dane y los consecutivos, porque para el
analisis no aportan nada.

## Dimensiones y metricas

Las dimensiones son las que sirven para agrupar: zona, genero, estrato,
departamento e internet. Las metricas son los numeros que se miden:
promedios de matematicas, lectura y puntaje global, mas conteos y
porcentajes para los KPIs. Ojo: para el KPI del internet y para la prueba
chi cuadrado solo se usan los estudiantes que respondieron si o no, los
"No informado" quedan por fuera.
