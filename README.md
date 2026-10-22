# Análisis de datos educativos - Equipo 9

Proyecto de Business Intelligence sobre datos de educación.
ITM, Análisis de Datos, 2026-2.

## Fuente de datos

Resultados unicos Saber 11, periodo 20224, portal datos.gov.co
(datos abiertos del ICFES): https://www.datos.gov.co/d/kgxf-xxbe
Muestra de trabajo: 3000 registros en
`data/datos_reales.csv`, con puntajes de matematicas, lectura critica
y global por estudiante, mas zona, genero y estrato.

## Objetivo

Analizar los datos educativos para encontrar que factores se relacionan
con el rendimiento, y proponer decisiones con evidencia.

## Metodología

1. Limpieza de los datos (`notebooks/01_limpieza.ipynb`)
2. Pruebas de hipotesis con valor p (`notebooks/02_hipotesis.ipynb`)
3. Calculo de KPIs (`notebooks/03_kpis.ipynb`)
4. Dashboard en Power BI (`dashboard/`)
5. Video explicativo (`video/guion.md`)

## Resultados

Nivel de significancia 0.05. Ademas del valor p se reporta el tamanio del
efecto. Detalle en `docs/02_hipotesis.md` y `docs/04_kpis.md`.

| Hipotesis | Prueba | Valor p | Tamanio del efecto |
|---|---|---|---|
| H1: el puntaje global cambia con la zona | t de Welch | < 0.001 | d = 0.55 (mediano) |
| H2: el internet se relaciona con la zona | Chi cuadrado | < 0.001 | V = 0.29 (moderado) |
| H3: el puntaje global cambia con el internet | t de Welch | < 0.001 | d = 0.70 (mediano) |
| H4: el puntaje global cambia con el estrato | Kruskal-Wallis | < 0.001 | epsilon cuadrado = 0.06 |

| KPI | Muestra (IC 95%) | Nacional 20224 |
|---|---|---|
| Puntaje global promedio | 246.9 (244.9 a 248.8) | 250.1 |
| Promedio matematicas | 49.7 (49.2 a 50.1) | 50.6 |
| Promedio lectura critica | 52.2 (51.8 a 52.6) | 52.8 |
| Brecha rural-urbana | 28.7 puntos (24.6 a 32.8) | 26.2 |
| % de estudiantes con internet en el hogar | 67.3% (65.5% a 69.1%) | 72.6% |

Hallazgos principales:

- La brecha rural-urbana no se explica solo por el estrato: dentro del mismo
  estrato se mantiene y crece (15.8 puntos en estrato 1, 48.1 en estrato 3).
- Tener internet es el factor con el efecto mas grande (36 puntos), pero no
  cierra la brecha por si solo: entre estudiantes con internet sigue en 28.6
  puntos.
- La brecha es parecida en matematicas y en lectura, asi que es un problema
  general del aprendizaje rural y no de una sola materia.

## Conclusiones

Se completan con los hallazgos del dashboard en la fase 6.

## Equipo

- Juan David Osorio Zapata
- David Galvan Sierra
- Federico Rodriguez Franco

## Como correrlo

```
pip install -r requirements.txt
```

Abrir los notebooks en orden: 01, 02, 03.
