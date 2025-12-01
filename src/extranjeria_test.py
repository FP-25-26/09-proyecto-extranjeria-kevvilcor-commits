from extranjeria import *

def test_lee_datos_extranjeria(ruta_fichero):
    ruta = lee_datos_extranjeria(ruta_fichero)
    print(f"Leídos {len(ruta)} registros.")
    print("Mostrando los 3 primeros:")
    print (ruta[:3])
    print("Mostrando los 3 últimos:")
    print (ruta[-3:])


def test_numero_nacionalidades_distintas(registros):
    num = numero_nacionalidades_distintas_2(registros)
    print (f"Hay {num} nacionalidades distintas en los datos.")


def test_secciones_distritos_con_extranjeros_nacionalidades(registros, paises):
    seccion = secciones_distritos_con_extranjeros_nacionalidades(registros, paises)
    print(f"Hay {len(seccion)} secciones de distritos con residentes cuya procedencia es {paises}.")
    print("Mostrando los 3 primeros:")
    print(seccion[:3])


def test_total_extranjeros_por_pais(registros):
    total = total_extranjeros_por_pais(registros)
    print("Mostrando el número de residentes para algunos países de procedencia:")
    print(total)
   

def test_top_n_extranjeria(registros, n):
    top = top_n_extranjeria(registros, n)
    print("Mostrando los 5 países de los que proceden más residentes:")
    print(top)


def test_barrio_mas_multicultural(registros):
    barrio = barrio_mas_multicultural(registros)
    print("El barrio más multicultural de sevilla es:")
    print(barrio)


def test_barrio_con_mas_extranjeros(registros, tipo):
    extr = barrio_con_mas_extranjeros(registros, tipo)
    
    if tipo == None:
        print(f"El barrio con más residentes extranjeros es: {extr}")
        
    elif tipo.lower() == "hombres":
        print(f"El barrio con más hombres residentes extranjeros es: {extr}")
        
    elif tipo.lower() == "mujeres":
        print(f"El barrio con más mujeres residentes extranjeros es: {extr}")
        
    
def test_pais_mas_representado_por_distrito(registros):
    distr = pais_mas_representado_por_distrito(registros)
    print(f"\n{distr}")




def main():
    registros = lee_datos_extranjeria("data\extranjeriaSevilla.csv")
    test_lee_datos_extranjeria("data\extranjeriaSevilla.csv")
    print("")
    print("#"*70)
    test_numero_nacionalidades_distintas(registros)
    print("")
    print("#"*70)
    paises = {'ITALIA', 'ALEMANIA'}
    test_secciones_distritos_con_extranjeros_nacionalidades(registros,paises)
    print("")
    print("#"*70)
    test_total_extranjeros_por_pais(registros)
    print("")
    print("#"*70)
    test_top_n_extranjeria(registros,5)
    print("")
    print("#"*70)
    test_barrio_mas_multicultural(registros)
    print("")
    print("#"*70)
    test_barrio_con_mas_extranjeros(registros, None)
    test_barrio_con_mas_extranjeros(registros, "hombres")
    test_barrio_con_mas_extranjeros(registros, "mujeres")

    print("")
    print("#"*70)
    test_pais_mas_representado_por_distrito(registros)

if __name__ == "__main__":
    main()