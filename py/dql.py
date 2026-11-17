"""DQL (Data Query Language) para la base de datos Sistema_academico.

Consultas de solo lectura definidas en el script 03_DQL.sql de Sistema_academico.
Sin argumentos ejecuta todas; con un nombre ejecuta una sola:
    python py/dql.py 08_pagos_mas_altos

Requisitos: Python 3.9+, el paquete PyMySQL y la base Sistema_academico creada.
Ejecución desde la raíz del proyecto con el entorno virtual instalado y ACTIVADO:
    python py/dql.py
"""

# `sys` da acceso a los argumentos de la línea de comandos (sys.argv) y a sys.exit.
import sys

# Funciones comunes de conexion.py (aquí no se necesita `ejecutar`: solo se lee).
from conexion import conexion, consultar, imprimir, principal

# Catálogo de consultas: nombre corto -> (título para mostrar, sentencia SQL).
CONSULTAS = {
    "01_estudiantes_todos": (
        "01. Todos los estudiantes",
        """SELECT * FROM ESTUDIANTE""",
    ),
    "02_nombre_email_estudiantes": (
        "02. Nombre y email de los estudiantes",
        """SELECT Nombre, email FROM ESTUDIANTE""",
    ),
    "03_estudiantes_activos": (
        "03. Estudiantes activos",
        """SELECT Nombre, Documento
           FROM ESTUDIANTE
           WHERE activo = TRUE""",
    ),
    "04_estudiantes_ordenados": (
        "04. Estudiantes ordenados por nombre",
        """SELECT Nombre, fecha_registro
           FROM ESTUDIANTE
           ORDER BY Nombre ASC""",
    ),
    "05_asignaturas_mas_de_3_creditos": (
        "05. Asignaturas con más de 3 créditos",
        """SELECT nombre, creditos
           FROM asignatura
           WHERE creditos > 3""",
    ),
    "06_estudiantes_nombre_con_l": (
        "06. Estudiantes cuyo nombre empieza por L",
        """SELECT Nombre
           FROM ESTUDIANTE
           WHERE Nombre LIKE 'L%'""",
    ),
    "07_matriculas_por_total": (
        "07. Matrículas con total entre 1000000 y 1500000",
        """SELECT matriculaID, estado, total
           FROM matricula
           WHERE total BETWEEN 1000000 AND 1500000""",
    ),
    "08_pagos_mas_altos": (
        "08. Los 3 pagos más altos",
        """SELECT pagoID, total, metodo_pago
           FROM pago
           ORDER BY total DESC
           LIMIT 3""",
    ),
    "09_total_estudiantes": (
        "09. Cantidad de estudiantes",
        """SELECT COUNT(*) AS total_estudiantes
           FROM ESTUDIANTE""",
    ),
    "10_total_pagado": (
        "10. Suma de todos los pagos",
        """SELECT SUM(total) AS total_pagado
           FROM pago""",
    ),
    "11_promedio_creditos": (
        "11. Promedio de créditos de las asignaturas",
        """SELECT AVG(creditos) AS promedio_creditos
           FROM asignatura""",
    ),
    "12_estudiantes_por_programa": (
        "12. Cantidad de estudiantes por programa",
        """SELECT programa_academicoID, COUNT(*) AS cantidad
           FROM ESTUDIANTE
           GROUP BY programa_academicoID""",
    ),
    "13_estudiantes_y_programa": (
        "13. Estudiantes con su programa",
        """SELECT ESTUDIANTE.Nombre, PROGRAMA_ACADEMICO.Nombre AS programa
           FROM ESTUDIANTE
           INNER JOIN PROGRAMA_ACADEMICO
               ON ESTUDIANTE.programa_academicoID = PROGRAMA_ACADEMICO.programa_academicoID""",
    ),
    "14_matriculas_y_estudiante": (
        "14. Matrículas con el nombre del estudiante",
        """SELECT matricula.matriculaID, ESTUDIANTE.Nombre, matricula.estado, matricula.total
           FROM matricula
           INNER JOIN ESTUDIANTE
               ON matricula.estudianteID = ESTUDIANTE.EstudianteID""",
    ),
    "15_pagos_y_estudiante": (
        "15. Pagos con el nombre del estudiante",
        """SELECT ESTUDIANTE.Nombre, pago.total, pago.metodo_pago, pago.estado_pago
           FROM pago
           INNER JOIN matricula
               ON pago.matriculaID = matricula.matriculaID
           INNER JOIN ESTUDIANTE
               ON matricula.estudianteID = ESTUDIANTE.EstudianteID""",
    ),
    "16_grupos_y_asignatura": (
        "16. Grupos con el nombre de su asignatura",
        """SELECT grupo.grupoID, asignatura.nombre, grupo.numero, grupo.cupo
           FROM grupo
           INNER JOIN asignatura
               ON grupo.asignaturaID = asignatura.asignaturaID""",
    ),
}


def main(argv):
    # Sin argumentos se ejecutan todas las consultas; con argumentos, solo las nombradas.
    nombres = argv or list(CONSULTAS)
    # Detecta nombres que no existan en el catálogo para fallar antes de conectar.
    desconocidas = [n for n in nombres if n not in CONSULTAS]
    if desconocidas:
        # sys.exit con un texto lo imprime en stderr y termina con código 1.
        sys.exit(f"Consulta desconocida: {', '.join(desconocidas)}. Opciones: {', '.join(CONSULTAS)}")
    # Una sola conexión a Sistema_academico para todas las consultas.
    with conexion(database="Sistema_academico") as con:
        for nombre in nombres:
            # Desempaqueta la pareja (título, SQL) y muestra el resultado como tabla.
            titulo, sql = CONSULTAS[nombre]
            imprimir(titulo, consultar(con, sql))


# Al lanzar el archivo, pasa a main() los argumentos (sin el nombre del script).
if __name__ == "__main__":
    principal(main, sys.argv[1:])
