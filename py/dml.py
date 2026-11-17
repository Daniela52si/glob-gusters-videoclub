"""DML (Data Manipulation Language) para la base de datos Sistema_academico.

Carga datos de ejemplo en el orden de las llaves foráneas, actualiza cuatro registros
y elimina los datos de una matrícula. Requiere haber ejecutado antes 01_DDL.sql.
Las sentencias usan parámetros (%s) y se confirman en una sola transacción.

Requisitos: Python 3.9+, PyMySQL configurado para este proyecto y un servidor MariaDB
en marcha con Sistema_academico creada.
Ejecución desde la raíz del proyecto, con el entorno virtual activado:
    python py/dml.py
"""

# Funciones comunes de conexion.py.
from conexion import conexion, ejecutar, principal


def main():
    # Conserva la configuración de host y usuario, pero selecciona la base requerida.
    with conexion(database="Sistema_academico") as con:
        n = ejecutar(
            con,
            """INSERT INTO PROGRAMA_ACADEMICO
                   (programa_academicoID, Nombre, fecha_inicio, fecha_final, Descripcion)
               VALUES (%s, %s, %s, %s, %s), (%s, %s, %s, %s, %s), (%s, %s, %s, %s, %s)""",
            (
                1, "Ingenieria de Sistemas", "2026-02-01", "2030-12-01",
                "Programa profesional de 10 semestres",
                2, "Administracion de Empresas", "2026-02-01", "2030-12-01",
                "Programa profesional de 10 semestres",
                3, "Tecnologia en Analisis de Datos", "2026-02-01", "2029-06-01",
                "Programa tecnologico de 6 semestres",
            ),
        )
        print(f"INSERT PROGRAMA_ACADEMICO: {n} fila(s)")

        n = ejecutar(
            con,
            """INSERT INTO ESTUDIANTE
                   (EstudianteID, Nombre, Documento, programa_academicoID, Telefono, email, fecha_registro, activo)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s), (%s, %s, %s, %s, %s, %s, %s, %s),
                      (%s, %s, %s, %s, %s, %s, %s, %s), (%s, %s, %s, %s, %s, %s, %s, %s),
                      (%s, %s, %s, %s, %s, %s, %s, %s), (%s, %s, %s, %s, %s, %s, %s, %s)""",
            (
                1, "Laura Perez", "1001001", 1, "3001112233", "laura.perez@mail.com", "2026-01-15", True,
                2, "Carlos Ruiz", "1001002", 2, "3002223344", "carlos.ruiz@mail.com", "2026-01-16", True,
                3, "Maria Gomez", "1001003", 1, "3003334455", "maria.gomez@mail.com", "2026-01-17", True,
                4, "Andres Torres", "1001004", 3, "3004445566", "andres.torres@mail.com", "2026-01-18", True,
                5, "Sofia Ramirez", "1001005", 2, "3005556677", "sofia.ramirez@mail.com", "2026-01-19", True,
                6, "Juan Castro", "1001006", 3, "3006667788", "juan.castro@mail.com", "2026-01-20", False,
            ),
        )
        print(f"INSERT ESTUDIANTE: {n} fila(s)")

        n = ejecutar(
            con,
            """INSERT INTO PERIODO_ACADEMICO
                   (periodo_academicoID, nombre, fecha_registro, programa_academicoID)
               VALUES (%s, %s, %s, %s), (%s, %s, %s, %s),
                      (%s, %s, %s, %s), (%s, %s, %s, %s)""",
            (
                1, "2026-1", "2026-01-10", 1,
                2, "2026-1", "2026-01-10", 2,
                3, "2026-1", "2026-01-10", 3,
                4, "2026-2", "2026-07-01", 1,
            ),
        )
        print(f"INSERT PERIODO_ACADEMICO: {n} fila(s)")

        n = ejecutar(
            con,
            """INSERT INTO asignatura (asignaturaID, nombre, creditos)
               VALUES (%s, %s, %s), (%s, %s, %s), (%s, %s, %s),
                      (%s, %s, %s), (%s, %s, %s)""",
            (
                1, "Bases de Datos", 3,
                2, "Programacion I", 4,
                3, "Matematicas Basicas", 3,
                4, "Contabilidad General", 3,
                5, "Estadistica", 3,
            ),
        )
        print(f"INSERT asignatura: {n} fila(s)")

        n = ejecutar(
            con,
            """INSERT INTO PERIODO_ACADEMICO_ASIGNATURA (periodo_academicoID, asignaturaID)
               VALUES (%s, %s), (%s, %s), (%s, %s), (%s, %s),
                      (%s, %s), (%s, %s), (%s, %s), (%s, %s)""",
            (1, 1, 1, 2, 1, 3, 2, 3, 2, 4, 3, 1, 3, 5, 4, 1),
        )
        print(f"INSERT PERIODO_ACADEMICO_ASIGNATURA: {n} fila(s)")

        n = ejecutar(
            con,
            """INSERT INTO grupo (grupoID, asignaturaID, numero, cupo)
               VALUES (%s, %s, %s, %s), (%s, %s, %s, %s), (%s, %s, %s, %s),
                      (%s, %s, %s, %s), (%s, %s, %s, %s), (%s, %s, %s, %s)""",
            (
                1, 1, 1, 30, 2, 1, 2, 25, 3, 2, 1, 30,
                4, 3, 1, 40, 5, 4, 1, 35, 6, 5, 1, 30,
            ),
        )
        print(f"INSERT grupo: {n} fila(s)")

        n = ejecutar(
            con,
            """INSERT INTO horario (horarioID, grupoID, dia, hora_inicio, hora_fin, aula)
               VALUES (%s, %s, %s, %s, %s, %s), (%s, %s, %s, %s, %s, %s),
                      (%s, %s, %s, %s, %s, %s), (%s, %s, %s, %s, %s, %s),
                      (%s, %s, %s, %s, %s, %s), (%s, %s, %s, %s, %s, %s)""",
            (
                1, 1, "Lunes", "07:00:00", "09:00:00", "A-101",
                2, 2, "Martes", "09:00:00", "11:00:00", "A-102",
                3, 3, "Miercoles", "11:00:00", "13:00:00", "B-201",
                4, 4, "Jueves", "07:00:00", "09:00:00", "B-202",
                5, 5, "Viernes", "14:00:00", "16:00:00", "C-301",
                6, 6, "Sabado", "08:00:00", "10:00:00", "C-302",
            ),
        )
        print(f"INSERT horario: {n} fila(s)")

        n = ejecutar(
            con,
            """INSERT INTO matricula
                   (matriculaID, periodo_academicoID, estudianteID, fecha, estado, total)
               VALUES (%s, %s, %s, %s, %s, %s), (%s, %s, %s, %s, %s, %s),
                      (%s, %s, %s, %s, %s, %s), (%s, %s, %s, %s, %s, %s),
                      (%s, %s, %s, %s, %s, %s), (%s, %s, %s, %s, %s, %s)""",
            (
                1, 1, 1, "2026-01-25", "Activa", 1500000.00,
                2, 2, 2, "2026-01-26", "Activa", 1200000.00,
                3, 1, 3, "2026-01-27", "Activa", 1500000.00,
                4, 3, 4, "2026-01-28", "Pendiente", 900000.00,
                5, 2, 5, "2026-01-29", "Activa", 1200000.00,
                6, 3, 6, "2026-01-30", "Cancelada", 900000.00,
            ),
        )
        print(f"INSERT matricula: {n} fila(s)")

        n = ejecutar(
            con,
            """INSERT INTO matricula_grupo (matriculaID, grupoID)
               VALUES (%s, %s), (%s, %s), (%s, %s), (%s, %s), (%s, %s),
                      (%s, %s), (%s, %s), (%s, %s), (%s, %s), (%s, %s)""",
            (1, 1, 1, 3, 2, 4, 2, 5, 3, 2, 3, 4, 4, 6, 5, 4, 5, 5, 6, 6),
        )
        print(f"INSERT matricula_grupo: {n} fila(s)")

        n = ejecutar(
            con,
            """INSERT INTO pago
                   (pagoID, total, fecha_pago, metodo_pago, matriculaID, estado_pago)
               VALUES (%s, %s, %s, %s, %s, %s), (%s, %s, %s, %s, %s, %s),
                      (%s, %s, %s, %s, %s, %s), (%s, %s, %s, %s, %s, %s),
                      (%s, %s, %s, %s, %s, %s), (%s, %s, %s, %s, %s, %s)""",
            (
                1, 1500000.00, "2026-01-26", "Tarjeta de credito", 1, "Pagado",
                2, 1200000.00, "2026-01-27", "Transferencia", 2, "Pagado",
                3, 750000.00, "2026-01-28", "Efectivo", 3, "Parcial",
                4, 900000.00, "2026-01-29", "PSE", 4, "Pendiente",
                5, 1200000.00, "2026-01-30", "Tarjeta debito", 5, "Pagado",
                6, 900000.00, "2026-01-31", "Efectivo", 6, "Reembolsado",
            ),
        )
        print(f"INSERT pago: {n} fila(s)")

        n = ejecutar(
            con,
            "UPDATE ESTUDIANTE SET Telefono = %s WHERE EstudianteID = %s",
            ("3109998877", 1),
        )
        print(f"UPDATE ESTUDIANTE: {n} fila(s)")

        n = ejecutar(
            con,
            "UPDATE matricula SET estado = %s WHERE matriculaID = %s",
            ("Activa", 4),
        )
        print(f"UPDATE matricula: {n} fila(s)")

        n = ejecutar(
            con,
            "UPDATE pago SET total = %s, estado_pago = %s WHERE pagoID = %s",
            (1500000.00, "Pagado", 3),
        )
        print(f"UPDATE pago: {n} fila(s)")

        n = ejecutar(
            con,
            "UPDATE grupo SET cupo = cupo + %s WHERE grupoID = %s",
            (5, 1),
        )
        print(f"UPDATE grupo: {n} fila(s)")

        n = ejecutar(con, "DELETE FROM horario WHERE horarioID = %s", (6,))
        print(f"DELETE horario: {n} fila(s)")

        n = ejecutar(con, "DELETE FROM matricula_grupo WHERE matriculaID = %s", (6,))
        print(f"DELETE matricula_grupo: {n} fila(s)")

        n = ejecutar(con, "DELETE FROM pago WHERE matriculaID = %s", (6,))
        print(f"DELETE pago: {n} fila(s)")

        n = ejecutar(con, "DELETE FROM matricula WHERE matriculaID = %s", (6,))
        print(f"DELETE matricula: {n} fila(s)")

        con.commit()


# Ejecuta main() solo al lanzar el archivo directamente.
if __name__ == "__main__":
    principal(main)
