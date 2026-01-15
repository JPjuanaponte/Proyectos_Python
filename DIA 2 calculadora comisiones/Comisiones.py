print("="*80)
print("   💰 SISTEMA DE GESTIÓN DE COMISIONES v2.0 💰   ")
print("="*80)

nombre = input("\n👤 Por favor, ingresa tu nombre de agente: ")
ventas = int(input("📈 ¿Cuál fue el total de tus ventas este mes? (USD): "))

comision = round(ventas * 13 / 100,2)
print("\n" + "─" * 80)
print(f"📊 RESUMEN DE RENDIMIENTO PARA: {nombre.upper()}")
print(f"💳Ventas Totales:  ${ventas}")
print(f" Tu comisión de venta es de: ${comision} 💵 ")