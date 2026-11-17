// Control de transacciones para la base de datos Sistema_academico.
import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Savepoint;
import java.util.List;
import java.util.Map;

/**
 * TCL (Transaction Control Language) para la base de datos Sistema_academico.
 *
 * Demuestra COMMIT, ROLLBACK y SAVEPOINT con pagos, matrículas y estudiantes.
 * Requiere haber ejecutado antes 01_DDL.sql y 02_DML.sql.
 *
 * Requisitos: JDK 17 o superior, el driver MariaDB configurado para este proyecto y un
 * servidor MariaDB en marcha con Sistema_academico creada.
 * Compilación y ejecución, desde la carpeta java/:
 *     javac -encoding UTF-8 -d out *.java
 *     java -cp "out;lib/*" Tcl
 */
public class Tcl {

    public static void main(String[] args) throws SQLException {
        Conexion.configurarSalida();
        Conexion.correr(() -> principal(args));
    }

    /** Cuerpo del programa; main lo ejecuta con Conexion.correr() para explicar tablas dañadas. */
    private static void principal(String[] args) throws SQLException {
        try (Connection con = Conexion.conectarA("Sistema_academico")) {
            // --- 1. COMMIT: confirmar el pago y activar la matrícula ------------------
            try {
                int n = Conexion.ejecutar(con,
                        "UPDATE pago SET estado_pago = ? WHERE pagoID = ?", "Pagado", 4);
                System.out.println("UPDATE pago: " + n + " fila(s)");

                n = Conexion.ejecutar(con,
                        "UPDATE matricula SET estado = ? WHERE matriculaID = ?", "Activa", 4);
                System.out.println("UPDATE matricula: " + n + " fila(s)");

                con.commit();
            } catch (SQLException error) {
                con.rollback();
                throw error;
            }
            Conexion.imprimir("Pago confirmado",
                    Conexion.consultar(con, "SELECT pagoID, estado_pago FROM pago WHERE pagoID = ?", 4));

            // --- 2. ROLLBACK: cancelar temporalmente un pago y deshacer el cambio -----
            try {
                Conexion.ejecutar(con,
                        "UPDATE pago SET estado_pago = ? WHERE pagoID = ?", "Cancelado", 1);
                Conexion.imprimir("Pago dentro de la transacción",
                        Conexion.consultar(con, "SELECT pagoID, estado_pago FROM pago WHERE pagoID = ?", 1));
            } catch (SQLException error) {
                con.rollback();
                throw error;
            }

            con.rollback();
            Conexion.imprimir("Pago después del ROLLBACK",
                    Conexion.consultar(con, "SELECT pagoID, estado_pago FROM pago WHERE pagoID = ?", 1));

            // --- 3. SAVEPOINT: mantener el teléfono y deshacer solo la desactivación --
            try {
                Conexion.ejecutar(con,
                        "UPDATE ESTUDIANTE SET Telefono = ? WHERE EstudianteID = ?", "3000000001", 2);
                Savepoint cambioTelefono = con.setSavepoint("cambio_telefono");

                Conexion.ejecutar(con,
                        "UPDATE ESTUDIANTE SET activo = ? WHERE EstudianteID = ?", false, 2);
                con.rollback(cambioTelefono);
                con.commit();
            } catch (SQLException error) {
                con.rollback();
                throw error;
            }

            List<Map<String, Object>> estudiante = Conexion.consultar(con, """
                    SELECT EstudianteID, Nombre, Telefono, activo
                    FROM ESTUDIANTE
                    WHERE EstudianteID = ?""", 2);
            Conexion.imprimir("Estudiante tras ROLLBACK TO SAVEPOINT y COMMIT", estudiante);
        }
    }
}
