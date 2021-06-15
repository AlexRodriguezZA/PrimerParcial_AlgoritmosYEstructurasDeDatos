from listas import Lista;
#Dada una lista con nombres de personajes de la saga de Avengers, resolver las siguientes tareas:
#a. Determinar si ‘Thor’ está en la lista, de ser así indicar en qué posición de la misma;
#b. Modificar el nombre de ‘Scalet Witch’ a ‘Scarlet Witch’;
#c. Dada una lista auxiliar con los siguientes personajes (‘Black Widow’, ‘Hulk’,
#‘Rocket Racoonn’, ‘Loki’), agregarlos a la lista principal en el caso de no estar
#cargados. 
#d. Realizar un barrido ascendente y descendente de la lista. 
# e. Mostrar la información del personaje en la posición 7. 
# f. Mostrar todos los personajes que comienzan con C o S. 
# g. Ahora los datos cambiaron y debe incluir (año de aparición y un campo
#booleano que indica si es héroe True villano False), luego realizar un barrido
#ordenado por nombre y otro por año de aparición. Deberá cargar toda la
#información de nuevo.

listaHeroes = Lista()
listaAux = Lista()

listaNuevaHeroesPorNombres = Lista()
listaNuevaHeroesPorAnio = Lista()
datosHeroes = [
    {"Personaje":"Loki","Anio":1956,"HeroeVillano":False},
    {"Personaje":"Iron man","Anio":1960,"HeroeVillano":True},
    {"Personaje":"Thor","Anio":1989,"HeroeVillano":True},
    {"Personaje":"Miss marvel","Anio":1936,"HeroeVillano":True},

]
vectorHeroes = ["Loki","thor","Scalet Witch","Hulk","iron man","Capi","black panter","vision"]
vecAux= ["Loki","Black Widow","Hulk","Rocket Racoonn"]
PersonajesConCS = []; #Para mostrar los perosnajes con iniciales C o S

#Cargamos ordenado por nombre
for v in datosHeroes:
    listaNuevaHeroesPorNombres.insertar(v,"Personaje")
#Cargamos ordenado por anio de aparicion
for v in datosHeroes:
    listaNuevaHeroesPorAnio.insertar(v,"Anio")

for v in vectorHeroes:
    listaHeroes.insertar(v)

for v in vecAux:
    listaAux.insertar(v)

# punto a
print("-->PUNTO A")
thor = listaHeroes.busqueda("thor")
if thor!=1:
    print("-Thor esta en la lista en la posición ->",thor)
#punto b
posScarlet = listaHeroes.busqueda("Scalet Witch")
if posScarlet!=-1:
    listaHeroes.modificar_elemento(posScarlet,"Scarlet Witch")
print("\n-->PUNTO B")
#verificamos si lo cambió
print("-Nuevo nombre-> ",listaHeroes.obtenerElemento(posScarlet))


#punto c
print("\n-->PUNTO C")
for i in range(listaAux.tamanio()):
    contador = 0;
    dato = listaAux.obtenerElemento(i)
    for j in range(listaAux.tamanio()):
        dato2 = listaHeroes.obtenerElemento(j)
        if dato==dato2:
            contador +=1
    if contador==0:
        print(">>Dato nuevo es ->",dato)
        listaHeroes.insertar(dato)


print("\n->PUNTO E")
pos7 = listaHeroes.obtenerElemento(7)
print("-Esta en la poscion 7 --> ",pos7)

print("\n-->PUNTO D")
print("BARRIDO desendente")
for i in range(listaHeroes.tamanio()):
    print(listaHeroes.obtenerElemento(i))


#BARRIDO ascendente
print("\nBARRIDO ascendente")
for i in reversed(range(0,listaHeroes.tamanio())):
    dato = listaHeroes.obtenerElemento(i)
    if (dato[0] == "S" or dato[0] == "C"):
        PersonajesConCS.append(dato)
    print(dato)

print("\n-->PUNTO F")
print("Los personajes con las iniciales S o C son -->  ",PersonajesConCS)
            
print("\n-->PUNTO G")
print("LISTADO ORDENADO POR NOMBRE:")
print(listaNuevaHeroesPorNombres.barrido())
print("LISTADO ORDENADO POR AÑO DE APARICIÓN:")
print(listaNuevaHeroesPorAnio.barrido())




