from scipy import stats


def prueba_t(grupo1, grupo2):
    resultado = stats.ttest_ind(grupo1, grupo2)
    print("Estadistico t:", round(resultado.statistic, 3))
    print("Valor p:", round(resultado.pvalue, 4))
    if resultado.pvalue < 0.05:
        print("Se rechaza H0: si hay diferencia entre los grupos")
    else:
        print("No se rechaza H0: no hay evidencia de diferencia")
    return resultado.pvalue


def prueba_chi2(tabla_cruzada):
    chi, p, grados, esperados = stats.chi2_contingency(tabla_cruzada)
    print("Chi cuadrado:", round(chi, 3))
    print("Valor p:", round(p, 4))
    if p < 0.05:
        print("Se rechaza H0: si hay relacion entre las variables")
    else:
        print("No se rechaza H0: no hay evidencia de relacion")
    return p
