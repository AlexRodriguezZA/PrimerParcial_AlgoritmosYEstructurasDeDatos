#Dado un vector con personaje de las películas de la saga de Star Wars resolver las
#siguientes actividades:
#a. Realizar un barrido recursivo del vector.
#b. Realizar una función recursiva que permita determinar si ‘Yoda’ está en el
# vector y en que posición

vectorPersonajes = ["boba Fett","cepo","darth veader","Yoda"]

def barridoRecursivo(vector,pos):
    print(vector[pos])
    if (pos == len(vector)-1):
        pass
    else:
        return barridoRecursivo(vector,pos+1)

def buscarYoda(vector,i):
    if (vector[i] == "Yoda"):
        print("Yoda está en la pos ",i)
    else:
        return buscarYoda(vector,i+1)
pos = 0;
i = 0;
print("BARRIDO RECURSIVO")
print(barridoRecursivo(vectorPersonajes,pos))
print("\nBUSQUEDA RECURSIVA -> YODA")
print(buscarYoda(vectorPersonajes,i))




