// Conexión JDBC y excepción de errores SQL.
import java.sql.Connection;
import java.sql.SQLException;
// LinkedHashMap conserva el orden de las vistas.
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * VDL (View Definition Language) — vistas de Sistema_academico.
 *
 * Crea y consulta las vistas definidas en 04_VDL.sql. La vista de prueba se crea,
 * consulta y elimina durante la ejecución normal; --drop elimina las vistas del script.
 *
 * Requisitos: JDK 17 o superior, el driver java/lib/mariadb-java-client-3.5.3.jar (se descarga
 * una sola vez; ver README.md), un servidor MariaDB 10.2.1+ en marcha y la base Sistema_academico
 * ya creada. Instalación y comandos para Windows, macOS y Linux: README.md, secciones
 * «Dependencias requeridas» y «Guía de ejecución por sistema operativo».
 * Compilación y ejecución, desde la carpeta java/:
 *     javac -encoding UTF-8 -d out *.java        (Windows PowerShell: (Get-ChildItem *.java).Name)
 *     java -cp "out:lib/*" Vdl          (Windows: java -cp "out;lib/*" Vdl)
 */
public class Vdl {

    /** Cada vista: sentencia de creación y consulta de verificación. */
    record Vista(String crear, String consulta) {}

    // Catálogo de vistas: nombre -> Vista.
    static final Map<String, Vista> VISTAS = new LinkedHashMap<>();

    // Bloque estático: se ejecuta una vez al cargar la clase y llena el catálogo.
    static {
        VISTAS.put("vista_estudiantes_activos", new Vista("""
                CREATE OR REPLACE VIEW vista_estudiantes_activos AS
                SELECT EstudianteID, Nombre, Documento, email
                FROM ESTUDIANTE
                WHERE activo = TRUE""",
                "SELECT * FROM vista_estudiantes_activos"));
        VISTAS.put("vista_estudiante_programa", new Vista("""
                CREATE OR REPLACE VIEW vista_estudiante_programa AS
                SELECT ESTUDIANTE.Nombre AS estudiante,
                       PROGRAMA_ACADEMICO.Nombre AS programa
                FROM ESTUDIANTE
                INNER JOIN PROGRAMA_ACADEMICO
                    ON ESTUDIANTE.programa_academicoID = PROGRAMA_ACADEMICO.programa_academicoID""",
                "SELECT * FROM vista_estudiante_programa"));
        VISTAS.put("vista_matriculas", new Vista("""
                CREATE OR REPLACE VIEW vista_matriculas AS
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
                "SELECT * FROM vista_matriculas"));
        VISTAS.put("vista_pagos", new Vista("""
                CREATE OR REPLACE VIEW vista_pagos AS
                SELECT ESTUDIANTE.Nombre AS estudiante,
                       pago.total,
                       pago.metodo_pago,
                       pago.estado_pago
                FROM pago
                INNER JOIN matricula
                    ON pago.matriculaID = matricula.matriculaID
                INNER JOIN ESTUDIANTE
                    ON matricula.estudianteID = ESTUDIANTE.EstudianteID""",
                "SELECT * FROM vista_pagos"));
        VISTAS.put("vista_grupos", new Vista("""
                CREATE OR REPLACE VIEW vista_grupos AS
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
                "SELECT * FROM vista_grupos"));
    }

    public static void main(String[] args) throws SQLException {
        Conexion.configurarSalida();
        Conexion.correr(() -> principal(args));
    }

    /** Cuerpo del programa; main lo ejecuta con Conexion.correr() para explicar tablas dañadas. */
    private static void principal(String[] args) throws SQLException {
        // Abre la conexión y la cierra automáticamente al terminar.
        try (Connection con = Conexion.conectar()) {
            // Con la opción --drop solo se eliminan las vistas y se termina.
            if (List.of(args).contains("--drop")) {
                for (String nombre : VISTAS.keySet()) {
                    Conexion.ejecutar(con, "DROP VIEW IF EXISTS `" + nombre + "`");
                    System.out.println("Vista eliminada: " + nombre);
                }
                Conexion.ejecutar(con, "DROP VIEW IF EXISTS `vista_prueba`");
                System.out.println("Vista eliminada: vista_prueba");
                con.commit();
                return;
            }
            // Crea (o reemplaza) cada vista y muestra su contenido.
            for (Map.Entry<String, Vista> vista : VISTAS.entrySet()) {
                Conexion.ejecutar(con, vista.getValue().crear());
                Conexion.imprimir(vista.getKey(), Conexion.consultar(con, vista.getValue().consulta()));
            }
            // Consulta adicional de pagos pendientes.
            Conexion.imprimir("vista_pagos (estado_pago = 'Pendiente')",
                    Conexion.consultar(con, "SELECT * FROM vista_pagos WHERE estado_pago = 'Pendiente'"));

            // Crea, consulta y elimina la vista de prueba definida en 04_VDL.sql.
            Conexion.ejecutar(con, """
                    CREATE VIEW vista_prueba AS
                    SELECT Nombre FROM ESTUDIANTE""");
            Conexion.imprimir("vista_prueba", Conexion.consultar(con, "SELECT * FROM vista_prueba"));
            Conexion.ejecutar(con, "DROP VIEW vista_prueba");
            con.commit();
        }
    }
}
