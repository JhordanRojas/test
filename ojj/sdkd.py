#Area de un trapecio
base_menor,base_mayor,altura,area=0.0,0.0,0.0,0.0

#asignacion de valores
base_mayor=8
base_menor=17
altura=5

#calculo
area=((base_mayor+base_menor)*altura)

#mostrar valores
print("el valor de la base menor es:",base_menor,"m")
print("el valor de la base mayor es:",base_mayor,"m")
print("el valor de la altura es:",altura,"m")
print("el valor del area del trapecio es:",area,"m")

#verificador 3
area_pequena=(area<80)
print("El trapecio tiene area pequeña:",area_pequena)
