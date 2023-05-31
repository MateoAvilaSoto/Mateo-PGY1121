a=1
conp=0
conc=0
conpa=0
tot=0
dtot=0
dtotp=0
dtotc=0
dtotpa=0
print("Bienvenido a la de ropa ")
print("A continuacion se le mostraran los precios de nuestros articulos y sus correspondientes descuentos")
while a==1:
   print("  Articulo  | Precio | Descuento")
   print("------------------------------------------------")
   print("1.Poleras   | $2500  | 10% desde las 3 unidades ")
   print("2.Camisas   | $5000  | 12% desde las 4 unidades ")
   print("3.Pantalón  | $8000  | 30% desde las 2 unidades ")
   print("------------------------------------------------")
   print("4.Salir")
   print("5.Anular")
   print("6.Generar boleta")
   print("------------------------------------------------")
   op=int(input("Seleccione una opcion "))
    
   if op==1:
         print("Usted selecciono Poleras")
         print("Esta seguro de esta compra?")
         s=int(input("1.Si y 2.No, porfavor seleccione una opcion valida "))
         if s==1:
            conp=int(input("Cuantas Poleras va a querer? "))
         if s==2:
            print("")
         if s!=2 or 1:
            print("")
            print("")
 
   if op==2:
         print("Usted selecciono Camisas")
         print("Esta seguro de esta compra?")
         s=int(input("1.Si y 2.No, porfavor seleccione una opcion valida "))
         if s==1:
          conc=int(input("Cuantas Camisas va a querer? "))
         if s==2:
            print("")
         if s!=2 or 1:
            print("")
            print("")
 
   if op==3:
          print("Usted selecciono Pantalones")
          print("Esta seguro de esta compra?")
          s=int(input("1.Si y 2.No, porfavor seleccione una opcion valida "))
          if s==1:
           conpa=int(input("Cuantos Pantalones va a querer? "))
          if s==2:
            print("")
          if s!=2 or 1:
            print("")
            print("") 

   if op==4:
            a=0
    
   if op==5:
        conp=0
        conc=0
        conpa=0
        tot=0
        dtot=0
        dtotp=0
        dtotc=0
        dtotpa=0
   if op==6:
        tot=(conp*2500)+(conc*5000)+(conpa*8000)
        totp=conp*2500
        totc=conc*5000
        totpa=conpa*8000

        if conp>=3:
         dtotp=totp*0.9
        if conc>=4:
         dtotc=totc*0.88
        if conpa>=2:
         dtotpa=totpa*0.7
        dtot=dtotp+dtotc+dtotpa
        dtott=(tot-xd)
        if tot>0:
         print("  Articulo  | Cantidad | Valor unidad | SubTotal")
         print("------------------------------------------------")
         print(f" Poleras   | {conp}   |  $2500       | ${totp}")
         print(f" Camisas   | {conc}   |  $5000       | ${totc}")
         print(f" Pantalón  | {conpa}  |  $8000       | ${totpa}")
         print("------------------------------------------------")
         print(f"                  SubTotal              ${tot}")
         print(f"                  Descuento             ${dtot}")
         print("------------------------------------------------")
         print(f"                  Total a pagar         ${dtott}")
         print("------------------------------------------------")

         conp=0
         conc=0
         conpa=0
         tot=0
         dtot=0
         dtotp=0
         dtotc=0
         dtotpa=0
   if op!=4:
      print("Volviendo al menu...")


 