"""DCL (Data Control Language) para la base de datos Sistema_academico.

Crea las cuentas de estudiante, profesor y administrador, concede sus permisos,
revoca UPDATE al profesor y elimina al administrador al final. Las claves se leen
de las variables de entorno SISTEMA_ACADEMICO_PASS_ESTUDIANTE,
SISTEMA_ACADEMICO_PASS_PROFESOR y SISTEMA_ACADEMICO_PASS_ADMIN; no se imprimen.

Requisitos: Python 3.9+, PyMySQL instalado y un servidor MariaDB en marcha, con
Sistema_academico ya creada. Ejecución desde la raíz del proyecto:
    python py/dcl.py
"""

import os

from conexion import conexion, consultar, ejecutar, principal

BD = "Sistema_academico"
USUARIOS = {
    "estudiante_user": ("SISTEMA_ACADEMICO_PASS_ESTUDIANTE", "SELECT"),
    "profesor_user": ("SISTEMA_ACADEMICO_PASS_PROFESOR", "SELECT, INSERT, UPDATE"),
    
}


def main():
    cuentas = {}
    for usuario, (variable, privilegios) in USUARIOS.items():
        clave = os.getenv(variable)
        if not clave:
            raise RuntimeError(f"Define la variable de entorno {variable}.")
        cuentas[usuario] = (clave, privilegios)

    with conexion(database=BD) as con:
        for usuario, (clave, privilegios) in cuentas.items():
            cuenta = f"'{usuario}'@'localhost'"
            ejecutar(con, f"CREATE USER IF NOT EXISTS {cuenta} IDENTIFIED BY %s", (clave,))
            ejecutar(con, f"GRANT {privilegios} ON `{BD}`.* TO {cuenta}")
            print(f"Usuario {cuenta}: GRANT {privilegios}")

        ejecutar(con, f"GRANT SELECT ON `{BD}`.pago TO 'estudiante_user'@'localhost'")

        _mostrar_grants(con, "estudiante_user")
        _mostrar_grants(con, "profesor_user")
        _mostrar_grants(con, "admin_user")

        ejecutar(con, f"REVOKE UPDATE ON `{BD}`.* FROM 'profesor_user'@'localhost'")
        _mostrar_grants(con, "profesor_user")

        ejecutar(con, "DROP USER 'admin_user'@'localhost'")


def _mostrar_grants(con, usuario):
    print(f"\n== Privilegios de {usuario} ==")
    for fila in consultar(con, f"SHOW GRANTS FOR '{usuario}'@'localhost'"):
        print(next(iter(fila.values())))


if __name__ == "__main__":
    principal(main)
