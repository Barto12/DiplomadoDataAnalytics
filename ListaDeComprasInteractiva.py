# Listas de compras
compras = ["leche", "huevo", "pan", "cafe"]

# agregar azucar

compras.append("azucar")

# Eliminar un articulo
compras.remove("huevo")

print("primer articulo:", compras[0])
print("ultimo articulo:", compras[-1])

# verificar si hay pan

hay_pan = "pan" in compras
print("¿Tengo que comprar pan?:", hay_pan)