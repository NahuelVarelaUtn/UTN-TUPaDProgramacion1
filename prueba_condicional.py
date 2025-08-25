#Escribir un programa que pida al usuario la magnitud de un terremoto, clasificando la magnitud en una de las siguientes categorías:
# - Menor a 3.0: Muy leve
# - Entre 3.0 y 4: Leve 
# - mayor o igual a 4.0 y menor a 5 : Moderado
# - Mayor o igual a 5.0 y menor a 6 : fuerte
# - Mayor o igual a 6.0 y menor a 7 : Muy fuerte
# - Mayor o igual a 7.0: extremo 

magnitud = float(input("Introduce la magnitud del terremoto: "))
if magnitud > 0 and magnitud < 3:
    print("Muy leve")
elif 3 <= magnitud < 4:
    print("leve") 
elif 4 <= magnitud < 5:
    print("Moderado")
elif 5 <= magnitud <6:
    print("fuerte")
elif 6 <= magnitud < 7:
    print(("Muy fuerte"))
elif magnitud >=7 and magnitud < 10:
    print("extremo")
else:
    print("Ingresa una magnitud válida entre 0 y 10.")
