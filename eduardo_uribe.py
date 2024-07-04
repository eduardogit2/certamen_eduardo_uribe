from os import system
system("cls")
sectores = ["Concepción", "Chiguayante", "Talcahuano", "Hualpén", "San Pedro"]
#link de github 
"""
Recuerde las validaciones implícitas en el problema.
• Recuerde utilizar librería para limpiar pantalla haciendo más fácil su visualización y generar números aleatorios
para generar el ID de pedido
• Cada opción de la aplicación debe desarrollarse en una función que, pudiendo estar en archivos separados o
en un mismo archivo, deben se llamadas desde el programa principal"""
#funciones
"""Para registrar un pedido se requiere lo siguiente: Nombre y apellido del cliente, comuna, detalle del pedido. Por ejemplo, la empresa vende
dispensadores de 6, 10 y 20 litros. Debe permitir ingresar la cantidad de cada cilindro a solicitar y considerar que la suma de las cantidades
(de cada cilindro) deben sumar más de cero (para que tenga sentido el pedido)."""
def registrar():
    registro = {}
    while True:
        nombre = input("ingrese su nombre y apellido ")
        if len(nombre) >= 0 and nombre.replace(" ", "").isalpha() and " " in nombre:
            print("nombre ingresado correctamente ")
            break
        else:
            print("nombre ingresado incorrectamente ")
    while True:
        direccion = input("ingrese su direccion ")
        if len(direccion) <= 0:
            print("direccion ingresada incorrectamente")
        else:
            break
    while True:
        sector = input("ingrese su sector ")
        if len(sector) <= 0:
            print("sector ingresado incorrectamente")
        else:
            break
    cil6 = 0
    cil10 = 0
    cil20 = 0
    while True:
        system("cls")
        print("""
ingrese el timpo de cilindro que desea
1.- 6 litros
2.- 10 litros
3.- 20 litros
4.- salir
""")
        op = input("ingrese una opcion ")
        match op:
            case "1":
                cil6 = cil6+1
            case "2":
                cil10 = cil10+1
            case "3":
                cil20 = cil20+1
            case "4":
                if (cil6 +  cil10 + cil20) == 0:
                    print("no se ha cargado ningun cilindro ")
                    system("pause")
                else:
                    print("hasta luego ")
                    break 
            case other:
                print("opcion invalida ")
                system("pause")

    registro = {"nombre":nombre , "direccion": direccion,"sector": sector, "cil6": cil6,"cil10": cil10,"cil20": cil20}
    return registro

"""Debe mostrar en la pantalla la lista de todos los pedidos realizados en un formato similar al ejemplo anterior de registro de pedidos. Al
listar se DEBE INCLUIR el encabezado tal y como se muestra en la imagen anterior."""
def listar(lista):
    """print("ID pedido", "Cliente", "Direccion", "|", "Sector", "Disp.6lts","Disp.10lts", "Disp.20lts", sep="     ")
    for cosas in lista:
        print("",cosas['nombre'], cosas['direccion'],"|", cosas['sector'], cosas['cil6'],cosas['cil10'],cosas['cil20'] ,sep="     ")"""
    pass
"""Para imprimir la hoja de ruta, el usuario debe seleccionar alguno de los sectores donde es posible realizar un pedido. Estos sectores deben
estar previamente definidos en algún tipo de colección de Python en el código, los sectores son: Concepción, Chiguayante, Talcahuano,
Hualpén, San Pedro.Subdirección de Evaluación de Resultados de Aprendizaje - Subdirección de Diseño Instruccional 2- 2023 5
Al seleccionar uno de los sectores, se generará un archivo de texto (.csv) con el detalle de los pedidos que se deberá llevar al sector. Este
debe tener la misma forma del registro completo de las opciones anteriores, pero en archivo de texto. Este archivo debe contener el
encabezado del detalle de pedido."""
def imprimir(sectores):
  """  sector = input("ingrese el sector a buscar ")
    for sec in sectores:
        if sec == sectores:
            f=open(f"pedidos_{sector}.csv", "w")
            f.write("ID pedido", "CLiente", "Direccion", "|", "Sector", "Disp.6lts","Disp.10lts", "Disp.20lts", sep="     ")
            print("datos imprimidos correctamente") """
  pass
"""Debe pedir al usuario ingresar un id del pedido y mostrar su detalle"""
def buscar():
    pass

#main
lista={}
while True:
    system("cls")
    print("""
1. Registrar pedido
2. Listar los todos los pedidos
3. Imprimir hoja de ruta
4. Buscar un pedido por ID
5. Salir del programa
""")
    op = input("Ingrese una opcion ")
    match op:
        case "1":
            lista = registrar()
            system("pause")
        case "2":
            system("pause")
            pass
        case "3":
            system("pause")
            pass
        case "4":
            system("pause")
            pass
        case "5":
            print("hasta luego ")
            system("pause")
            break
        case other:
            print("opcion invalida ")
            system("pause")