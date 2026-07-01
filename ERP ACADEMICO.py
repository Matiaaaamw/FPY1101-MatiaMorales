def mostrar_menu():
    print("\nMini ERP Academico")
    print("1. Registrar alumno y notas")
    print("2. Mostrar alumnos registrados")
    print("3. Salir")


def leer_nota(mensaje):
    while True:
        try:
            nota = float(input(mensaje))
            if 1.0 <= nota <= 7.0:
                return nota
            print("La nota debe estar entre 1.0 y 7.0 Intente otra vez")
        except ValueError:
            print("Entrada no valida Ingrese un numero decimal, por ejemplo 4.5")


def calcular_promedio(notas):
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


def estado_academico(promedio):
    if promedio >= 6.0:
        return "Aprobado"
    if promedio >= 4.0:
        return "Condicional"
    return "Reprobado"


def registrar_alumno(alumnos):
    nombre = input("Nombre del alumno: ").strip()
    if not nombre:
        print("El nombre no puede estar vacio")
        return

    notas = []
    for i in range(1, 4):
        nota = leer_nota(f"Nota {i} (1.0-7.0): ")
        notas.append(nota)

    promedio = calcular_promedio(notas)
    alumnos[nombre] = {
        "notas": notas,
        "promedio": promedio,
        "estado": estado_academico(promedio)
    }
    print(f"Alumno {nombre} registrado Promedio: {promedio:.2f} Estado: {alumnos[nombre]["estado"]}")


def mostrar_alumnos(alumnos):
    if not alumnos:
        print("No hay alumnos registrados")
        return

    print("\nAlumnos registrados:")
    for nombre, datos in alumnos.items():
        notas_str = ", ".join(f"{nota:.1f}" for nota in datos["notas"])
        print(f"- {nombre}: notas [{notas_str}], promedio {datos["promedio"]:.2f}, estado {datos["estado"]}")


def main():
    alumnos = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_alumno(alumnos)
        elif opcion == "2":
            mostrar_alumnos(alumnos)
        elif opcion == "3":
            print("Saliendo del sistema Hasta luego")
            break
        else:
            print("Opcion no valida. Elija 1, 2 o 3")


if __name__ == "__main__":
    main()
