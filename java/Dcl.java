// Conexión JDBC y excepción de errores SQL.
import java.sql.Connection;
import java.sql.SQLException;
// LinkedHashMap conserva el orden de las cuentas.
import java.util.LinkedHashMap;
import java.util.Map;

/**
 * DCL (Data Control Language) para la base de datos Sistema_academico.
 *
 * Crea las cuentas de estudiante, profesor y administrador, concede sus permisos,
 * revoca UPDATE al profesor y elimina al administrador al final. Las claves se leen
 * de las variables de entorno SISTEMA_ACADEMICO_PASS_ESTUDIANTE,
 * SISTEMA_ACADEMICO_PASS_PROFESOR y SISTEMA_ACADEMICO_PASS_ADMIN; no se imprimen.
 *
 * Requisitos: JDK 17 o superior, el driver MariaDB y un servidor MariaDB en marcha,
 * con Sistema_academico ya creada. Compilación y ejecución, desde la carpeta java/:
 *     javac -encoding UTF-8 -d out *.java        (Windows PowerShell: (Get-ChildItem *.java).Name)
 *     java -cp "out:lib/*" Dcl          (Windows: java -cp "out;lib/*" Dcl)
 */
public class Dcl {

    // Base de datos sobre la que se conceden los permisos.
    static final String BD = "Sistema_academico";

    /** Cuenta y privilegios que se conceden. */
    record Cuenta(String clave, String privilegios) {}

    // Cuentas del script: nombre de usuario -> datos de la cuenta.
    static final Map<String, Cuenta> USUARIOS = new LinkedHashMap<>();

    static {
        USUARIOS.put("estudiante_user",
                new Cuenta(Conexion.env("SISTEMA_ACADEMICO_PASS_ESTUDIANTE", null), "SELECT"));
        USUARIOS.put("profesor_user",
                new Cuenta(Conexion.env("SISTEMA_ACADEMICO_PASS_PROFESOR", null), "SELECT, INSERT, UPDATE"));
        USUARIOS.put("admin_user",
                new Cuenta(Conexion.env("SISTEMA_ACADEMICO_PASS_ADMIN", null), "ALL PRIVILEGES"));
    }

    public static void main(String[] args) throws SQLException {
        Conexion.configurarSalida();
        Conexion.correr(() -> principal());
    }

    /** Ejecuta las operaciones DCL en el orden del script resuelto. */
    private static void principal() throws SQLException {
        validarClaves();
        try (Connection con = Conexion.conectarA(BD)) {
            for (Map.Entry<String, Cuenta> usuario : USUARIOS.entrySet()) {
                String cuenta = "'" + usuario.getKey() + "'@'localhost'";
                Cuenta datos = usuario.getValue();
                Conexion.ejecutar(con,
                        "CREATE USER IF NOT EXISTS " + cuenta + " IDENTIFIED BY ?", datos.clave());
                Conexion.ejecutar(con,
                        "GRANT " + datos.privilegios() + " ON `" + BD + "`.* TO " + cuenta);
                System.out.println("Usuario " + cuenta + ": GRANT " + datos.privilegios());
            }

            Conexion.ejecutar(con,
                    "GRANT SELECT ON `" + BD + "`.pago TO 'estudiante_user'@'localhost'");

            mostrarGrants(con, "estudiante_user");
            mostrarGrants(con, "profesor_user");
            mostrarGrants(con, "admin_user");

            Conexion.ejecutar(con,
                    "REVOKE UPDATE ON `" + BD + "`.* FROM 'profesor_user'@'localhost'");
            mostrarGrants(con, "profesor_user");

            Conexion.ejecutar(con, "DROP USER 'admin_user'@'localhost'");
        }
    }

    /** Rechaza claves ausentes antes de crear o modificar cuentas. */
    private static void validarClaves() {
        for (Map.Entry<String, Cuenta> usuario : USUARIOS.entrySet()) {
            if (usuario.getValue().clave() == null || usuario.getValue().clave().isBlank()) {
                String variable = switch (usuario.getKey()) {
                    case "estudiante_user" -> "SISTEMA_ACADEMICO_PASS_ESTUDIANTE";
                    case "profesor_user" -> "SISTEMA_ACADEMICO_PASS_PROFESOR";
                    default -> "SISTEMA_ACADEMICO_PASS_ADMIN";
                };
                throw new IllegalStateException("Define la variable de entorno " + variable + ".");
            }
        }
    }

    private static void mostrarGrants(Connection con, String usuario) throws SQLException {
        System.out.println("\n== Privilegios de " + usuario + " ==");
        for (Map<String, Object> fila : Conexion.consultar(con,
                "SHOW GRANTS FOR '" + usuario + "'@'localhost'")) {
            System.out.println(fila.values().iterator().next());
        }
    }
}
