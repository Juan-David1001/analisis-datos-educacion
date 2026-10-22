# Fase 4 - KPIs

Los calculos estan en el notebook 03. Cada KPI tiene su intervalo de
confianza del 95% (el rango donde probablemente esta el valor real de la
poblacion de donde sale la muestra) y se compara con el valor nacional del
mismo periodo. El valor nacional lo sacamos del mismo dataset de
datos.gov.co, con todos los estudiantes del periodo 20224 (1 065 888),
consultado con la API del portal el 22 de octubre de 2026.

| KPI | Muestra | IC 95% | Nacional 20224 | Relacion con hipotesis |
|---|---|---|---|---|
| 1. Puntaje global promedio | 246.9 | 244.9 a 248.8 | 250.1 | H1, H3, H4 |
| 2. Promedio matematicas | 49.7 | 49.2 a 50.1 | 50.6 | H1 |
| 3. Promedio lectura critica | 52.2 | 51.8 a 52.6 | 52.8 | H1 |
| 4. Brecha rural-urbana (puntos) | 28.7 | 24.6 a 32.8 | 26.2 | H1 |
| 5. % de estudiantes con internet en el hogar | 67.3% | 65.5% a 69.1% | 72.6% | H2, H3 |

## Que tan representativa es la muestra

La brecha nacional (26.2) cae dentro del intervalo de la muestra, asi que en
el indicador principal la muestra se comporta como el pais. En cambio los
promedios de la muestra quedan entre 0.6 y 3.2 puntos por debajo del
nacional, y el internet 5.3 puntos por debajo, con el valor nacional por
fuera del intervalo. O sea que la muestra tiene un poco mas de estudiantes
de contextos dificiles que el promedio del pais. Las diferencias son
pequenas y no cambian las conclusiones, pero hay que tenerlo en cuenta: los
promedios de la muestra no se pueden reportar como si fueran los nacionales.

## KPI 1: puntaje global promedio

Dio 246.9, 3.2 puntos por debajo del nacional. Es el numero mas general y
resume las cinco areas de la prueba. Sirve como linea base: una region o
grupo que este por debajo de 250 esta por debajo del pais. En la muestra eso
pasa con los estratos 1 y 2, con los rurales (224.8) y con los que no
tienen internet (225.8).

## KPI 2: promedio de matematicas

Dio 49.7 sobre 100, casi un punto por debajo del nacional. Lo separamos del
global para ver si la brecha se concentra en un area. En matematicas los
rurales sacan 45.0 y los urbanos 51.1: 6.0 puntos de brecha, que equivalen a
0.48 desviaciones estandar. A nivel nacional la brecha en matematicas es de
5.4 puntos (46.1 contra 51.5), parecida a la de la muestra.

## KPI 3: promedio de lectura critica

Dio 52.2, cerca del nacional (52.8). Lectura salio mejor que matematicas,
pero la brecha rural-urbana es un poco mas grande que en matematicas: 6.3
puntos, o 0.56 desviaciones estandar. Esto contradice la idea inicial de que
el problema rural estaba sobre todo en matematicas: la brecha es parecida en
las dos areas, o sea que es un problema general del aprendizaje rural y no de
una sola materia. Las intervenciones no deberian enfocarse solo en
matematicas.

## KPI 4: brecha rural-urbana

Dio 28.7 puntos a favor de lo urbano, con un intervalo de 24.6 a 32.8. Es el
indicador mas importante del proyecto porque responde directo a la
hipotesis 1 (p < 0.001, d de Cohen = 0.55, efecto mediano). La brecha
nacional del mismo periodo es 26.2, dentro del intervalo, asi que no es un
resultado raro de la muestra.

Meta propuesta por el equipo: bajarla a menos de 20 puntos, que equivale a
pasar de un efecto mediano (d = 0.55) a uno pequeno (cerca de d = 0.38).
Mientras el intervalo de confianza de la brecha no baje de 20, no se puede
decir que la meta se cumplio. Ojo: la brecha crece con el estrato (15.8 en
estrato 1 y 48.1 en estrato 3), asi que una brecha general mas baja puede
esconder brechas grandes en algun estrato. Hay que seguirla tambien por
estrato.

## KPI 5: estudiantes con internet en el hogar

Dio 67.3%, por debajo del nacional (72.6%). Se calcula sobre los 2558
estudiantes que respondieron si o no; los 442 "No informado" (14.7% de la
muestra) quedan por fuera para no contarlos como sin internet. Cada fila es
un estudiante, por eso el indicador habla de estudiantes y no de hogares.

Esta conectado con dos hipotesis. Con la 2: la falta de internet se
concentra en lo rural (57.4% de los rurales no tiene, contra 24.9% de los
urbanos). Con la 3: los que tienen internet sacan 36 puntos mas (d = 0.70,
el efecto mas grande que encontramos). Es el indicador mas facil de mover
con inversion, pero el cruce de la fase 2 muestra que no basta: entre
estudiantes con internet la brecha rural-urbana sigue en 28.6 puntos. Por
eso hay que leerlo junto con el KPI 4 y no como meta por si solo.
