

nombre=str(input("Escribe tu nombre con apellido\t"))
documento=int(input("Ingresa tu numero de identificacion\t"))


horas_trabajadas=int(input("ingresa el numero de las horas trabajadas   "))
precio_hora=float(input("ingresa el valor de la hora trabajada  "))

#las horas ordinarias son 40 horas
if horas_trabajadas<=40:
    pago_normal=horas_trabajadas*precio_hora
    print(f"{nombre} con numero de identificacion {documento}\n")
    print(f"Tu pago total es: {pago_normal}\n")

elif horas_trabajadas>40:
    horas_extras=horas_trabajadas-40
    horas_normales=horas_trabajadas-horas_extras
    precio_xh_extra=25*precio_hora /100
    h_extras=precio_xh_extra*horas_extras
    precio_sin_estra=precio_hora*horas_extras
    total_xh_extras=precio_sin_estra+h_extras
    pago_normal=horas_normales*precio_hora
    pago_total=horas_normales*precio_hora+total_xh_extras
    print(f"{nombre} con numero de identificacion {documento}\n")
    print(f"Tu pago Horas ordinarias es: {pago_normal}\n")
    print(f"Tu pago de horas extras es: {total_xh_extras}\n")
    print(f"Tu pago total es: {pago_total}\n")
