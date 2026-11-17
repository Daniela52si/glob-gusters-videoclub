"""TCL (Transaction Control Language) para la base de datos Sistema_academico.

Demuestra COMMIT, ROLLBACK y SAVEPOINT con pagos, matrículas y estudiantes.
Requiere haber ejecutado antes 01_DDL.sql y 02_DML.sql.

Requisitos: Python 3.9+, PyMySQL configurado para este proyecto y un servidor MariaDB
en marcha con Sistema_academico creada.
Ejecución desde la raíz del proyecto, con el entorno virtual activado:
    python py/tcl.py
"""

# Funciones comunes de conexion.py.
from conexion import conexion, consultar, ejecutar, imprimir, principal


def main():
    # Conserva la configuración de host y usuario, pero selecciona la base requerida.
    with conexion(database="Sistema_academico") as con:
        # --- 1. COMMIT: confirmar el pago y activar la matrícula ------------------
        try:
            con.begin()
            n = ejecutar(
                con,
                "UPDATE pago SET estado_pago = %s WHERE pagoID = %s",
                ("Pagado", 4),
            )
            print(f"UPDATE pago: {n} fila(s)")

            n = ejecutar(
                con,
                "UPDATE matricula SET estado = %s WHERE matriculaID = %s",
                ("Activa", 4),
            )
            print(f"UPDATE matricula: {n} fila(s)")

            con.commit()
        except Exception:
            con.rollback()
            raise
        imprimir(
            "Pago confirmado",
            consultar(con, "SELECT pagoID, estado_pago FROM pago WHERE pagoID = %s", (4,)),
        )

        # --- 2. ROLLBACK: cancelar temporalmente un pago y deshacer el cambio -----
        con.begin()
        ejecutar(
            con,
            "UPDATE pago SET estado_pago = %s WHERE pagoID = %s",
            ("Cancelado", 1),
        )
        imprimir(
            "Pago dentro de la transacción",
            consultar(con, "SELECT pagoID, estado_pago FROM pago WHERE pagoID = %s", (1,)),
        )

        con.rollback()
        imprimir(
            "Pago después del ROLLBACK",
            consultar(con, "SELECT pagoID, estado_pago FROM pago WHERE pagoID = %s", (1,)),
        )

        # --- 3. SAVEPOINT: mantener el teléfono y deshacer solo la desactivación --
        try:
            con.begin()
            ejecutar(
                con,
                "UPDATE ESTUDIANTE SET Telefono = %s WHERE EstudianteID = %s",
                ("3000000001", 2),
            )
            ejecutar(con, "SAVEPOINT cambio_telefono")

            ejecutar(
                con,
                "UPDATE ESTUDIANTE SET activo = %s WHERE EstudianteID = %s",
                (False, 2),
            )
            ejecutar(con, "ROLLBACK TO SAVEPOINT cambio_telefono")
            con.commit()
        except Exception:
            con.rollback()
            raise

        estudiante = consultar(
            con,
            """SELECT EstudianteID, Nombre, Telefono, activo
               FROM ESTUDIANTE
               WHERE EstudianteID = %s""",
            (2,),
        )
        imprimir("Estudiante tras ROLLBACK TO SAVEPOINT y COMMIT", estudiante)


# Ejecuta main() solo al lanzar el archivo directamente.
if __name__ == "__main__":
    principal(main)
