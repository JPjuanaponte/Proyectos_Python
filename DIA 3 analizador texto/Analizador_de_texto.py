print('\n'+"="*80)
print("   🔍 ✨ SUPER ANALIZADOR DE TEXTO 3000 ✨ 🔍   ")
print("="*80+'\n')

texto = input("📝Ingresa el texto que deseas analizar: ")
letras = []

texto = texto.lower()

print("\n🎯 Ahora elige 3 letras para rastrear: 🔍")

letras.append(input("1️⃣ Ingresa la primera letra: ".lower()))
letras.append(input("2️⃣ Ingresa la segunda letra: ".lower()))
letras.append(input("3️⃣ Ingresa la tercera letra: ".lower()))

print("\n" + "📊" + " GENERANDO REPORTE " + "📊")
print("-" * 80)
# --- 1. CANTIDAD DE LETRAS ---
print("\n")
print("🔤 CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

# --- 2. CANTIDAD DE PALABRAS ---
print("\n📖 CANTIDAD DE PALABRAS")
palabras = texto.split() # divide el texo po defecvto en palabras que son los espacios
print(f"👉 Hemos encontrado {len(palabras)} palabras en tu mensaje.")
# --- 3. LETRAS DE INICIO Y FIN ---
print("\n")
print("\n📍 LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"🏁 La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")
# --- 4. TEXTO INVERTIDO ---

print("\n🔄 MODO ESPEJO(TEXTO INVERTIDO)")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"✨ Si ordenamos tu texto al revés va a decir: '{texto_invertido}'")


print("\n🐍 ¿ESTÁ LA PALABRA PYTHON EN EL TEXTO?")
buscar_python = 'python' in texto
dic = {True:"sí", False:"no"}
print(f"La palabra 🐍 'Python' {dic[buscar_python]} se encuentra en el texto")

print("\n" + "="*80)
print("       ✅ ¡Análisis completado con éxito! ✅       ")
print("="*80)