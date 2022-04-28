import pandas as pd

stats = pd.read_csv("Dataset.csv", header=0)


hp = list(stats["hp"])  
attack = list(stats["attack"])   
defense = list(stats["defense"])  
l = len(hp)

for i in range (1,l):
    diccionario = {"salud":hp, "ataque":attack, "defensa":defense}
print(l)

#Cantidad de observaciones

print("- CANTIDAD DE OBSERVACIONES -")
print("Cantidad de observaciones = {}".format(l))

#Valores mínimos y máximos

print(" Stats máximas ")
max_value = None

for num in hp:
    if (max_value is None or num > max_value):
        max_value = num

print('Mejor estadísta salud:', max_value)

for num in attack:
    if (max_value is None or num > max_value):
        max_value = num

print('Mejor estadística ataque', max_value)

for num in defense:
    if (max_value is None or num > max_value):
        max_value = num

print('Mejor estadística defensa:', max_value)

print(" Stats mínimas ")

min_value = None

for num in hp:
    if (min_value is None or num < min_value):
        min_value = num

print('Peor estadística salud', min_value)

for num in attack:
    if (min_value is None or num < min_value):
        min_value = num

print('Peor estadística ataque', min_value)

for num in defense:
    if (min_value is None or num < min_value):
        min_value = num

print('Peor estadística defensa:', min_value)

#MEDIA

print(" Media estadísticas")
puntos_salud_totales = sum(hp)
media_hp = puntos_salud_totales / l
print("La media de Salud es {}".format(media_hp))

puntos_ataques_totales = sum(attack)
media_ataque = puntos_ataques_totales / l
print("La media del ataque es {}".format(media_ataque))

puntos_defensa_totales = sum(defense)
media_defensa = puntos_defensa_totales / l
print("La media de Escritura es {}".format(media_defensa))

#MEDIANA
print("- MEDIANA -")
Mediana = int(l/2)

medianaSalud = (hp[Mediana] + hp[Mediana + 1])/2
print("La mediana de las notas de mates es: {}".format(medianaSalud))

medianaAtaque = (attack[Mediana] + attack[Mediana + 1])/2
print("La mediana de las notas de lectura es: {}".format(medianaAtaque))

medianaDefensa = (defense[Mediana] + defense[Mediana + 1])/2
print("La mediana de las notas de escritura  es: {}".format(medianaDefensa))

#MODA
print("Moda")

cant_puntos_salud = {}
for numero in hp:
    n = str(numero)
   
    if not n in cant_puntos_salud:
        
        cant_puntos_salud[n] = 1
    
    else:
        
        cant_puntos_salud[n] += 1

mayor_cantidad = 0
frecuencia_hp = hp[0]

for numero in cant_puntos_salud:
    if cant_puntos_salud[numero] > frecuencia_hp:
        mayor_cantidad = numero
        frecuencia_hp = cant_puntos_salud[numero]

frecuencia_hp = cant_puntos_salud[str(mayor_cantidad)]
print(f"La nota de mates más repetida es {mayor_cantidad} (encontrado {frecuencia_hp} ocasiones)")



cant_puntos_ataque = {}
for numero in attack:
    n = str(numero)
   
    if not n in cant_puntos_ataque:
        
        cant_puntos_ataque[n] = 1
    
    else:
        
        cant_puntos_ataque[n] += 1

mayor_cantidad = 0
frecuencia_ataque = attack[0]

for numero in cant_puntos_ataque :
    if cant_puntos_ataque [numero] > frecuencia_ataque:
        mayor_cantidad = numero
        frecuencia_ataque = cant_puntos_ataque [numero]

n = cant_puntos_ataque [str(mayor_cantidad)]
print(f"La nota de lectura más repetida es {mayor_cantidad} (encontrado {n} ocasiones)")



#No he podido acabar la moda de la escritura