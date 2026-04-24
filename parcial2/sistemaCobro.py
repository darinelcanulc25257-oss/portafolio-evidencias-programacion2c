#---funciones(Modulo)

def d(subtotal, porcentaje):
    """
    Calcula el monto del dinero a descontar.
    Multiplica el subtotal por el porcentaje (ej. 15) dividido entre 100.
    """
    return subtotal * (porcentaje / 100)

def calcular_iva(sub_con_descuento, tasa):
    """
    Calcula el IVA sobre el monto que ya tiene el descuento aplicado.
    """
    return sub_con_descuento * tasa

# --- PROGRAMA PRINCIPAL ---

def main():
    # 1. Inicio del programa y captura de datos
    print("-- Ticket de ventas --")
    
    # Convertimos las entradas a float para poder hacer cálculos
    sub_inicial = float(input("Ingrese el subtotal de la compra: "))
    por_descuento = float(input("Ingrese el porcentaje de descuento: "))
    porcentaje_iva = 0.16
    
    # 2. Procesamos la información usando las funciones
    # Calculamos cuánto se descuenta
    monto_descuento = d(sub_inicial, por_descuento)
    
    # Obtenemos el nuevo subtotal y restamos el descuento
    subtotal_con_descuento = sub_inicial - monto_descuento
    
    # Calculamos el IVA sobre el nuevo subtotal
    monto_iva = calcular_iva(subtotal_con_descuento, porcentaje_iva)
    
    # Sumamos el subtotal rebajado más el IVA para el total
    total_final = subtotal_con_descuento + monto_iva
    
    # 3. Imprimimos los resultados
    print("\n--- RESUMEN DE COMPRA ---")
    print("Descuento aplicado: $", monto_descuento)
    print("Subtotal neto:      $", subtotal_con_descuento)
    print("IVA (16%):          $", monto_iva)
    print("TOTAL A PAGAR:      $", total_final)
    print("-------------------------")
    
    # 4. Opción de salir
    # Simplemente pedimos un input final. Al presionar Enter, 
    # el programa termina porque no hay más instrucciones.
    input("Presione ENTER para salir...")

# Llamada a la función principal para que el código se ejecute
main()