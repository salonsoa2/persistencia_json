import persistencia_json as pj
lista_coches = list()
while True:
    marca = input("marca del coche:")
    if marca == "fin":
        break
    modelo = input("modelo del coche:")
    combustible = input("tipo de combustible que lleva:")
    cilindrada = input("cilindrada del coche:")
    cell_1 = {}
    cell_1["marca del coche"] = marca
    cell_1["modelo del coche"] = modelo
    cell_1["tipo de combustible que lleva"] = combustible
    cell_1["cilindrada del coche"] = cilindrada
    lista_coches.append(cell_1)

for cell_1 in lista_coches:
    print("Lista de coches:", cell_1)
pj.store(lista_coches, "coches.txt")
