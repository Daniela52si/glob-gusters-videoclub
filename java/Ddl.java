// Conexión JDBC y excepción de errores SQL.
import java.sql.Connection;
import java.sql.SQLException;
// Lista inmutable para las sentencias.
import java.util.List;

/**
 * DDL (Data Definition Language) — estructura de la base de datos Sistema_academico.
 *
 * Selecciona Sistema_academico, crea FACULTAD y DOCENTE, y agrega columnas a
 * ESTUDIANTE, grupo, horario y asignatura.
 *
 * Requisitos: JDK 17 o superior, el driver java/lib/mariadb-java-client-3.5.3.jar (se descarga
 * una sola vez; ver README.md), un servidor MariaDB 10.2.1+ en marcha y la base
 * Sistema_academico ya creada. Instalación y comandos para Windows, macOS y Linux: README.md, secciones
 * «Dependencias requeridas» y «Guía de ejecución por sistema operativo».
 * Compilación y ejecución, desde la carpeta java/:
 *     javac -encoding UTF-8 -d out *.java        (Windows PowerShell: (Get-ChildItem *.java).Name)
 *     java -cp "out:lib/*" Ddl          (Windows: java -cp "out;lib/*" Ddl)
 */
public class Ddl {

    // Sentencias DDL de Sistema_academico en el orden en que se ejecutan.
    static final List<String> SENTENCIAS = List.of(
            // Crea la tabla de facultades.
            """
            CREATE TABLE FACULTAD (
                facultad_id INT PRIMARY KEY,
                nombre_facultad VARCHAR(150) NOT NULL UNIQUE,
                ubicacion VARCHAR(100),
                presupuesto DECIMAL(12,2) NOT NULL,
                CONSTRAINT chk_presupuesto CHECK (presupuesto >= 0)
            )""",
            // Crea la tabla de docentes y su relación con FACULTAD.
            """
            CREATE TABLE DOCENTE (
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
            // Agrega los datos personales complementarios de ESTUDIANTE.
            """
            ALTER TABLE ESTUDIANTE
                ADD fecha_nacimiento DATE NULL,
                ADD ciudad_residencia VARCHAR(100) NULL""",
            // Relaciona los grupos con sus docentes.
            """
            ALTER TABLE grupo
                ADD docente_id INT NULL,
                ADD CONSTRAINT fk_grupo_docente
                    FOREIGN KEY (docente_id) REFERENCES DOCENTE (docente_id)""",
            // Agrega información descriptiva a horario y asignatura.
            "ALTER TABLE horario ADD tipo_aula VARCHAR(50)",
            "ALTER TABLE asignatura ADD descripcion VARCHAR(500)");

    public static void main(String[] args) throws SQLException {
        Conexion.configurarSalida();
        Conexion.correr(() -> principal(args));
    }

    /** Cuerpo del programa; main lo ejecuta con Conexion.correr() para explicar tablas dañadas. */
    private static void principal(String[] args) throws SQLException {
        // Abre la conexión, selecciona la base de destino y la cierra al terminar.
        try (Connection con = Conexion.conectar()) {
            con.setCatalog("Sistema_academico");
            // Ejecuta cada sentencia DDL en orden.
            for (String sql : SENTENCIAS) {
                Conexion.ejecutar(con, sql);
                // Resumen: espacios múltiples colapsados en uno solo y máximo 90 caracteres.
                String resumen = sql.trim().replaceAll("\\s+", " ");
                System.out.println("OK: " + resumen.substring(0, Math.min(90, resumen.length())));
            }
            // Confirma los cambios (en MariaDB el DDL ya confirma implícitamente).
            con.commit();

            // Verifica las tablas creadas y las columnas agregadas en information_schema.
            Conexion.imprimir("Estructura de Sistema_academico", Conexion.consultar(con, """
                    SELECT table_name AS tabla, column_name AS columna, column_type AS tipo
                    FROM information_schema.columns
                    WHERE table_schema = DATABASE()
                      AND (table_name IN ('FACULTAD', 'DOCENTE')
                           OR (table_name, column_name) IN
                              (('ESTUDIANTE', 'fecha_nacimiento'),
                               ('ESTUDIANTE', 'ciudad_residencia'),
                               ('grupo', 'docente_id'),
                               ('horario', 'tipo_aula'),
                               ('asignatura', 'descripcion')))
                    ORDER BY table_name, column_name"""));
        }
    }
}
