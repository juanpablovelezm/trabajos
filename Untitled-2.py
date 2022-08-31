
print("\nvamos a calcular tu indice de masa corporal")
estatura=float(input("\nIngresa tu estatura en metros\t"))
peso=float(input("\nIngresa tu peso en kilogramos\t"))
edad= int(input("\nIngresa tu edad\t"))

if edad ==16:
    Imc=peso/estatura**2

    print(f"\n{round(Imc,1)}")


    if Imc < 18.5:
        tipo_de_peso="Bajo peso"

    elif Imc >= 18.5 and Imc<=24.9:
        tipo_de_peso="Peso normal "

    elif Imc >= 25.0 and Imc <= 29.9:
        tipo_de_peso="Sobre peso"

    elif Imc >= 30.0 and Imc <= 34.9:
        tipo_de_peso="Obesidad clase 1"

    elif Imc >= 35.0 and Imc <= 39.9:
        tipo_de_peso="Obesidad clase 2"

    elif Imc >= 40.0:
        tipo_de_peso="Obesidad"

    print(f"\nTienes {tipo_de_peso}")

if edad ==17:
    Imc=peso/estatura**2
    print(f"\n{round(Imc,1)}")

    

    if Imc < 18.5:
        tipo_de_peso="Bajo peso"

    elif Imc >= 20.0 and Imc<=25.9:
        tipo_de_peso="Peso normal "

    elif Imc >= 25.0 and Imc <= 29.9:
        tipo_de_peso="Sobre peso"

    elif Imc >= 30.0 and Imc <= 34.9:
        tipo_de_peso="Obesidad clase 1"

    elif Imc >= 35.0 and Imc <= 39.9:
        tipo_de_peso="Obesidad clase 2"

    elif Imc >= 40.0:
        tipo_de_peso="Obesidad"

    print(f"\nTienes {tipo_de_peso}")
