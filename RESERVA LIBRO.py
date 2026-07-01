def registrar_usuario():
    while True:
        nombre = input("Nombre: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacio Intente nuevamente")
    while True:
        carrera = input("Carrera: ").strip()
        if carrera:
            break
        print("La carrera no puede estar vacio Intente nuevamente")
    nombre = nombre.title()
    carrera = carrera.title()
    return {"nombre": nombre, "carrera": carrera}


def registrar_libro():
    libro = input("Libro: ").strip()
    while True:
        try:
            dias = int(input("Dias de prestamo: ").strip())
            if dias <= 14:
                break
            print("El prestamo no puede superar los 14 dias Intente nuevamente")
        except ValueError:
            print("Ingrese un numero entero de dias")
    return {"libro": libro, "dias": dias}


def generar_resumen(usuario, reserva):
    aviso = ""
    if reserva["dias"] > 14:
        aviso = "Advertencia: El prestamo supera los 14 dias"
    resumen = (
        f"Usuario: {usuario['nombre']}\n"
        f"Carrera: {usuario['carrera']}\n"
        f"Libro: {reserva['libro']}\n"
        f"Dias de prestamo: {reserva['dias']}\n"
        f"{aviso}"
    )
    return resumen


def main():
    usuario = registrar_usuario()
    reserva = registrar_libro()
    print("\nResumen de reserva:")
    print(generar_resumen(usuario, reserva))


if __name__ == "__main__":
    main()
