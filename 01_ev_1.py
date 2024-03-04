from datetime import datetime, timedelta

contador_clave = 0
contador_folio = 0
contador_cita_realizada = 0
registro_paciente = dict()
folio_cita = dict()
cita_realizada = dict()

hora_llegada_paciente = None
peso_paciente = None
altura_paciente = None

while True:
    print("\nBienvenidos al consultorio XXXXX")
    print("Acciones que se pueden realizar")
    print(
        " 1.- Registro de pacientes",
        "\n 2.- Programacion de citas",
        "\n 3.- Realizacion de citas programadas",
        "\n 4.- Consultas y reportes",
        "\n 5.- Salir del sistema",
    )
    try:
        eleccion_pacientes = int(input("\nElija una opción del menú: "))
    except Exception:
        print("\n\tEl texto debe ser entero. Intente de nuevo")
        continue

    if eleccion_pacientes == 1:
        while True:
            primer_apellido = input("\nIntroduzca el primer apellido: ").upper()
            if primer_apellido == "":
                print("\n\tEl dato no debe omitirse")
                continue
            elif primer_apellido.isalpha():
                break
            else:
                print("El dato no debe ser numerico. Intente de nuevo")
                continue

        while True:
            segundo_apellido = input("\nIntroduzca el segundo apellido: ").upper()
            if segundo_apellido == "":
                break
            elif segundo_apellido.isalpha():
                break
            else:
                print("El dato no debe ser numerico. Intente de nuevo.")
                continue
        while True:
            nombre = input("\nIntroduzca el nombre: ").strip().upper()
            if nombre == "":
                print("\n\tEl dato no debe omitirse")
                continue
            elif not nombre.replace(" ", "").isalpha():
                print(
                    "\n\tEl dato no debe contener números ni caracteres especiales, excepto espacios"
                )
                continue
            else:
                break
        while True:

            try:
                fecha_naci = input(
                    "\nIntroduzca Fecha de nacimiento (Valor de fecha en el formato mm/dd/aaa): "
                )
                fecha_nacimiento = datetime.strptime(fecha_naci, "%m/%d/%Y")
                if fecha_nacimiento < datetime.now():
                    break
                else:
                    print("\n\tLa fecha debe ser anterior al dia de hoy")
                    continue
            except Exception:
                print("\n\tEl dato debe ser en el formato indicado")
                continue

        contador_clave += 1
        registro_paciente[contador_clave] = [
            primer_apellido,
            segundo_apellido,
            nombre,
            fecha_nacimiento.strftime("%m/%d/%Y"),
        ]

        print("\n\t", registro_paciente)

    elif eleccion_pacientes == 2:
        if contador_clave == 0:
            print("\n\tDebe haber un paciente registrado")
            continue
        while True:
            try:
                clave_paciente = int(input("\nIntroduzca la clave del paciente: "))
            except Exception:
                print("\n\tLa clave de ser el formato deseado. Intente de nuevo")
                continue
            if clave_paciente in registro_paciente:
                break
            else:
                print("\n\tEl paciente no está registrado. Intente de nuevo.")
                continue

        while True:
            try:
                fecha_cita_str = input(
                    "\nIntroduzca la fecha de la cita (Valor de fecha en el formato mm/dd/aaaa): "
                )
                fecha_cita = datetime.strptime(fecha_cita_str, "%m/%d/%Y")
                if (
                    fecha_cita <= datetime.now() + timedelta(days=60)
                    and fecha_cita > datetime.now()
                ):
                    break
                else:
                    print(
                        "\n\tLa fecha debe ser mayor a la actual y no puede ser mayor a 60 días después de hoy. Intente de nuevo."
                    )
                    continue
            except Exception:
                print("\n\tLa fecha debe llevar el formato indicado. Intente de nuevo.")
                continue

        while True:
            try:
                turno_cita = int(
                    input(
                        "\nIntroduzca el turno del paciente 1.- mañana, 2.- mediodia, 3.- tarde: "
                    )
                )
                if turno_cita <= 4:
                    break
                else:
                    print(
                        "\n\tEl turno debe de ser solo los proporcionados. Intente de nuevo"
                    )
                    continue
            except Exception:
                print("\n\tEl valor debe ser numerico, Intente de nuevo")
                continue

        contador_folio += 1
        if clave_paciente in registro_paciente:
            folio_cita[contador_folio] = [
                clave_paciente,
                fecha_cita.strftime("%m/%d/%Y"),
                turno_cita,
            ]
            print("\n\tLa cita ya está programada")
            print("\n\t", folio_cita)

    elif eleccion_pacientes == 3:
        if contador_folio == 0:
            print("\n\tDebe de haber un folio registrado")
            continue
        while True:
            try:
                confirmacion_folio_cita = int(
                    input("\nIntroduzca el folio de su cita: ")
                )
                if confirmacion_folio_cita in folio_cita:
                    registro_clave = folio_cita[contador_folio][0]
                    hora_llegada_paciente = hora_actual = datetime.now().time()
                    print("\n\t", registro_clave)
                    break
                else:
                    print(
                        "\n\tEl folio no coincide. La cita no esta registrada. Intente de nuevo."
                    )
                    continue
            except Exception:
                print("\n\tEl dato debe ser numerico. Intente de nuevo.")
                continue

        while True:
            try:
                peso_paciente = float(input("\nIntroduzca el peso del paciente: "))
                break
            except Exception:
                print("\n\tEl peso debe de tener el formato correcto. Intente de nuevo")
                continue

        while True:
            try:
                altura_paciente = float(input("\nIntroduzca la altura del paciente: "))
                break
            except Exception:
                print("\n\tLa altura debe tener el formato correcto. Intente de nuevo")
                continue

        contador_cita_realizada += 1
        cita_realizada[contador_cita_realizada] = [
            hora_llegada_paciente.strftime("%H:%M:%S"),
            peso_paciente,
            altura_paciente,
            "La cita se realizó",
        ]
        print("\n\t", cita_realizada)

    elif eleccion_pacientes == 4:
        if contador_clave == 0:
            print("\n\tDebe de haber algun paciente registrado. Intente de nuevo")
            continue
        while True:
            print("\n=======SUBMENU CONSULTAS Y REPORTES=======")
            print(
                "1.- Reporte por citas",
                "\n2.- Reporte por pacientes",
                "\n3.- Regresar al menu principal",
            )
            try:
                opcion_sub_consultas_reportes = int(input("\nSelecciona la opción: "))
            except Exception:
                print("\n\tLa entrada debe ser un número entero. Intente de nuevo.")
                continue

            if opcion_sub_consultas_reportes == 1:
                if contador_folio == 0:
                    print("\n\tDebe haber alguna cita registrada. Intente de nuevo")
                    continue
                while True:
                    print("\n=======SUBMENU REPORTES DE CITAS=======")
                    print(
                        "1.- Por periodo",
                        "\n2.- Por paciente",
                        "\n3.- Regresar al sub menú",
                    )
                    try:
                        opcion_sub_reportes_citas = int(
                            input("\nElija una de las opciones: ")
                        )
                    except Exception:
                        print(
                            "\n\tLa entrada debe ser un número entero. Intente de nuevo."
                        )
                        continue

                    if opcion_sub_reportes_citas == 1:
                        while True:
                            try:
                                fecha_inicial_str = input(
                                    "\nIntroduzca la fecha inicial (Valor de la fecha en el formato mm/dd/aaaa): "
                                )

                                fecha_inicial = datetime.strptime(
                                    fecha_inicial_str, "%m/%d/%Y"
                                )
                                break
                            except Exception:
                                print(
                                    "\n\tEl dato debe estar en el formato proporcionado"
                                )
                                continue

                        while True:
                            try:
                                fecha_fin_str = input(
                                    "\nIntroduzca la fecha final (Valor de la fecha en el formato mm/dd/aaaa): "
                                )

                                fecha_fin = datetime.strptime(fecha_fin_str, "%m/%d/%Y")
                                if fecha_fin > fecha_inicial:
                                    break
                                else:
                                    print(
                                        "\n\tLa fecha inicial no debe ser mayor a la final. Intente de nuevo"
                                    )
                            except Exception:
                                print(
                                    "\n\tEl dato debe estar en el formato proporcionado"
                                )
                                continue
                        citas_en_periodo = []
                        for folio, datos_cita in folio_cita.items():
                            fecha_cita = datetime.strptime(datos_cita[1], "%m/%d/%Y")

                            if folio in cita_realizada:
                                if len(cita_realizada[folio]) > 4:
                                    (
                                        hora_llegada_paciente,
                                        peso_paciente,
                                        altura_paciente,
                                    ) = cita_realizada[folio][0:3]

                            if fecha_inicial <= fecha_cita <= fecha_fin:
                                clave_paciente = datos_cita[0]
                                fecha_cita_str = fecha_cita.strftime("%m/%d/%Y")
                                turno_cita = datos_cita[2]

                                citas_en_periodo.append(
                                    [
                                        folio,
                                        clave_paciente,
                                        fecha_cita_str,
                                        turno_cita,
                                        hora_llegada_paciente,
                                        peso_paciente,
                                        altura_paciente,
                                    ]
                                )

                        encabezado = "Folio\tClave\tFecha Cita\tTurno\tHora Llegada\tPeso\tAltura\tNombre"
                        print("*" * (len(encabezado) + 10))
                        print(encabezado)
                        print("*" * (len(encabezado) + 10))

                        for datos_cita_periodo in citas_en_periodo:
                            (
                                folio,
                                clave,
                                fecha_cita,
                                turno,
                                hora_llegada,
                                peso_paciente,
                                altura_paciente,
                            ) = datos_cita_periodo

                            nombre_paciente = " ".join(registro_paciente[clave][:-1])

                            print(
                                f"{folio:^6}\t{clave:^5}\t{fecha_cita:<20}\t{turno:^5}\t{hora_llegada_paciente}\t{peso_paciente or '':<5}\t{altura_paciente or '':<5}\t{nombre_paciente}"
                            )

                    elif opcion_sub_reportes_citas == 2:
                        while True:
                            try:
                                clave_busqueda_paciente = int(
                                    input(
                                        "\nIntroduzca la clave del paciente a buscar: "
                                    )
                                )

                            except Exception:
                                print(
                                    "\n\tLa clave debe ser un número entero. Intente de nuevo."
                                )
                                continue

                            resultados = []
                            if clave_busqueda_paciente in folio_cita:
                                datos_cita = folio_cita[clave_busqueda_paciente]
                                resultados.append(
                                    "\nCitas programadas y realizadas para el paciente:"
                                )
                                resultados.append(
                                    "Folio\tFecha\t\tTurno\tHora Llegada\tPeso\tAltura\tNombre"
                                )
                                resultados.append("*" * 90)

                                if (
                                    clave_busqueda_paciente in cita_realizada
                                    and cita_realizada[clave_busqueda_paciente]
                                ):
                                    datos_cita_realizada = cita_realizada[
                                        clave_busqueda_paciente
                                    ]
                                    nombre_paciente = " ".join(
                                        registro_paciente[clave_busqueda_paciente][:-1]
                                    )
                                    resultados.append(
                                        f"{clave_busqueda_paciente}\t{datos_cita[1]}\t{datos_cita[2]}\t{datos_cita_realizada[0]}\t{datos_cita_realizada[1]}\t{datos_cita_realizada[2]}\t{nombre_paciente}"
                                    )
                                else:
                                    nombre_paciente = " ".join(
                                        registro_paciente[clave_busqueda_paciente][:-1]
                                    )
                                    resultados.append(
                                        f"{clave_busqueda_paciente}\t{datos_cita[1]}\t{datos_cita[2]}\t\t\t\t\t\t{nombre_paciente}"
                                    )
                            else:
                                resultados.append(
                                    "\n\tNo se encontró ninguna cita programada para el paciente."
                                )

                            print("\n".join(resultados))

                            resultados = []
                            break

                    elif opcion_sub_reportes_citas == 3:
                        break

                    else:
                        print(
                            "\n\tLa opción debe ser alguna de las proporcionadas. Intente de nuevo."
                        )
                        continue

            elif opcion_sub_consultas_reportes == 2:
                while True:
                    print("\n=======SUBMENU REPORTES DE PACIENTES=======")
                    print("1. Lista de los pacientes registrados")
                    print("2. Búsqueda de paciente por clave")
                    print("3. Búsqueda de pacientes por apellidos y nombres")
                    print("4. Regresar al submenu")
                    try:
                        opcion_sub_reportes_pacientes = int(
                            input("\nAcciones que se pueden realizar en Consultas: ")
                        )
                    except Exception:
                        print(
                            "\n\tLa entrada debe ser un número entero. Intente de nuevo."
                        )
                        continue

                    if opcion_sub_reportes_pacientes == 1:
                        encabezado = "Clave\tPrimerApellido\tSegundoApellido\tnombre\tfechanacimiento"
                        print("*" * (len(encabezado) + 10))
                        print(encabezado)
                        print("*" * (len(encabezado) + 10))

                        for clave, datos_paciente in registro_paciente.items():
                            primer_apellido = datos_paciente[0]
                            segundo_apellido = (
                                datos_paciente[1] if datos_paciente[1] else ""
                            )
                            nombre = datos_paciente[2]
                            fecha_nacimiento = datos_paciente[3]

                            print(
                                f"{clave:^5}\t{primer_apellido:^8}\t{segundo_apellido:^10}\t{nombre:^10}\t{fecha_nacimiento:^5}"
                            )
                        print("\nSe mostraran los registros de pacientes")
                        continue

                    elif opcion_sub_reportes_pacientes == 2:
                        while True:
                            try:
                                clave_busqueda_paciente = int(
                                    input(
                                        "\nIntroduzca la clave del paciente a buscar: "
                                    )
                                )

                            except Exception:
                                print(
                                    "\n\tLa clave debe ser un número entero. Intente de nuevo."
                                )
                                continue
                            if clave_busqueda_paciente in registro_paciente:
                                datos_paciente = registro_paciente[
                                    clave_busqueda_paciente
                                ]
                                print("\nDatos del paciente:")
                                encabezados = [
                                    "Clave",
                                    "PrimerApellido",
                                    "SegundoApellido",
                                    "nombre",
                                    "fechanacimiento",
                                ]
                                separador = "*" * (
                                    len("".join(encabezados)) + len(encabezados) * 3
                                )

                                print(encabezados)
                                print(separador)
                                print(
                                    f"{clave_busqueda_paciente}\t{datos_paciente[0]}\t{datos_paciente[1]}\t{datos_paciente[2]}\t{datos_paciente[3]}"
                                )
                                break
                            else:
                                print(
                                    "\n\tNo se encontró un paciente con esa clave. Intente de nuevo"
                                )
                                continue

                    elif opcion_sub_reportes_pacientes == 3:
                        while True:
                            apellidos_nombres = input(
                                "\nIntroduzca los apellidos y nombres del paciente a buscar: "
                            )
                            if not apellidos_nombres.isalpha():
                                print(
                                    "\n\tEl dato debe ser un formato adecuado. Intente de nuevo"
                                )
                                continue
                            resultados_busqueda = []
                            for clave, datos in registro_paciente.items():
                                nombre_completo = f"{datos[0]} {datos[1]} {datos[2]}"
                                if apellidos_nombres.lower() in nombre_completo.lower():
                                    resultados_busqueda.append(
                                        [clave, datos[0], datos[1], datos[2], datos[3]]
                                    )
                            if len(resultados_busqueda) > 0:
                                encabezado = "Clave\tPrimerApellido\tSegundoApellido\tnombre\tfechanacimiento"
                                print("*" * (len(encabezado) + 10))
                                print(encabezado)
                                print("*" * (len(encabezado) + 10))

                                for resultado in resultados_busqueda:
                                    print(
                                        f"{resultado[0]:^5}\t{resultado[1]:^8}\t{resultado[2]:^10}\t{resultado[3]:^10}\t{resultado[4]:^5}"
                                    )
                            else:
                                print(
                                    "\n\tNo se encontraron pacientes con esos apellidos y nombres."
                                )
                            break

                    else:
                        break

            elif opcion_sub_consultas_reportes == 3:
                break

            else:
                print(
                    "\n\tLa opción debe ser alguna de las proporcionadas. Intente de nuevo."
                )
                continue

    elif eleccion_pacientes == 5:
        while True:
            salir = input("\n¿Seguro que desea salir? Introduzca SI o NO: ")
            if salir.upper() == "SI":
                break
            elif salir.upper() == "NO":
                break
            else:
                print("\n\tLa opcion debe ser una de las indicadas. Intente de nuevo")
                continue
        if salir.upper() == "SI":
            break

    else:
        print("\n\tEl dato debe ser un numero del 1 al 5. Intente de nuevo")
        continue
