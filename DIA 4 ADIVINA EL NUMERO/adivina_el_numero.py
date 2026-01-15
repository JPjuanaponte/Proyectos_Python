from random import randint

intentos = 0
estimado = 0
numero_secreto = randint(1,100)

print("="*80)
print("   🌟 ¡BIENVENIDO AL DESAFÍO MENTAL! 🌟   ")
print("="*80)

nombre = input('👋 ¡Hola! Estoy emocionado de jugar contigo. ¿Cuál es tu nombre?:')

print(f'\n✨ ¡Perfecto, {nombre}! He seleccionado un número secreto entre 1 y 100 🧐\n🎯 Tienes 8 intentos para vencer al sistema. ¡Mucha suerte! 🍀\n')
print("👾"*40)

while intentos < 8:
    estimado = int(input("\n👉 ¿Qué número crees que es?: "))
    intentos += 1

    if estimado not in range(1,101):
        print('🚫 ¡Oye! Ese número ni siquiera está en el rango. 1 al 100, recuerda 💡')
        print("="*80)

    if estimado < numero_secreto:
        print('⬆️  ¡Mmm no! Mi número secreto es MÁS ALTO. ¡Sigue subiendo!')
        print("="*80)
    elif estimado > numero_secreto:
        print('⬇️  ¡Cuidado! Te pasaste, mi número secreto es MÁS BAJO.')
        print("="*80)
    else:
        print(f'\n🎉¡Brutal {nombre}!🎉, 🏆 has adivinado en {intentos} intentos')
        print("⭐" * 40)
        break
if estimado != numero_secreto:
    print("\n" + "💀" * 40)
    print(f'\n¡Oh no, {nombre}!.Se agotaron tus vidas❌ ...\n\nEl número secreto era {numero_secreto}\n\n¡No te rindas, vuelve a intentarlo! 🔄')

"""
Categoría,Emojis recomendados
Acción,🚀 🛸 🚁 🧨 ⚡ 🏹 🛡️
Efectos,✨ 💥 🔥 ❄️ 🌪️ 🌊 🌈
Premios,🏆 💎 👑 🎁 💰 🥇 ⭐
Robots/IA,🤖 👾 💻 🧠 🧬 📡 🦾
Humor,🤡 👻 👽 🦄 🍕 🌮 🍦
"""