"""DDL (Data Definition Language) para la base de datos Sistema_academico.

Selecciona Sistema_academico, crea FACULTAD y DOCENTE, y agrega columnas a
ESTUDIANTE, grupo, horario y asignatura.

Requisitos: Python 3.9+, el paquete PyMySQL (`pip install -r requirements.txt` dentro del
entorno virtual .venv), un servidor MariaDB 10.2.1+ en marcha y la base Sistema_academico ya
creada. Instalación y comandos para Windows, macOS y Linux: README.md, secciones
«Dependencias requeridas» y «Guía de ejecución por sistema operativo».
Ejecución, con el entorno virtual instalado y ACTIVADO y desde la raíz del proyecto:
    python3 py/ddl.py          (macOS y Linux; en Windows: python py/ddl.py)
"""

# Funciones comunes de conexion.py: context manager de conexión, SELECT, escritura e impresión.
from conexion import conexion, consultar, ejecutar, imprimir, principal

# Lista ordenada de sentencias DDL para Sistema_academico.
SENTENCIAS = [
    # Crea la tabla de facultades.
    """CREATE TABLE FACULTAD (
        facultad_id INT PRIMARY KEY,
        nombre_facultad VARCHAR(150) NOT NULL UNIQUE,
        ubicacion VARCHAR(100),
        presupuesto DECIMAL(12,2) NOT NULL,
        CONSTRAINT chk_presupuesto CHECK (presupuesto >= 0)
    )""",
    # Crea la tabla de docentes y su relación con FACULTAD.
    """CREATE TABLE DOCENTE (
        docente_id INT PRIMARY KEY,
        nombres VARCHAR(100) NOT NULL,
        apellidos VARCHAR(100) NOT NULL,
        identificacion VARCHAR(30) NOT NULL UNIQUE,
        correo_institucional VARCHAR(150) NOT NULL UNIQUE,
        especialidad VARCHAR(100),
        fecha_contratacion DATE NOT NULL,
        salario DECIMAL(10,2) NOT NULL,
        facultad_id INT NOT NULL,
        CONSTRAINT chk_salario CHECK (salario >= 0),
        CONSTRAINT fk_docente_facultad
            FOREIGN KEY (facultad_id) REFERENCES FACULTAD (facultad_id)
    )""",
    # Agrega los datos personales complementarios de ESTUDIANTE.
    """ALTER TABLE ESTUDIANTE
        ADD fecha_nacimiento DATE NULL,
        ADD ciudad_residencia VARCHAR(100) NULL""",
    # Relaciona los grupos con sus docentes.
    """ALTER TABLE grupo
        ADD docente_id INT NULL,
        ADD CONSTRAINT fk_grupo_docente
            FOREIGN KEY (docente_id) REFERENCES DOCENTE (docente_id)""",
    # Agrega información descriptiva a horario y asignatura.
    "ALTER TABLE horario ADD tipo_aula VARCHAR(50)",
    "ALTER TABLE asignatura ADD descripcion VARCHAR(500)",
]


def main():
    # Abre la conexión, selecciona la base de destino y la cierra al salir.
    with conexion() as con:
        con.select_db("Sistema_academico")
        # Ejecuta cada sentencia DDL en el orden de la lista.
        for sql in SENTENCIAS:
            ejecutar(con, sql)
            # Muestra un resumen: espacios múltiples colapsados y máximo 90 caracteres.
            print("OK:", " ".join(sql.split())[:90])
        # Confirma los cambios (en MariaDB el DDL ya confirma implícitamente).
        con.commit()

        # Verifica las tablas creadas y las columnas agregadas en information_schema.
        imprimir(
            "Estructura de Sistema_academico",
            consultar(
                con,
                """SELECT table_name AS tabla, column_name AS columna, column_type AS tipo
                   FROM information_schema.columns
                   WHERE table_schema = DATABASE()
                     AND (table_name IN ('FACULTAD', 'DOCENTE')
                          OR (table_name, column_name) IN
                             (('ESTUDIANTE', 'fecha_nacimiento'),
                              ('ESTUDIANTE', 'ciudad_residencia'),
                              ('grupo', 'docente_id'),
                              ('horario', 'tipo_aula'),
                              ('asignatura', 'descripcion')))
                   ORDER BY table_name, column_name""",
            ),
        )


# Ejecuta main() solo cuando el archivo se lanza directamente (python3 py/ddl.py).
if __name__ == "__main__":
    principal(main)
