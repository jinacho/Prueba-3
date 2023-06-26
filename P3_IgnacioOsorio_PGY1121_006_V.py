def grabar(codigo, tipo, comuna, fecha, precio, valor):
    for x in range(len(casas)):
        if casas[x][0] == codigo.upper():
            print("[ERROR BD01] Codigo ya existente en base de datos.")
            return False
    if type(codigo) == str:
        if len(codigo) == 6:
            if int(codigo[4]) and int(codigo[5]):
                if type(codigo[0]) == str and type(codigo[1]) == str and type(codigo[2]) == str and type(codigo[3]) == str:
                    if tipo.lower() == "arriendo" or tipo.lower() == "venta":
                        if valor.lower() == "uf" or valor.lower() == "clp":
                            datos = [codigo.upper(), tipo.upper(), comuna.upper(), fecha, precio, valor.upper()]
                            casas.append(datos)
                            print("\nAñadiendo a la base de datos")
                            return True
                        else:
                            print("[ERROR BA01] Valor erroneo | Formato : UF ó CLP") 
                    else:
                        print("[ERROR CA01] Tipo erroneo | Formato : Arriendo ó Venta")
                else:
                    print("[ERROR AF04] Codigo erroneo | Formato : ABCD12")
            else:
                print("[ERROR AF03] Codigo erroneo | Formato : ABCD12")
        else:
                print("[ERROR AF02] Codigo erroneo | Formato : ABCD12")
    else:
        print("[ERROR AF01] Codigo erroneo | Formato : ABCD12")
    return False

def buscar(codigo):
    encontrado = False
    for x in range(len(casas)):
        if casas[x][0] == codigo:
            encontrado= True
            print("\n----Codigo",casas[x][0])
            print("Tipo",casas[x][1])
            print("Comuna",casas[x][2])
            print("Fecha",casas[x][3])
            if casas[x][5] == "CLP" :
                print("Precio $"+casas[x][4]+" pesos")
            else:
                print("Precio",casas[x][4],casas[x][5])
    if encontrado == False:
        print("No se encontró una propiedad con ese codigo\n")
def imprimir():
    if len(casas) >= 1:
        for x in range(len(casas)):
            print("\n----Codigo",casas[x][0])
            print("Tipo",casas[x][1])
            print("Comuna",casas[x][2])
            print("Fecha",casas[x][3])
            if casas[x][5] == "CLP" :
                print("Precio $"+casas[x][4]+" pesos")
            else:
                print("Precio",casas[x][4],casas[x][5])
    else:
        print("\nBase de datos vacia\n")
def salir():
    menu = False
    quit()

casas = []
menu = True
while menu == True:
    print("||  Menu")
    print("||  1)Grabar propiedad")
    print("||  2)Buscar propiedad")
    print("||  3)Imprimir información")
    print("||  4)Salir")
    opc = input("")    
    if opc == "1":
        print("||  Grabar propiedad\n")
        codigo = input("Ingresa el codigo | Formato : ABCD12\n")
        tipo = input("Ingresa el tipo | Formato : Arriendo ó Venta\n")
        comuna = input("Ingresa la comuna | Formato : 'Las Condes'\n")
        fecha = input("Ingresa la fecha | Formato : DD/MM/AAAA\n")
        precio = input("Ingresa el precio | Formato : '100000' (NO DECIMALES)\n")
        valor = input("Ingresa el valor | Formato : UF ó CLP\n")
        v = grabar(codigo, tipo, comuna, fecha, precio, valor)
        if v :
            print("Propiedad agregada a la base de datos con exito.\n")
    elif opc == "2":
        print("||  Buscar propiedad\n")
        cod = input("Ingrese el codigo a buscar | Formato : ABCD12\n").upper()
        buscar(cod)
    elif opc == "3":
        print("||  Imprimir información")
        imprimir()
            
    elif opc == "4":
        print("||  Saliendo del programa")
        salir()
        
