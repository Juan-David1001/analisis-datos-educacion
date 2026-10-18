# Fase 2 - Hipotesis

## Hipotesis 1: puntaje global por zona

H0: el puntaje global promedio es igual en zona rural y urbana.
H1: el puntaje global promedio es distinto segun la zona.

La planteamos porque es la pregunta central del proyecto. Todo el mundo dice
que lo rural sale peor, pero hay que probarlo con numeros. Usamos el puntaje
global porque es el indicador mas completo que trae la prueba: combina las
tres areas evaluadas y no depende de una sola materia. El test que toca es la
prueba t para dos grupos, porque compara promedios. Como los grupos tienen
tamanios muy diferentes (691 rurales contra 2309 urbanos) usamos la version
de Welch, que no asume varianzas iguales. Si el valor p sale menor a 0.05,
rechazamos H0.

Variables: zona (rural, urbano) y puntaje global del estudiante.

## Hipotesis 2: zona e internet

H0: la zona no tiene relacion con tener internet en la casa.
H1: la zona si tiene relacion con tener internet en la casa.

Esta salio de mirar los datos. Vimos que en zona rural muchos hogares no
tienen internet, y eso nos parecio grave porque hoy casi todo el estudio
pasa por internet. El test que toca es chi cuadrado, porque las dos
variables son categorias (zona: rural o urbano, internet: si o no). Solo
entran los 2558 estudiantes que respondieron si o no; los 442 que quedaron
como "No informado" no sirven para esta prueba. Igual que antes, si p sale
menor a 0.05 rechazamos H0.

Variables: zona e internet en el hogar.

## Lo que salio

Corrimos las dos pruebas con los datos limpios. En la primera, el promedio
rural fue 224.8 y el urbano 253.5, con un estadistico t de -13.678 y un
valor p menor a 0.001. Se rechaza H0, o sea que si hay diferencia y no es
casualidad.

En la segunda tambien se rechazo H0, con un chi cuadrado de 220.252 y un
valor p menor a 0.001. En numeros: de 612 estudiantes rurales que
respondieron, 351 no tienen internet (57.4%). En zona urbana, 486 de 1946
no tienen (24.9%). La relacion entre zona e internet es real.

Lo que mas nos llamo la atencion fue lo grande que es la diferencia. No es
un punto ni dos, son 28.7 puntos en el puntaje global, y mas de la mitad de
los rurales sin internet. Eso ya no es un detalle, es el problema.
