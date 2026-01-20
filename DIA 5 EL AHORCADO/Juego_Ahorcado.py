from random import choice

# Configuración inicial
palabras = ['perro', 'dinosaurio', 'helipuerto', 'tiburon', 'computador', 'colombia']
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas

def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('_')
    print('   ' + ' '.join(lista_oculta))

def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("\n👉 Elige una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print('🚫 ¡Oye! No has elegido una letra válida. Intenta de nuevo 💡')
    return letra_elegida

# --- INICIO DEL JUEGO ---
print("="*80)
print("   🔤 ¡BIENVENIDO AL DESAFÍO DEL AHORCADO! 🔤   ")
print("="*80)

nombre = input('👋 ¡Hola! Estoy emocionado de jugar contigo. ¿Cuál es tu nombre?: ')

print(f'\n✨ ¡Perfecto, {nombre}! He seleccionado una palabra secreta 🧐')
print(f'🎯 Tienes {intentos} vidas para descubrirla. ¡Que comience el juego! 🍀\n')
print("👾"*40)

palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print('\n' + '═' * 40)
    mostrar_nuevo_tablero(palabra)
    print('═' * 40)
    
    print(f'📉 Letras incorrectas: {"-".join(letras_incorrectas)}')
    print(f'❤️ Vidas restantes: {intentos}')
    print("="*40)

    letra = pedir_letra()

    # Lógica de chequeo
    if letra in palabra:
        if letra not in letras_correctas:
            letras_correctas.append(letra)
            aciertos += 1
            print("✅ ¡Excelente! Esa letra está en la palabra.")
        else:
            print("💡 Ya habías descubierto esa letra, ¡no pierdas el tiempo!")
    else:
        if letra not in letras_incorrectas:
            letras_incorrectas.append(letra)
            intentos -= 1
            print("❌ ¡Mmm no! Esa letra no vive aquí.")
        else:
            print("⚠️ Ya intentaste con esa letra y fallaste, ¡presta atención!")

    # Condición de victoria o derrota
    if intentos == 0:
        print("\n" + "💀" * 40)
        print(f'\n¡Oh no, {nombre}!. Se agotaron tus vidas ❌')
        print(f'La palabra secreta era: {palabra.upper()}')
        print('\n¡No te rindas, el conocimiento es poder! 🔄')
        juego_terminado = True
    
    elif aciertos == letras_unicas:
        mostrar_nuevo_tablero(palabra)
        print(f'\n🎉 ¡BRUTAL {nombre.upper()}! 🎉')
        print(f'🏆 Has descubierto la palabra con {intentos} vidas de sobra.')
        print("⭐" * 40)
        juego_terminado = True
