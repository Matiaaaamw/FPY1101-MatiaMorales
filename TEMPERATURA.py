def validar_temperatura(texto):
    try:
        return float(texto)
    except ValueError:
        return None


def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas) if temperaturas else 0.0


def obtener_alerta(promedio):
    if promedio < 0:
        return "Frio intenso"
    if promedio < 10:
        return "Frio"
    if promedio < 20:
        return "Templado"
    if promedio < 30:
        return "Calor"
    return "Calor extremo"


def main():
    temperaturas = []
    while len(temperaturas) < 5:
        entrada = input(f"Temperatura {len(temperaturas) + 1}: ")
        temperatura = validar_temperatura(entrada)
        if temperatura is None:
            print("Entrada invalida Ingrese un numero valido")
            continue
        temperaturas.append(temperatura)

    promedio = calcular_promedio(temperaturas)
    print("\nReporte final")
    print("Temperaturas:", ", ".join(f"{t:.1f}" for t in temperaturas))
    print(f"Promedio: {promedio:.2f}")
    print(f"Alerta: {obtener_alerta(promedio)}")


if __name__ == "__main__":
    main()
