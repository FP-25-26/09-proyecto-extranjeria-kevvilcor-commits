from typing import NamedTuple
import csv

RegistroExtranjeria = NamedTuple(
    "RegistroExtranjeria", 
            [("distrito",str),
             ("seccion", str),
             ("barrio", str),
             ("pais",str),
             ("hombres", int),
             ("mujeres", int)
            ]
)


def lee_datos_extranjeria(ruta_fichero):
    res = []
    with open(ruta_fichero, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for distrito, seccion, barrio, pais, hombres, mujeres in lector:
            hombres, mujeres = int(hombres), int(mujeres)
            res.append(RegistroExtranjeria(distrito, seccion, barrio, pais, hombres, mujeres))
    return res


def numero_nacionalidades_distintas(registros):
    nacionalidades = set()
    for a in registros:
        nacionalidades.add(a.pais)
    return len(nacionalidades)


def secciones_distritos_con_extranjeros_nacionalidades(registros, paises):
    res = []
    paises = {p.lower() for p in paises}
    for a in registros:
        if a.pais.lower() in paises:
            res.append((a.distrito,a.seccion))
    return sorted(res)


def total_extranjeros_por_pais(registros):
    res = dict()
    for a in registros:
        if a.pais in res:
            res[a.pais] += (a.hombres + a.mujeres)
        else:
            res[a.pais] = (a.hombres + a.mujeres)
    return res


def top_n_extranjeria(registros, n=3):
    res = dict()
    for a in registros:
        if a.pais in res:
            res[a.pais] += (a.hombres + a.mujeres)
        else:
            res[a.pais] = (a.hombres + a.mujeres)
    res_ord = sorted(res.items(), key=lambda r:r[1], reverse=True)
    return res_ord[:n]


def barrio_mas_multicultural(registros):
    barrios = dict()
    for a in registros:
        if a.barrio in barrios:
            barrios[a.barrio] += a.hombres + a.mujeres
        else:
            barrios[a.barrio] = a.hombres + a.mujeres
    # res = sorted(barrios.items(), key=lambda b:b[1], reverse=True)
    # return res[0]
    return max(barrios, key=barrios.get)


def barrio_con_mas_extranjeros(registros, tipo=None):
    barrios = dict()
    
    for a in registros:
        if tipo == None:
            if a.barrio in barrios:
                barrios[a.barrio] += a.hombres + a.mujeres
            else:
                barrios[a.barrio] = a.hombres + a.mujeres
        elif tipo.capitalize() == "Hombres":
            if a.barrio in barrios:
                barrios[a.barrio] += a.hombres
            else:
                barrios[a.barrio] = a.hombres
        elif tipo.capitalize() == "Mujeres":
            if a.barrio in barrios:
                barrios[a.barrio] += a.mujeres
            else:
                barrios[a.barrio] = a.mujeres
    return max(barrios, key=barrios.get)


def pais_mas_representado_por_distrito(registros):
    res = dict()
    for a in registros:
        pass