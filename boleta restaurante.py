#input
nombre_cliente=input("inserte el nombre del cliente:")
nombre_mesero=input("ingrese el nombre del mesero:")
cant_arroz_pato=int(input("ingrese la cantidad de arroz con pato:"))
precio_arroz=int(input("ingrese el precio unitario del arroz con pato:"))

cant_chica=int(input("ingres la cantidad de jarras de chicha:"))
precio_chicha=int(input("ingrese el precio unitario de la chicha"))

cant_gelatina=int(input("ingrese la cantidad de la gelatina:"))
precio_gelatina=int(input("ingrese el precio de la gelatina:"))



#processing
total_arroz=(cant_arroz_pato*precio_arroz)
total_chicha=(cant_chica*precio_chicha)
total_gelatina=(cant_gelatina*precio_gelatina)
consumo=(total_arroz+total_chicha+total_gelatina)
igv=(consumo*0.18)
total_pago=(consumo+igv)


#output
print("######################################")
print("# RESTAURANTE - PATO RICO CON LOCHE   ")
print("######################################")
print("#Cliente:",nombre_cliente,"     Mesero:",nombre_mesero)
print("######################################")
print("#Producto        cantidad  P.U.  total")
print("#Arroz con pato:" ,cant_arroz_pato,precio_arroz   ,total_arroz)
print("#Jarra de chicha:",cant_chica     ,precio_chicha  ,total_chicha)
print("#Gelatina:"       ,cant_gelatina  ,precio_gelatina,total_gelatina)
print("######################################")
print("#Consumo       :"           ,consumo)
print("#IGV           :"           ,igv )
print("#Total a pagar :"           ,total_pago)
print("######################################")
