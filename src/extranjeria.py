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

#EJERCICIO 1:

def lee_datos_extranjeria(ruta_fichero: csv)->list[RegistroExtranjeria]:
    res = []
    with open(ruta_fichero, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for distrito, seccion, barrio, pais, hombres, mujeres in lector:
            hombres, mujeres = int(hombres), int(mujeres)
            res.append(RegistroExtranjeria(distrito, seccion, barrio, pais, hombres, mujeres))
    return res


#EJERCICIO 2:

def numero_nacionalidades_distintas(registros:RegistroExtranjeria)->int:
    nacionalidades = set()
    for a in registros:
        nacionalidades.add(a.pais)
    return len(nacionalidades)

def numero_nacionalidades_distintas_2(registros:RegistroExtranjeria)->int:
    nacionalidades = set(a.pais for a in registros)
    return len(nacionalidades)


#EJERCICIO 3:

def secciones_distritos_con_extranjeros_nacionalidades(registros:RegistroExtranjeria, paises:{str})->list:
    res = []
    paises = {p.lower() for p in paises}
    for a in registros:
        if a.pais.lower() in paises:
            res.append((a.distrito,a.seccion))
    return sorted(res)

def secciones_distritos_con_extranjeros_nacionalidades_2(registros:RegistroExtranjeria, paises:{str})->list[str,str]:
    paises = {p.lower() for p in paises}
    res = [(a.distrito,a.sesccion) for a in registros if a.pais.lower() in paises]
    return sorted(res)


#EJERCICIO 4:

def total_extranjeros_por_pais(registros:RegistroExtranjeria)->dict[str:int]:
    res = dict()
    for a in registros:
        if a.pais in res:
            res[a.pais] += (a.hombres + a.mujeres)
        else:
            res[a.pais] = (a.hombres + a.mujeres)
    return res


#EJERCICIO 5:

def top_n_extranjeria(registros:RegistroExtranjeria, n:int)->list[str,int]:
    res = dict()
    for a in registros:
        if a.pais in res:
            res[a.pais] += (a.hombres + a.mujeres)
        else:
            res[a.pais] = (a.hombres + a.mujeres)
    res_ord = sorted(res.items(), key=lambda r:r[1], reverse=True)
    return res_ord[:n]

def top_n_extranjeria_2(registros:RegistroExtranjeria, n:int)->list[str,int]:
    res = total_extranjeros_por_pais(registros)
    res_ord = sorted(res.items(), key=lambda r:r[1], reverse=True)
    return res_ord[:n]


#EJERCICIO 6:

def total_extranjeros_por_barrio(registros:RegistroExtranjeria)->dict[str:int]:
    barrios = dict()
    for a in registros:
        if a.barrio in barrios:
            barrios[a.barrio] += (a.hombres + a.mujeres)
        else:
            barrios[a.barrio] = (a.hombres + a.mujeres)
    return barrios

def barrio_mas_multicultural(registros:RegistroExtranjeria)->dict[str:int]:
    barrios = dict()
    for a in registros:
        if a.barrio in barrios:
            barrios[a.barrio] += a.hombres + a.mujeres
        else:
            barrios[a.barrio] = a.hombres + a.mujeres
    res = max(barrios, key=barrios.get)
    return res
    
def barrio_mas_multicultural_2(registros:RegistroExtranjeria)->dict[str:int]:
    barrios = total_extranjeros_por_barrio(registros)
    res = max(barrios, key=barrios.get)
    return res


#EJERCICIO 7:

def barrio_con_mas_extranjeros(registros:RegistroExtranjeria, tipo:str|None)->dict[str:str]:
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


#EJERCICIO 8

def pais_mas_representado_por_distrito(registros):
    res = dict()
    for a in registros:
        pass