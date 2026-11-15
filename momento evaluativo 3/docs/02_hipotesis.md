# Fase 2 - Hipotesis

En todas las pruebas usamos un nivel de significancia de 0.05: si el valor p
sale menor, rechazamos H0. Pero con 3000 estudiantes casi cualquier
diferencia sale significativa, asi que el valor p solo dice si la diferencia
existe. Para saber si la diferencia importa reportamos tambien el tamanio del
efecto de cada prueba. Las funciones estan en src/estadistica.py y los
calculos en el notebook 02.

| Tamanio del efecto | Para que prueba | Pequeno | Mediano | Grande |
|---|---|---|---|---|
| d de Cohen | t de Welch (dos promedios) | 0.2 | 0.5 | 0.8 |
| V de Cramer | chi cuadrado 2x2 | 0.1 | 0.3 | 0.5 |
| Epsilon cuadrado | Kruskal-Wallis | 0.01 | 0.06 | 0.14 |

## Hipotesis 1: puntaje global por zona

H0: el puntaje global promedio es igual en zona rural y urbana.
H1: el puntaje global promedio es distinto segun la zona.

La planteamos porque es la pregunta central del proyecto. Todo el mundo dice
que lo rural sale peor, pero hay que probarlo con numeros. Usamos el puntaje
global porque es el indicador mas completo que trae la prueba: combina las
areas evaluadas y no depende de una sola materia. El test que toca es la
prueba t para dos grupos, porque compara promedios. Como los grupos tienen
tamanios muy diferentes (691 rurales contra 2309 urbanos) usamos la version
de Welch, que no asume varianzas iguales. Con grupos de este tamanio la
prueba t es robusta aunque los puntajes no sean perfectamente normales.

Variables: zona (rural, urbano) y puntaje global del estudiante.

## Hipotesis 2: zona e internet

H0: la zona no tiene relacion con tener internet en la casa.
H1: la zona si tiene relacion con tener internet en la casa.

Esta salio de mirar los datos. Vimos que en zona rural muchos hogares no
tienen internet, y eso nos parecio grave porque hoy casi todo el estudio
pasa por internet. El test que toca es chi cuadrado, porque las dos
variables son categorias (zona: rural o urbano, internet: si o no). Solo
entran los 2558 estudiantes que respondieron si o no; los 442 que quedaron
como "No informado" no sirven para esta prueba.

Variables: zona e internet en el hogar.

## Hipotesis 3: internet y puntaje global

H0: el puntaje global promedio es igual con y sin internet en el hogar.
H1: el puntaje global promedio es distinto con y sin internet.

Es el eslabon que faltaba. La hipotesis 1 dice que lo rural sale peor y la 2
que lo rural tiene menos internet, pero eso no prueba que el internet tenga
que ver con el puntaje. Usamos otra vez t de Welch (1721 con internet contra
837 sin internet), solo con los que respondieron si o no.

Variables: internet en el hogar y puntaje global.

## Hipotesis 4: estrato y puntaje global

H0: el puntaje global tiene la misma distribucion en todos los estratos.
H1: al menos un estrato tiene un puntaje distinto.

La planteamos para revisar una explicacion alternativa: tal vez la brecha
rural-urbana no es por la zona sino porque en lo rural hay mas estratos
bajos. Son seis grupos de tamanios muy distintos (863 en estrato 1 y solo 34
en estrato 6), por eso usamos Kruskal-Wallis, que compara mas de dos grupos
sin asumir normalidad ni varianzas iguales. Entran los estratos 1 a 6; los
"No informado" y "Sin Estrato" quedan por fuera.

Variables: estrato y puntaje global.

## Lo que salio

| Hipotesis | Prueba | Estadistico | Valor p | Tamanio del efecto | Decision |
|---|---|---|---|---|---|
| H1 zona y puntaje | t de Welch | t = -13.678 | < 0.001 | d = 0.55 (mediano) | Se rechaza H0 |
| H2 zona e internet | Chi cuadrado | chi = 220.252 | < 0.001 | V = 0.29 (moderado) | Se rechaza H0 |
| H3 internet y puntaje | t de Welch | t = 17.976 | < 0.001 | d = 0.70 (mediano, cerca de grande) | Se rechaza H0 |
| H4 estrato y puntaje | Kruskal-Wallis | H = 140.414 | < 0.001 | epsilon cuadrado = 0.06 (mediano) | Se rechaza H0 |

**H1.** El promedio rural fue 224.8 y el urbano 253.5: 28.7 puntos de
diferencia. El d de 0.55 quiere decir que los grupos estan separados por mas
de media desviacion estandar. No es un detalle.

**H2.** De 612 estudiantes rurales que respondieron, 351 no tienen internet
(57.4%). En zona urbana, 486 de 1946 no tienen (24.9%). La V de 0.29 es una
asociacion moderada: la zona pesa, pero no lo explica todo.

**H3.** Con internet el promedio es 261.8 y sin internet 225.8: 36 puntos. Es
el efecto mas grande de los cuatro (d = 0.70), mas grande incluso que el de
la zona.

**H4.** El puntaje sube con el estrato: 238.8 en estrato 1, 249.9 en el 2,
265.3 en el 3 y 282.5 en el 4. Los estratos 5 y 6 (289.7 y 279.1) tienen muy
pocos estudiantes y no conviene sacar conclusiones de su orden.

## Lo que encontramos al cruzar las variables

Una prueba significativa no dice por que pasa. Por eso miramos la brecha
rural-urbana dentro de grupos parecidos:

| Grupo | Rural | Urbano | Brecha |
|---|---|---|---|
| Estrato 1 | 227.9 (265) | 243.7 (598) | 15.8 |
| Estrato 2 | 224.0 (161) | 256.3 (659) | 32.2 |
| Estrato 3 | 223.8 (64) | 271.9 (406) | 48.1 |
| Sin internet | 219.1 (351) | 230.6 (486) | 11.5 |
| Con internet | 237.6 (261) | 266.2 (1460) | 28.6 |

Entre parentesis va el numero de estudiantes.

1. **La brecha no es solo el estrato.** Si lo fuera, desapareceria al comparar
   estudiantes del mismo estrato. Pasa lo contrario: crece con el estrato. Un
   estudiante rural de estrato 3 saca casi lo mismo que uno de estrato 1
   (223.8 contra 227.9), mientras que en lo urbano subir de estrato si se nota.
2. **El internet ayuda, pero no cierra la brecha por si solo.** Entre los que
   tienen internet la brecha es de 28.6 puntos, casi la misma que en general.
   Los rurales con internet suben 18.5 puntos frente a los rurales sin
   internet, pero los urbanos suben 35.6. Llevar internet a lo rural es
   necesario, pero lo que lo acompana en la ciudad (computador, colegio, tiempo
   para estudiar) tambien cuenta.

Esto cambia las decisiones: la conectividad rural tiene que ir junto con
acompanamiento pedagogico, no sola.

## Limitaciones

- Son datos de observacion, no un experimento. Las pruebas muestran
  asociaciones, no causas: no podemos decir que poner internet suba el
  puntaje 36 puntos.
- Es una muestra de 3000 de un periodo. La brecha de la muestra se parece a
  la nacional (26.2 puntos, dentro del intervalo de confianza), pero los
  promedios y el internet quedan un poco por debajo del pais (ver
  docs/04_kpis.md). Ademas hay departamentos con muy pocos estudiantes
  (Vichada y Guaviare tienen 1) que no sirven para comparar departamentos
  entre si.
- El 14.7% no respondio lo del internet y el 15.5% lo del estrato. Si los que
  no respondieron son distintos a los que si (por ejemplo, mas rurales), los
  resultados de H2, H3 y H4 pueden tener sesgo.
- Hicimos cuatro pruebas. Aun con la correccion de Bonferroni (0.05 / 4 =
  0.0125) las cuatro siguen siendo significativas, porque todos los valores p
  son menores a 0.001.
