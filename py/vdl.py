"""VDL (View Definition Language) — vistas de Sistema_academico.

Crea y consulta las vistas definidas en 04_VDL.sql. La vista de prueba se crea,
consulta y elimina durante la ejecución normal; --drop elimina las vistas del script.

Requisitos: Python 3.9+, el paquete PyMySQL (`pip install -r requirements.txt` dentro del
entorno virtual .venv), un servidor MariaDB 10.2.1+ en marcha y la base Sistema_academico
ya creada. Instalación y comandos para Windows, macOS y Linux: README.md, secciones
«Dependencias requeridas» y «Guía de ejecución por sistema operativo».
Ejecución, con el entorno virtual instalado y ACTIVADO y desde la raíz del proyecto:
    python3 py/vdl.py          (macOS y Linux; en Windows: python py/vdl.py)
"""

# `sys` da acceso a los argumentos de la línea de comandos.
import sys

# Funciones comunes de conexion.py.
from conexion import conexion, consultar, ejecutar, imprimir, principal

# Cada vista: nombre -> (sentencia que la crea, consulta que la verifica).
VISTAS = {
    "vista_estudiantes_activos": (
        """CREATE OR REPLACE VIEW vista_estudiantes_activos AS
           SELECT EstudianteID, Nombre, Documento, email
           FROM ESTUDIANTE
           WHERE activo = TRUE""",
        "SELECT * FROM vista_estudiantes_activos",
    ),
    "vista_estudiante_programa": (
        """CREATE OR REPLACE VIEW vista_estudiante_programa AS
           SELECT ESTUDIANTE.Nombre AS estudiante,
                  PROGRAMA_ACADEMICO.Nombre AS programa
           FROM ESTUDIANTE
           INNER JOIN PROGRAMA_ACADEMICO
               ON ESTUDIANTE.programa_academicoID = PROGRAMA_ACADEMICO.programa_academicoID""",
        "SELECT * FROM vista_estudiante_programa",
    ),
    "vista_matriculas": (
        """CREATE OR REPLACE VIEW vista_matriculas AS
           SELECT matricula.matriculaID,
                  ESTUDIANTE.Nombre AS estudiante,
                  PERIODO_ACADEMICO.nombre AS periodo,
                  matricula.estado,
                  matricula.total
           FROM matricula
           INNER JOIN ESTUDIANTE
               ON matricula.estudianteID = ESTUDIANTE.EstudianteID
           INNER JOIN PERIODO_ACADEMICO
               ON matricula.periodo_academicoID = PERIODO_ACADEMICO.periodo_academicoID""",
        "SELECT * FROM vista_matriculas",
    ),
    "vista_pagos": (
        """CREATE OR REPLACE VIEW vista_pagos AS
           SELECT ESTUDIANTE.Nombre AS estudiante,
                  pago.total,
                  pago.metodo_pago,
                  pago.estado_pago
           FROM pago
           INNER JOIN matricula
               ON pago.matriculaID = matricula.matriculaID
           INNER JOIN ESTUDIANTE
               ON matricula.estudianteID = ESTUDIANTE.EstudianteID""",
        "SELECT * FROM vista_pagos",
    ),
    "vista_grupos": (
        """CREATE OR REPLACE VIEW vista_grupos AS
           SELECT asignatura.nombre AS asignatura,
                  grupo.numero AS grupo,
                  grupo.cupo,
                  horario.dia,
                  horario.aula
           FROM grupo
           INNER JOIN asignatura
               ON grupo.asignaturaID = asignatura.asignaturaID
           INNER JOIN horario
               ON horario.grupoID = grupo.grupoID""",
        "SELECT * FROM vista_grupos",
    ),
}


def main(argv):
    # Abre la conexión y la cierra al salir del bloque.
    with conexion() as con:
        # Con la opción --drop solo se eliminan las vistas y se termina.
        if "--drop" in argv:
            for nombre in VISTAS:
                ejecutar(con, f"DROP VIEW IF EXISTS `{nombre}`")
                print(f"Vista eliminada: {nombre}")
            ejecutar(con, "DROP VIEW IF EXISTS `vista_prueba`")
            print("Vista eliminada: vista_prueba")
            con.commit()
            return
        # Crea (o reemplaza) cada vista y muestra su contenido.
        for nombre, (crear, consulta) in VISTAS.items():
            ejecutar(con, crear)
            imprimir(nombre, consultar(con, consulta))

        # Consulta adicional de pagos pendientes.
        imprimir(
            "vista_pagos (estado_pago = 'Pendiente')",
            consultar(con, "SELECT * FROM vista_pagos WHERE estado_pago = 'Pendiente'"),
        )

        # Crea, consulta y elimina la vista de prueba definida en 04_VDL.sql.
        ejecutar(con, "CREATE VIEW vista_prueba AS SELECT Nombre FROM ESTUDIANTE")
        imprimir("vista_prueba", consultar(con, "SELECT * FROM vista_prueba"))
        ejecutar(con, "DROP VIEW vista_prueba")
        con.commit()


# Al lanzar el archivo, pasa a main() los argumentos (sin el nombre del script).
if __name__ == "__main__":
    principal(main, sys.argv[1:])
