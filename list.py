lista_mixta = [1,2.23,"alejandro"]
lista_colores = ["red", "blue", "green"]

number_list = list((1, 2, 3, 4, 5));


#print(number_list)
#print(type(number_list))

# r = list(range(1,109999))
# print(r)

print(len(lista_colores))
print(lista_colores[-1])

#print(dir(lista_colores))
lista_colores.insert(len(lista_colores),"purple")
lista_colores.append("black")
lista_colores.extend(("orange","white"))

print(lista_colores)

print("purple" in lista_colores)

#las listas a diferecia de las tuplas son modificables
print(lista_mixta)
lista_mixta[1] = "andrade"
print(lista_mixta)
lista_mixta[0] = "soriano"
print(lista_mixta)
lista_colores.pop()
print(lista_colores)
lista_colores.remove("black")
print(lista_colores)
lista_colores.pop(0)
print(lista_colores)
#not working on 2.7 version lista_colores.clear()
print(lista_colores)


color.sort()
print(lista_colores)
