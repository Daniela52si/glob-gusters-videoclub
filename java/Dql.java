// Conexión JDBC y excepción de errores SQL.
import java.sql.Connection;
import java.sql.SQLException;
// LinkedHashMap conserva el orden de inserción de las consultas.
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * DQL (Data Query Language) para la base de datos Sistema_academico.
 *
 * Consultas de solo lectura definidas en el script 03_DQL.sql de Sistema_academico.
 * Sin argumentos ejecuta todas; con un nombre ejecuta una sola:
 *     java -cp "out;lib/*" Dql 08_pagos_mas_altos
 *
 * Requisitos: JDK 17 o superior, el driver MariaDB y la base Sistema_academico creada.
 * Ejecución desde la carpeta java/:
 *     javac -encoding UTF-8 -d out *.java
 *     java -cp "out;lib/*" Dql
 */
public class Dql {

    // Una consulta: título para mostrar y sentencia SQL.
    record Consulta(String titulo, String sql) {}

    // Catálogo de consultas: nombre corto -> Consulta.
    static final Map<String, Consulta> CONSULTAS = new LinkedHashMap<>();

    // Bloque estático: se ejecuta una vez al cargar la clase y llena el catálogo.
    static {
        CONSULTAS.put("01_estudiantes_todos", new Consulta("01. Todos los estudiantes", """
                SELECT * FROM ESTUDIANTE"""));
        CONSULTAS.put("02_nombre_email_estudiantes", new Consulta("02. Nombre y email de los estudiantes", """
                SELECT Nombre, email FROM ESTUDIANTE"""));
        CONSULTAS.put("03_estudiantes_activos", new Consulta("03. Estudiantes activos", """
                SELECT Nombre, Documento
                FROM ESTUDIANTE
                WHERE activo = TRUE"""));
        CONSULTAS.put("04_estudiantes_ordenados", new Consulta("04. Estudiantes ordenados por nombre", """
                SELECT Nombre, fecha_registro
                FROM ESTUDIANTE
                ORDER BY Nombre ASC"""));
        CONSULTAS.put("05_asignaturas_mas_de_3_creditos", new Consulta("05. Asignaturas con más de 3 créditos", """
                SELECT nombre, creditos
                FROM asignatura
                WHERE creditos > 3"""));
        CONSULTAS.put("06_estudiantes_nombre_con_l", new Consulta("06. Estudiantes cuyo nombre empieza por L", """
                SELECT Nombre
                FROM ESTUDIANTE
                WHERE Nombre LIKE 'L%'"""));
        CONSULTAS.put("07_matriculas_por_total", new Consulta("07. Matrículas con total entre 1000000 y 1500000", """
                SELECT matriculaID, estado, total
                FROM matricula
                WHERE total BETWEEN 1000000 AND 1500000"""));
        CONSULTAS.put("08_pagos_mas_altos", new Consulta("08. Los 3 pagos más altos", """
                SELECT pagoID, total, metodo_pago
                FROM pago
                ORDER BY total DESC
                LIMIT 3"""));
        CONSULTAS.put("09_total_estudiantes", new Consulta("09. Cantidad de estudiantes", """
                SELECT COUNT(*) AS total_estudiantes
                FROM ESTUDIANTE"""));
        CONSULTAS.put("10_total_pagado", new Consulta("10. Suma de todos los pagos", """
                SELECT SUM(total) AS total_pagado
                FROM pago"""));
        CONSULTAS.put("11_promedio_creditos", new Consulta("11. Promedio de créditos de las asignaturas", """
                SELECT AVG(creditos) AS promedio_creditos
                FROM asignatura"""));
        CONSULTAS.put("12_estudiantes_por_programa", new Consulta("12. Cantidad de estudiantes por programa", """
                SELECT programa_academicoID, COUNT(*) AS cantidad
                FROM ESTUDIANTE
                GROUP BY programa_academicoID"""));
        CONSULTAS.put("13_estudiantes_y_programa", new Consulta("13. Estudiantes con su programa", """
                SELECT ESTUDIANTE.Nombre, PROGRAMA_ACADEMICO.Nombre AS programa
                FROM ESTUDIANTE
                INNER JOIN PROGRAMA_ACADEMICO
                    ON ESTUDIANTE.programa_academicoID = PROGRAMA_ACADEMICO.programa_academicoID"""));
        CONSULTAS.put("14_matriculas_y_estudiante", new Consulta("14. Matrículas con el nombre del estudiante", """
                SELECT matricula.matriculaID, ESTUDIANTE.Nombre, matricula.estado, matricula.total
                FROM matricula
                INNER JOIN ESTUDIANTE
                    ON matricula.estudianteID = ESTUDIANTE.EstudianteID"""));
        CONSULTAS.put("15_pagos_y_estudiante", new Consulta("15. Pagos con el nombre del estudiante", """
                SELECT ESTUDIANTE.Nombre, pago.total, pago.metodo_pago, pago.estado_pago
                FROM pago
                INNER JOIN matricula
                    ON pago.matriculaID = matricula.matriculaID
                INNER JOIN ESTUDIANTE
                    ON matricula.estudianteID = ESTUDIANTE.EstudianteID"""));
        CONSULTAS.put("16_grupos_y_asignatura", new Consulta("16. Grupos con el nombre de su asignatura", """
                SELECT grupo.grupoID, asignatura.nombre, grupo.numero, grupo.cupo
                FROM grupo
                INNER JOIN asignatura
                    ON grupo.asignaturaID = asignatura.asignaturaID"""));
    }

    public static void main(String[] args) throws SQLException {
        Conexion.configurarSalida();
        Conexion.correr(() -> principal(args));
    }

    /** Cuerpo del programa; main lo ejecuta con Conexion.correr() para explicar tablas dañadas. */
    private static void principal(String[] args) throws SQLException {
        // Sin argumentos se ejecutan todas las consultas; con argumentos, solo las nombradas.
        List<String> nombres = args.length == 0 ? List.copyOf(CONSULTAS.keySet()) : List.of(args);
        // Detecta nombres que no existan en el catálogo para fallar antes de conectar.
        List<String> desconocidas = nombres.stream().filter(n -> !CONSULTAS.containsKey(n)).toList();
        if (!desconocidas.isEmpty()) {
            // Mensaje de error con las opciones válidas y salida con código 1.
            System.err.println("Consulta desconocida: " + String.join(", ", desconocidas)
                    + ". Opciones: " + String.join(", ", CONSULTAS.keySet()));
            System.exit(1);
        }
        // Una sola conexión para todas las consultas.
        try (Connection con = Conexion.conectarA("Sistema_academico")) {
            for (String nombre : nombres) {
                // Recupera la consulta y muestra su resultado como tabla.
                Consulta c = CONSULTAS.get(nombre);
                Conexion.imprimir(c.titulo(), Conexion.consultar(con, c.sql()));
            }
        }
    }
}
