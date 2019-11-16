#calcular el volumen de una piramide triangular
volumen,area_base,altura_piramide,base_triangle,altura_triangle=0.0,0.0,0.0,0.0,0.0

#asignacion de valores
altura_piramide=7
base_triangle=12
altura_triangle=4

#calculos
area_base=((base_triangle*altura_triangle)/2)
volumen=((area_base*altura_piramide)/3)

#mostrar resultados
print("la base de la piramide es un triangulo y su area es:",area_base)
print("la altura de la piramide es:",altura_piramide)
print("el volumen de la piramide es:",volumen,"metros cubicos")

#verificador 9
piramide_pequena=(volumen<55)
print("El volumen de la piramide es pequeño:",piramide_pequena)
