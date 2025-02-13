print("Diccionario de Python")
provincias = dict()
provincias = {
        924 : "Badajoz",
        956:  "Cádiz",
        958 : "Granada",    
        959 : "Huelva",    
        91 : "Madrid",    
        95 : "Málaga",    
        968 : "Murcia",    
        923 : "Salamanca",    
        95 : "Sevilla",    
        922 : "Sta. Cruz de Tenerife",    
        975 : "Soria",    
        96 : "Valencia",    
        976 : "Zaragoza"}
print(provincias)
print("---")

print(provincias.get(91))

for clave,valor in provincias.items():
    print("Prefijo: ", clave,"Provincia: ",valor)

print("Número de provincias:",len(provincias))

for claves in provincias.keys():
    print("Prefijo: ", claves)
print("----------------------------------------------------------")
for valores in provincias.values():
    print("Provincia: ", valores)

provincias.setdefault(925,"Toledo")
print(provincias)
#Si la clave existe no lo insertará
provincias.setdefault(91,"Toledo")
print(provincias)