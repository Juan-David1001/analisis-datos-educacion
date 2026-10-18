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
