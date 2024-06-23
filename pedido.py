from te import Te


sabor =int(input("Ingrese el sabor del té."))
formato = int(input("Ingrese los gramos."))


te = Te(sabor, formato)

print(f"El sabor del te es: {te.obtener_sabor()}")
print(f"El formato es de {te.formato} gramos")
print (f"El precio del té es de: {Te.obtener_precio(formato)}")
tiempo, recomendacion = Te.obtener_tiempo_recomendacion(sabor)
print(f"El tiempo de preparación es: {tiempo} minutos.")
print(f"Se recomienda: {recomendacion}")
print(f"Vence en: {Te.duracion} días.")

