from scipy import stats


def dar_formato_p(valor_p):
    """El valor p nunca se reporta como 0.0, se reporta como menor que 0.001."""
    if valor_p < 0.001:
        return "p < 0.001"
    return "p = " + str(round(valor_p, 4))


def prueba_t(grupo1, grupo2):
    # Prueba t de Welch: no asume varianzas iguales, que es lo correcto
    # cuando los dos grupos tienen tamanios muy diferentes
    resultado = stats.ttest_ind(grupo1, grupo2, equal_var=False)
    print("Estadistico t:", round(resultado.statistic, 3))
    print("Valor", dar_formato_p(resultado.pvalue))
    if resultado.pvalue < 0.05:
        print("Se rechaza H0: si hay diferencia entre los grupos")
    else:
        print("No se rechaza H0: no hay evidencia de diferencia")
    return resultado.pvalue


def prueba_chi2(tabla_cruzada):
    chi, p, grados, esperados = stats.chi2_contingency(tabla_cruzada)
    print("Chi cuadrado:", round(chi, 3))
    print("Valor", dar_formato_p(p))
    if p < 0.05:
        print("Se rechaza H0: si hay relacion entre las variables")
    else:
        print("No se rechaza H0: no hay evidencia de relacion")
    return p


def d_cohen(grupo1, grupo2):
    # Tamanio del efecto para dos promedios: cuantas desviaciones estandar
    # separan a los grupos. Se usa la desviacion combinada de los dos grupos.
    n1, n2 = len(grupo1), len(grupo2)
    var_combinada = ((n1 - 1) * grupo1.var() + (n2 - 1) * grupo2.var()) / (n1 + n2 - 2)
    d = (grupo1.mean() - grupo2.mean()) / var_combinada ** 0.5
    print("d de Cohen:", round(d, 3), "(" + interpretar_d(d) + ")")
    return d


def interpretar_d(d):
    # Cortes de Cohen (1988): 0.2 pequeno, 0.5 mediano, 0.8 grande
    d = abs(d)
    if d < 0.2:
        return "efecto despreciable"
    if d < 0.5:
        return "efecto pequeno"
    if d < 0.8:
        return "efecto mediano"
    return "efecto grande"


def v_cramer(tabla_cruzada):
    # Tamanio del efecto para chi cuadrado: va de 0 (sin relacion) a 1
    chi = stats.chi2_contingency(tabla_cruzada)[0]
    n = tabla_cruzada.values.sum()
    k = min(tabla_cruzada.shape) - 1
    v = (chi / (n * k)) ** 0.5
    print("V de Cramer:", round(v, 3))
    return v


def prueba_kruskal(grupos):
    # Kruskal-Wallis: compara mas de dos grupos sin asumir normalidad.
    # El tamanio del efecto es epsilon cuadrado (0 a 1).
    h, p = stats.kruskal(*grupos)
    n = sum(len(g) for g in grupos)
    epsilon2 = h / (n - 1)
    print("H de Kruskal-Wallis:", round(h, 3))
    print("Valor", dar_formato_p(p))
    print("Epsilon cuadrado:", round(epsilon2, 3))
    if p < 0.05:
        print("Se rechaza H0: al menos un grupo es distinto")
    else:
        print("No se rechaza H0: no hay evidencia de diferencia")
    return p


def intervalo_confianza(serie, confianza=0.95):
    # Intervalo de confianza para un promedio con la distribucion t
    media = serie.mean()
    error = stats.sem(serie)
    margen = error * stats.t.ppf((1 + confianza) / 2, len(serie) - 1)
    return media - margen, media + margen
