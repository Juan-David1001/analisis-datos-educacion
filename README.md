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

Los resultados se interpretan en docs/02_hipotesis.md y docs/04_kpis.md.

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
