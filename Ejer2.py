from cola import Cola;
from pila import Pila;

colaNotificaciones = Cola();
ColaAux = Cola();
pila = Pila();
Notificaciones = [
    {"Hora":16,"app":"Facebook","Mensaje":"Hola aleex"},
    {"Hora":5,"app":"Instagram","Mensaje":"jelooou"},
    {"Hora":21,"app":"Facebook","Mensaje":"Hola pibee"},
    {"Hora":23,"app":"Twitter","Mensaje":"Cursos Python"}
]

for n in Notificaciones:
    colaNotificaciones.arribo(n)

palabraClave = "Python"

while (not colaNotificaciones.cola_vacia()):
    dato = colaNotificaciones.atencion()
    print(dato)
    if (dato["app"] == "Facebook"):
        print(">Notificación de FACEBOOK eliminada")
        pass
    else:
        ColaAux.arribo(dato) ##No perdemos datos en la cola, Cargamos los elementos sin las noti de FACEBOOK
    if (dato["app"] == "Twitter"):
        if palabraClave in dato["Mensaje"]:
            print("\n>>Palabra clave encontrada<<") 
            print("-Mensaje:")
            print(dato["Mensaje"])
    if (dato["app"] == "Instagram"):
        pila.apilar(dato)

#VOLVEMOS A CARGAR LOS DATOS A LA PILA ORiGINAL
while not ColaAux.cola_vacia():
    dato = ColaAux.atencion()
    colaNotificaciones.arribo(dato)

print("\nDATOS FINALES DE LA COLA")
while not colaNotificaciones.cola_vacia():
    dato = colaNotificaciones.atencion()
    print(dato)

print("\nDATOS FINALES DE LA PILA")
while not pila.pila_vacia():
    datoPIla = pila.desapilar()
    print(datoPIla)


    





