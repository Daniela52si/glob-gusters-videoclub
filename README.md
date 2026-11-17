# `Sistema_academico` · Base de Datos Relacional

Proyecto de base de datos relacional para la base de datos `Sistema_academico`,
desarrollado como material de apoyo para la asignatura de Base de Datos (Ingeniería de
Sistemas). La base de datos gestiona información de **programas académicos, estudiantes,
periodos, asignaturas, grupos, horarios, matrículas, pagos, facultades y docentes**,
facilitando la administración académica y financiera de una institución educativa.

Motor de base de datos: **MariaDB** sobre entorno **XAMPP**.

<!-- indice:inicio -->
## Índice

- [Descripción del ejercicio](#descripción-del-ejercicio)
  - [Modelo normalizado (Tercera Forma Normal — 3FN)](#modelo-normalizado-tercera-forma-normal--3fn)
  - [Estructura de las tablas](#estructura-de-las-tablas)
  - [Reglas de negocio e integridad](#reglas-de-negocio-e-integridad)
  - [Vistas y usuarios de ejemplo](#vistas-y-usuarios-de-ejemplo)
  - [Datos de prueba](#datos-de-prueba)
- [Especificaciones del proyecto](#especificaciones-del-proyecto)
- [Contenido del repositorio](#contenido-del-repositorio)
- [Requisitos previos](#requisitos-previos)
- [Dependencias requeridas](#dependencias-requeridas)
  - [Instalación de las dependencias, por sistema operativo](#instalación-de-las-dependencias-por-sistema-operativo)
- [Guía de ejecución por sistema operativo](#guía-de-ejecución-por-sistema-operativo)
  - [1. Archivos SQL (MariaDB)](#1-archivos-sql-mariadb)
  - [2. Diagnóstico del servidor (`check-mariadb`)](#2-diagnóstico-del-servidor-check-mariadb)
  - [3. Python](#3-python)
  - [4. Java](#4-java)
  - [5. Windows CMD (Símbolo del sistema)](#5-windows-cmd-símbolo-del-sistema)
    - [5.1 Archivos SQL](#51-archivos-sql)
    - [5.2 Diagnóstico del servidor](#52-diagnóstico-del-servidor)
    - [5.3 Python](#53-python)
    - [5.4 Java](#54-java)
    - [5.5 Si las tildes o la `ñ` se ven mal en la consola](#55-si-las-tildes-o-la-ñ-se-ven-mal-en-la-consola)
  - [Probar la creación desde cero sin tocar tu base](#probar-la-creación-desde-cero-sin-tocar-tu-base)
  - [Tildes y `ñ` en la terminal](#tildes-y-ñ-en-la-terminal)
  - [Errores frecuentes](#errores-frecuentes)
- [Scripts de shell (`shell/`)](#scripts-de-shell-shell)
  - [Antes de empezar](#antes-de-empezar)
  - [Linux y macOS (Bash)](#linux-y-macos-bash)
  - [Windows (PowerShell)](#windows-powershell)
  - [Windows (CMD)](#windows-cmd)
  - [Qué hacen y qué no](#qué-hacen-y-qué-no)
- [Ejecución paso a paso en XAMPP MariaDB](#ejecución-paso-a-paso-en-xampp-mariadb)
  - [1. Iniciar los servicios](#1-iniciar-los-servicios)
  - [2. Verificar que el cliente `mariadb` es accesible](#2-verificar-que-el-cliente-mariadb-es-accesible)
  - [3. Ejecutar los scripts en orden](#3-ejecutar-los-scripts-en-orden)
    - [Ejecución segura: se puede repetir y desordenar sin miedo](#ejecución-segura-se-puede-repetir-y-desordenar-sin-miedo)
  - [4. Verificar la instalación desde phpMyAdmin (opcional)](#4-verificar-la-instalación-desde-phpmyadmin-opcional)
- [Configuración de la conexión (`.env`)](#configuración-de-la-conexión-env)
- [Conexión y consultas desde Python](#conexión-y-consultas-desde-python)
- [Conexión y consultas desde Java](#conexión-y-consultas-desde-java)
- [Documentación detallada de cada archivo](#documentación-detallada-de-cada-archivo)
  - [Archivos de la raíz](#archivos-de-la-raíz)
    - [`.env.example` — plantilla de configuración](#envexample--plantilla-de-configuración)
    - [`.env` — configuración real y local](#env--configuración-real-y-local)
    - [`.gitignore` — archivos que Git no versiona](#gitignore--archivos-que-git-no-versiona)
    - [`requirements.txt` — dependencias de Python](#requirementstxt--dependencias-de-python)
    - [`LICENSE`](#license)
    - [`README.md`](#readmemd)
  - [Carpeta `docs/`](#carpeta-docs)
  - [Carpeta `sql/mariadb/`](#carpeta-sqlmariadb)
    - [`glob_gusters.sql` — esquema completo (DDL)](#glob_gusterssql--esquema-completo-ddl)
    - [`glob_gusters_insert.sql` — datos de prueba (DML)](#glob_gusters_insertsql--datos-de-prueba-dml)
    - [`check-mariadb.sql` — diagnóstico del servidor (solo lectura)](#check-mariadbsql--diagnóstico-del-servidor-solo-lectura)
    - [`check-mariadb.sh` — lanzador con la configuración del `.env`](#check-mariadbsh--lanzador-con-la-configuración-del-env)
    - [`commands/01_DDL.sql` a `06_TCL.sql` — ejemplos por grupo de comandos SQL](#commands01_ddlsql-a-06_tclsql--ejemplos-por-grupo-de-comandos-sql)
  - [Carpeta `py/`](#carpeta-py)
    - [`conexion.py` — módulo base](#conexionpy--módulo-base)
    - [`conexion_mariabd.py`](#conexion_mariabdpy)
    - [`ddl.py`, `dml.py`, `dql.py`, `vdl.py`, `dcl.py`, `tcl.py`](#ddlpy-dmlpy-dqlpy-vdlpy-dclpy-tclpy)
  - [Carpeta `java/`](#carpeta-java)
    - [`Conexion.java` — clase base](#conexionjava--clase-base)
    - [`Ddl.java`, `Dml.java`, `Dql.java`, `Vdl.java`, `Dcl.java`, `Tcl.java`](#ddljava-dmljava-dqljava-vdljava-dcljava-tcljava)
  - [Flujo completo de ejecución y dependencias entre archivos](#flujo-completo-de-ejecución-y-dependencias-entre-archivos)
- [Cómo subir este proyecto a GitHub](#cómo-subir-este-proyecto-a-github)
- [Protección de la rama `main`](#protección-de-la-rama-main)
- [Licencia](#licencia)
<!-- indice:fin -->

## Descripción del ejercicio

El sistema académico necesita una base de datos para gestionar la operación de la
institución y la información relacionada con su oferta educativa. La base maneja la
siguiente información:

- Cada **programa académico** tiene nombre, fechas de inicio y fin, descripción y su
  relación con los periodos académicos.
- Los **estudiantes** se registran con su información personal, programa académico,
  contacto y estado activo.
- Los **periodos académicos** agrupan asignaturas, grupos y matrículas para cada
  programa.
- Cada **asignatura** se define por nombre y créditos, y puede estar asociada a varios
  grupos y periodos.
- Los **grupos** contienen la asignatura, el número del grupo y su cupo disponible.
- Los **horarios** indican día, hora de inicio y fin, y el aula asignada para cada
  grupo.
- Las **matrículas** registran la inscripción de un estudiante en un periodo académico,
  su fecha, estado y valor total.
- Los **pagos** registran el valor pagado, la fecha, el método y el estado del pago
  asociado a una matrícula.
- Las **facultades** organizan académicamente los programas y las áreas de formación.
- Los **docentes** participan en la oferta académica y se relacionan con los grupos y
  asignaturas según la estructura del plan de estudios.

### Modelo normalizado (Tercera Forma Normal — 3FN)

Para llegar a 3FN se separaron las entidades principales del modelo y se resolvieron las
relaciones muchos a muchos con tablas de unión. En `Sistema_academico`, la información se
organiza alrededor de programas, estudiantes, periodos académicos, asignaturas, grupos,
horarios, matrículas y pagos, evitando duplicar datos en varias tablas.

| Tabla | Llave primaria | Descripción |
|---|---|---|
| `PROGRAMA_ACADEMICO` | `programa_academicoID` | Programa académico que agrupa periodos, estudiantes y asignaturas. |
| `ESTUDIANTE` | `EstudianteID` | Datos personales del estudiante y su programa asociado. |
| `PERIODO_ACADEMICO` | `periodo_academicoID` | Periodo lectivo definido para un programa. |
| `asignatura` | `asignaturaID` | Catálogo de asignaturas con su número de créditos. |
| `PERIODO_ACADEMICO_ASIGNATURA` | (`periodo_academicoID`, `asignaturaID`) | Relación N:M entre periodos y asignaturas. |
| `grupo` | `grupoID` | Grupo académico asociado a una asignatura. |
| `horario` | `horarioID` | Horario semanal de un grupo con día, horas y aula. |
| `matricula` | `matriculaID` | Registro de la matrícula de un estudiante en un periodo. |
| `matricula_grupo` | (`matriculaID`, `grupoID`) | Relación N:M entre matrículas y grupos. |
| `pago` | `pagoID` | Registro del pago asociado a una matrícula. |

En el esquema real de `glob_gusters 1.sql` se utilizan tanto llaves primarias simples como
llaves compuestas para representar las relaciones del negocio. La conexión entre tablas se
documenta mediante restricciones `FOREIGN KEY` y validaciones con `CHECK`.

### Estructura de las tablas

PK = llave primaria, FK = llave foránea, UQ = restricción `UNIQUE`.

| Tabla | Columnas | Restricciones |
|---|---|---|
| `PROGRAMA_ACADEMICO` | `programa_academicoID`, `Nombre`, `fecha_inicio`, `fecha_final`, `Descripcion` | PK; `CHECK (fecha_final >= fecha_inicio)`. |
| `ESTUDIANTE` | `EstudianteID`, `Nombre`, `Documento`, `programa_academicoID`, `Telefono`, `email`, `fecha_registro`, `activo` | PK; UQ `Documento`, UQ `email`; FK → `PROGRAMA_ACADEMICO`. |
| `PERIODO_ACADEMICO` | `periodo_academicoID`, `nombre`, `fecha_registro`, `programa_academicoID` | PK; FK → `PROGRAMA_ACADEMICO`. |
| `asignatura` | `asignaturaID`, `nombre`, `creditos` | PK; `CHECK (creditos > 0)`. |
| `PERIODO_ACADEMICO_ASIGNATURA` | `periodo_academicoID`, `asignaturaID` | PK compuesta; FK → `PERIODO_ACADEMICO`, `asignatura`. |
| `grupo` | `grupoID`, `asignaturaID`, `numero`, `cupo` | PK; UQ (`asignaturaID`, `numero`); FK → `asignatura`; `CHECK (cupo > 0)`. |
| `horario` | `horarioID`, `grupoID`, `dia`, `hora_inicio`, `hora_fin`, `aula` | PK; FK → `grupo`; `CHECK (hora_fin > hora_inicio)`. |
| `matricula` | `matriculaID`, `periodo_academicoID`, `estudianteID`, `fecha`, `estado`, `total` | PK; UQ (`estudianteID`, `periodo_academicoID`); FK → `PERIODO_ACADEMICO`, `ESTUDIANTE`; `CHECK (total >= 0)`. |
| `matricula_grupo` | `matriculaID`, `grupoID` | PK compuesta; FK → `matricula`, `grupo`. |
| `pago` | `pagoID`, `total`, `fecha_pago`, `metodo_pago`, `matriculaID`, `estado_pago` | PK; FK → `matricula`; `CHECK (total >= 0)`. |

El script `01_DDL.sql` del proyecto mantiene la misma lógica de definición de esquema: crea
las tablas, agrega columnas con `ALTER TABLE` cuando hace falta y usa restricciones de
integridad para garantizar consistencia en los datos del sistema.

### Reglas de negocio e integridad

Los scripts del proyecto muestran cómo se expresan las reglas de negocio con DDL,
validaciones y operaciones de mantenimiento sobre los datos:

| Regla o práctica | Cómo se aplica en el proyecto |
|---|---|
| `CREATE TABLE` con estructura base y ampliaciones. | En `01_DDL.sql` se crea `tabla_prueba` para demostrar DDL y luego se elimina; además se agrega `Email` a `cliente`, se completa `Duracion_Minutos` en `pelicula` y se modifica `Telefono` a `VARCHAR(25)`. |
| Integridad por restricciones. | El proyecto usa `CHECK` para validar rangos (`fecha_final >= fecha_inicio`, `creditos > 0`, `cupo > 0`, `hora_fin > hora_inicio`, `total >= 0`), además de `UNIQUE` para evitar duplicados de documentos, correos, grupos por asignatura, etc. |
| Seguridad de datos y reejecución. | Los scripts cargan `IF NOT EXISTS` o `CREATE OR REPLACE VIEW`, y usan `IGNORE` o `DELETE ... WHERE` por llave natural para que puedan ejecutarse más de una vez sin romper la base. |
| Actualización de datos con criterio de negocio. | En `02_DML.sql` se inserta un nuevo cliente con aval válido, se cambia el estado de una copia a `Dañado` y se corrige la duración de `Interstellar`. |
| Eliminación controlada. | El script de DML elimina el reparto de Anne Hathaway en `Interstellar` usando la clave natural (`Titulo` + `Anio` + `Nombre`). Esto deja claro que las operaciones de borrado deben apuntar a la fila exacta y no depender de IDs fijos. |
| Idempotencia en prueba y operación. | Los datos de la práctica están pensados para volver a ejecutarse: si un registro ya existe, `INSERT IGNORE` evita duplicados; si el valor ya estaba actualizado, el `UPDATE` no cambia nada y el `DELETE` no falla si la fila ya no existe. |

El proyecto combina restricciones declarativas (`CHECK`, `UNIQUE`, `FOREIGN KEY`) con
operaciones de manipulación de datos para mantener la integridad del esquema y la
consistencia del sistema durante el desarrollo y la operación.

### Vistas y usuarios de ejemplo

Los ejemplos de vista y permisos se encuentran en `04_VDL.sql` y `05_DCL.sql`:

| Objeto | Descripción |
|---|---|
| `v_ejemplares_detalle` | Vista que unifica `ejemplar`, `pelicula` y `estado` para consultar el número del ejemplar, la película y el estado de conservación. |
| `v_clientes_con_aval` | Vista que muestra cada cliente y el nombre del aval que lo respalda, usando `LEFT JOIN` para conservar a los clientes sin aval. |
| `glob_gusters_reportes`@`localhost` | Usuario de sólo lectura con permiso `SELECT` sobre todas las tablas y vistas del esquema `glob_gusters`. |
| `glob_gusters_mostrador`@`localhost` | Usuario con permisos `SELECT`, `INSERT` y `UPDATE` sobre el esquema, pero sin `DELETE` para proteger el historial de rentas. |

La gestión de permisos se realiza con `CREATE USER IF NOT EXISTS`, `GRANT`, `REVOKE DELETE`
y `FLUSH PRIVILEGES`, dejando listas credenciales y permisos para usuarios específicos.

### Datos de prueba

El proyecto incluye dos tipos de datos de prueba:

1. Datos base del ejercicio (`glob_gusters_insert.sql`), que cargan información inicial en las tablas del modelo.
2. Cambios adicionales de validación en `02_DML.sql`, usados para demostrar `INSERT`, `UPDATE` y `DELETE` con criterio práctico.

| Caso de prueba | Script | Resultado esperado |
|---|---|---|
| Inserción de nuevo cliente con aval. | `02_DML.sql` | Se crea un socio nuevo en `cliente` con `Dni` único y `Email` válido. |
| Cambio de estado de ejemplar. | `02_DML.sql` | Un ejemplar de `Quo Vadis` pasa a estado `Dañado`. |
| Actualización de duración de película. | `02_DML.sql` | `Interstellar` queda con `Duracion_Minutos = 169`. |
| Eliminación de reparto incorrecto. | `02_DML.sql` | Se borra la fila de Anne Hathaway en `Interstellar` sin afectar el resto del catálogo. |
| Creación de vistas. | `04_VDL.sql` | Se generan `v_ejemplares_detalle` y `v_clientes_con_aval`. |
| Creación de usuarios y permisos. | `05_DCL.sql` | Se crean los usuarios de reportes y mostrador con sus permisos correspondientes. |

Estos ejemplos permiten comprobar que la base de datos responde bien a la carga inicial,
a la manipulación de datos y a la gestión de acceso por roles.

## Especificaciones del proyecto

| Aspecto | Detalle |
|---|---|
| Motor principal | MariaDB (XAMPP). Verificado con MariaDB 10.4.28. |
| Base de datos | `glob_gusters`, con juego de caracteres `utf8mb4` y collation `utf8mb4_general_ci`. |
| Motor de almacenamiento | InnoDB (necesario para llaves foráneas y transacciones). |
| Puerto de conexión | **3306** (en las variables de entorno `GLOB_GUSTERS_PORT` se puede cambiar). |
| Usuario por defecto | `root` sin contraseña (valor de XAMPP; ajústalo si tu servidor la exige). |
| Objetos | 11 tablas, 2 vistas, 4 triggers, 2 usuarios de ejemplo y 1 índice adicional. |
| Normalización | Tercera Forma Normal (3FN). |
| Lenguajes de acceso | SQL, Python 3.9+ (PyMySQL / `mariadb`) y Java 17+ (JDBC). |

## Contenido del repositorio

```
glob-gusters-videoclub/
├── docs/
│   ├── MER.pdf / MER.png                # Modelo Entidad-Relación del proyecto
│   ├── glob_gusters_diccionario.pdf     # Diccionario de datos: tablas, columnas, tipos y llaves
│   ├── relational-database.pdf          # Taller resuelto: diseño E-R de Glob-Gusters
│   ├── sql_scripts_commands.pdf         # Resumen de los grupos de comandos SQL (DDL/DML/DQL/DCL/TCL/VDL)
│   └── steps-create-project-database.pdf# Orden de ejecución recomendado del proyecto
├── sql/
│   └── mariadb/
│       ├── glob_gusters.sql             # DDL: base de datos, tablas, constraints y triggers
│       ├── glob_gusters_insert.sql      # DML: datos de prueba para todas las tablas
│       ├── check-mariadb.sql            # Script de diagnóstico del servidor MariaDB
│       ├── check-mariadb.sh              # Lanzador: ejecuta el diagnóstico con la configuración del .env
│       ├── check-mariadb.ps1             # Lanzador equivalente para Windows PowerShell
│       ├── check-mariadb.cmd             # Lanzador equivalente para Windows CMD
│       └── commands/
│           ├── 01_DDL.sql               # CREATE / ALTER / DROP de ejemplo
│           ├── 02_DML.sql               # INSERT / UPDATE / DELETE de ejemplo
│           ├── 03_DQL.sql               # SELECT / JOIN / GROUP BY de ejemplo
│           ├── 04_VDL.sql               # CREATE VIEW / consulta / DROP VIEW de ejemplo
│           ├── 05_DCL.sql               # CREATE USER / GRANT / REVOKE de ejemplo
│           └── 06_TCL.sql               # START TRANSACTION / SAVEPOINT / COMMIT / ROLLBACK
├── py/
│   ├── conexion.py                      # Conexión a MariaDB (PyMySQL) y funciones comunes
│   ├── conexion_mariabd.py              # Ejemplo mínimo con el conector oficial `mariadb`
│   ├── ddl.py / dml.py / dql.py         # Equivalentes en Python de 01_DDL, 02_DML y 03_DQL
│   └── vdl.py / dcl.py / tcl.py         # Equivalentes en Python de 04_VDL, 05_DCL y 06_TCL
├── java/
│   ├── Conexion.java                    # Conexión a MariaDB (JDBC) y funciones comunes
│   ├── Ddl.java / Dml.java / Dql.java   # Equivalentes en Java de 01_DDL, 02_DML y 03_DQL
│   └── Vdl.java / Dcl.java / Tcl.java   # Equivalentes en Java de 04_VDL, 05_DCL y 06_TCL
├── shell/                               # Lanzadores que ejecutan SQL, Python y Java con un comando
│   ├── bash/                            # Linux y macOS: lib.sh, configurar-utf8.sh, instalar-connector-c.sh (solo macOS), ejecutar-sql/python/java/todo.sh
│   ├── powershell/                      # Windows PowerShell: lib.ps1, configurar-utf8.ps1, ejecutar-sql/python/java/todo.ps1
│   └── cmd/                             # Windows CMD: lib.cmd, configurar-utf8.cmd, ejecutar-sql/python/java/todo.cmd
├── requirements.txt                     # Dependencias de Python (PyMySQL)
├── .env.example                         # Plantilla de variables de entorno (se versiona)
├── .env                                 # Variables reales de conexión (local, ignorado por Git)
├── .gitattributes                       # Fin de línea fijo: LF en .sh, CRLF en .cmd y .ps1
├── .gitignore
├── LICENSE
└── README.md
```

> `.venv/` (entorno virtual de Python), `java/lib/` (driver JDBC) y `java/out/` (clases
> compiladas) se generan localmente y no se versionan.

## Requisitos previos

- [XAMPP](https://www.apachefriends.org/) con el módulo **MySQL/MariaDB** habilitado.
- Cliente `mariadb` (o `mysql`) disponible en la terminal. Ruta típica según sistema
  operativo:
  - **Windows:** `C:\xampp\mysql\bin\mariadb.exe`
  - **macOS:** `/Applications/XAMPP/xamppfiles/bin/mariadb`
  - **Linux:** `/opt/lampp/bin/mariadb`
- Visual Studio Code con la extensión "MySQL" o "SQLTools" (opcional, para editar).
- MySQL Workbench (opcional, para la ingeniería inversa del modelo E-R).
- Python 3.9+ (opcional, para la carpeta `py/`).
- JDK 17 o superior (opcional, para la carpeta `java/`).
- Git y una cuenta de GitHub (opcional, para control de versiones).

El detalle de versiones y cómo instalarlo en Windows, macOS y Linux está en
[Dependencias requeridas](#dependencias-requeridas); los comandos para ejecutar SQL, Python
y Java en cada sistema, en [Guía de ejecución por sistema operativo](#guía-de-ejecución-por-sistema-operativo).

## Dependencias requeridas

Resumen de todo lo que hay que tener instalado, por componente. Cada parte del proyecto es
independiente: para usar solo SQL basta MariaDB y su cliente; Python y Java son opcionales.

| Componente | Versión | Para qué se usa | Obligatorio para |
|---|---|---|---|
| **MariaDB** (servidor) | **10.2.1 o superior** (verificado con 10.4.28, la de XAMPP) | Aloja la base `glob_gusters`. Los scripts usan `CHECK`, `IF NOT EXISTS` en `ADD COLUMN`/`CREATE INDEX`/`CREATE TRIGGER` y `CREATE OR REPLACE VIEW`. | Todo |
| Cliente `mariadb` (o `mysql`) | El que trae el servidor | Ejecuta los archivos `.sql` desde la terminal. | SQL y diagnóstico |
| **Python** | **3.9 o superior** (probado con 3.13) | Scripts de `py/`. | Python |
| `PyMySQL` | `>=1.1` (`requirements.txt`) | Conector que usan todos los scripts de `py/` a través de `conexion.py`. | Python |
| `mariadb` (paquete de pip) | `>=1.1` (`requirements.txt`) | Conector oficial; solo lo usa `py/conexion_mariabd.py`. | Solo ese ejemplo |
| MariaDB Connector/C | **3.3.1 o superior** (librería del sistema, no es un paquete de pip) | Lo necesita el paquete `mariadb` para instalarse. El de XAMPP (3.1.x) es demasiado antiguo. | Solo `mariadb` |
| **JDK** | **17 o superior** (probado con 26) | Compila y ejecuta `java/` (usa *text blocks* y `record`). | Java |
| MariaDB Connector/J | **3.5.3** o superior de la serie 3.x (`java/lib/mariadb-java-client-<versión>.jar`, no se versiona; los lanzadores `ejecutar-java` lo actualizan solo; la 3.5.11 se probó con los 7 programas de `java/`) | Driver JDBC. | Java |
| Git Bash (solo Windows) | Cualquiera reciente | Ejecutar `sql/mariadb/check-mariadb.sh`. | Solo ese lanzador |

> **MariaDB, no MySQL de Oracle.** Los scripts usan sintaxis propia de MariaDB (por ejemplo
> `ADD COLUMN IF NOT EXISTS` y `CREATE INDEX IF NOT EXISTS`) que MySQL de Oracle no
> admite. Si en tu equipo conviven ambos servidores, comprueba que apuntas al de MariaDB
> (puerto 3306 en XAMPP). Los programas de Python, Java y el lanzador del diagnóstico
> conectan por TCP a `127.0.0.1` justamente para no caer en el socket de otro servidor.

### Instalación de las dependencias, por sistema operativo

Los comandos de **macOS** están comprobados en este proyecto. Los de **Windows** y
**Linux** usan las herramientas estándar de cada sistema pero no se ejecutaron en esta
máquina.

| Dependencia | Windows (PowerShell) | macOS | Linux (Debian/Ubuntu; en Fedora usa `dnf`) |
|---|---|---|---|
| MariaDB + cliente | Instala [XAMPP](https://www.apachefriends.org/) y arranca **MySQL**. Cliente: `C:\xampp\mysql\bin\mariadb.exe` | XAMPP, o `brew install mariadb`. Cliente: `/Applications/XAMPP/xamppfiles/bin/mariadb` | XAMPP (`/opt/lampp/bin/mariadb`), o `sudo apt install mariadb-server mariadb-client` |
| Python 3.9+ | `winget install Python.Python.3.13` | `brew install python` | `sudo apt install python3 python3-venv python3-pip` |
| Connector/C (solo para `mariadb`) | Instálalo desde [mariadb.com/downloads/connectors](https://mariadb.com/downloads/connectors/) si `pip` intenta compilar el paquete | `brew install mariadb-connector-c` | `sudo apt install libmariadb-dev build-essential python3-dev` (Fedora: `sudo dnf install mariadb-connector-c-devel gcc python3-devel`) |
| JDK 17+ | `winget install EclipseAdoptium.Temurin.17.JDK` | `brew install openjdk@17` | `sudo apt install openjdk-17-jdk` |
| Driver JDBC | Ver «Java» en la guía de ejecución | Ver «Java» en la guía de ejecución | Ver «Java» en la guía de ejecución |

Para comprobar las versiones instaladas:

```bash
mariadb --version      # o: mysql --version
python3 --version      # Windows: python --version
javac -version
```

## Guía de ejecución por sistema operativo

Esta guía reúne, para **Windows (PowerShell y CMD)**, **macOS** y **Linux**, cómo ejecutar los
archivos SQL, el diagnóstico, Python y Java. Los pasos 1 a 5 usan PowerShell en Windows; el
paso 6 es la guía completa para **CMD** (Símbolo del sistema). Todas las rutas son relativas
a la **raíz del proyecto** (la carpeta que contiene `README.md`).

> ¿Prefieres no copiar comandos? Los lanzadores de [`shell/`](#scripts-de-shell-shell) ejecutan
> todo esto con un solo comando en Windows, macOS y Linux.

Convenciones usadas en los comandos:

| Sistema | Cliente MariaDB (`$MARIADB`) | Si `root` tiene contraseña |
|---|---|---|
| Windows | `C:\xampp\mysql\bin\mariadb.exe` | Agrega `-p` al comando (la pide), o define antes `$env:MYSQL_PWD = "tu_clave"` |
| macOS | `/Applications/XAMPP/xamppfiles/bin/mariadb` | Agrega `-p`, o `export MYSQL_PWD='tu_clave'` |
| Linux | `/opt/lampp/bin/mariadb` (o `mariadb` si lo instalaste con el sistema) | Agrega `-p`, o `export MYSQL_PWD='tu_clave'` |

Antes de empezar, asegúrate de que el servidor MariaDB está en marcha: en Windows y macOS,
módulo **MySQL** del Panel de XAMPP en verde; en Linux, `sudo /opt/lampp/lampp start`
(o `sudo systemctl start mariadb` si es una instalación del sistema).

### 1. Archivos SQL (MariaDB)

Se ejecutan **en este orden** (cada uno depende del anterior):
`glob_gusters.sql` → `glob_gusters_insert.sql` → `commands/01_DDL.sql` → `02_DML.sql` →
`03_DQL.sql` → `04_VDL.sql` → `05_DCL.sql` → `06_TCL.sql`. Son repetibles.

**Windows (PowerShell).** Se usa la orden `source` del propio cliente, que lee el archivo
directamente: evita los problemas de codificación (tildes, `ñ`) de canalizar texto por
PowerShell.

```powershell
$MARIADB = "C:\xampp\mysql\bin\mariadb.exe"
$Scripts = @(
    "sql/mariadb/glob_gusters.sql",
    "sql/mariadb/glob_gusters_insert.sql",
    "sql/mariadb/commands/01_DDL.sql",
    "sql/mariadb/commands/02_DML.sql",
    "sql/mariadb/commands/03_DQL.sql",
    "sql/mariadb/commands/04_VDL.sql",
    "sql/mariadb/commands/05_DCL.sql",
    "sql/mariadb/commands/06_TCL.sql"
)
foreach ($s in $Scripts) {
    Write-Host ">>> $s"
    & $MARIADB -u root -h 127.0.0.1 -P 3306 --default-character-set=utf8mb4 -e "source $s"
}
```

**macOS:**

```bash
MARIADB=/Applications/XAMPP/xamppfiles/bin/mariadb
for f in sql/mariadb/glob_gusters.sql sql/mariadb/glob_gusters_insert.sql \
         sql/mariadb/commands/01_DDL.sql sql/mariadb/commands/02_DML.sql \
         sql/mariadb/commands/03_DQL.sql sql/mariadb/commands/04_VDL.sql \
         sql/mariadb/commands/05_DCL.sql sql/mariadb/commands/06_TCL.sql; do
    echo ">>> $f"
    "$MARIADB" -u root -h 127.0.0.1 -P 3306 --default-character-set=utf8mb4 < "$f" || break
done
```

**Linux:** igual que macOS, cambiando la primera línea por
`MARIADB=/opt/lampp/bin/mariadb` (o `MARIADB=mariadb` si usas el MariaDB del sistema).

Si hubiera un error, el bucle de macOS/Linux se detiene en el primer archivo que falle
(`|| break`); el de PowerShell continúa, así que revisa los mensajes.

### 2. Diagnóstico del servidor (`check-mariadb`)

Es de solo lectura y se ejecuta con `--force`. Dos formas:

| Sistema | Con la configuración del `.env` | Directamente (usa la base `glob_gusters`) |
|---|---|---|
| macOS / Linux | `sh sql/mariadb/check-mariadb.sh` | `"$MARIADB" -u root -h 127.0.0.1 -P 3306 --default-character-set=utf8mb4 --force < sql/mariadb/check-mariadb.sql` |
| Windows | En **Git Bash**: `bash sql/mariadb/check-mariadb.sh` (si el cliente no está en el `PATH`, antes: `export MARIADB_BIN=/c/xampp/mysql/bin/mariadb.exe`) | `& $MARIADB -u root -h 127.0.0.1 -P 3306 --default-character-set=utf8mb4 --force -e "source sql/mariadb/check-mariadb.sql"` |

En Windows también existen `sql\mariadb\check-mariadb.ps1` (PowerShell, con
`powershell -ExecutionPolicy Bypass -File sql\mariadb\check-mariadb.ps1`) y
`sql\mariadb\check-mariadb.cmd` (CMD), que leen el `.env` sin necesitar Git Bash.

Para usar otra base desde la forma directa, agrega
`--init-command="SET @glob_gusters_db = 'mi_base'"`. En Windows el lanzador `.sh` necesita
Git Bash; la forma directa funciona en PowerShell sin nada más.

Es normal que aparezcan los errores 1577 (`event_scheduler` apagado) y 1558 (`mysql.proc`
desactualizada): son límites del entorno, descritos en el encabezado del script.

### 3. Python

Requisitos: Python 3.9+, el servidor en marcha y la base ya creada (paso 1). Se trabaja
dentro de un entorno virtual (`.venv/`, no se versiona) con las dependencias de
`requirements.txt`.

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1          # si PowerShell lo bloquea: Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
pip install -r requirements.txt
Copy-Item .env.example .env         # una sola vez; edita GLOB_GUSTERS_PASSWORD si tu root tiene clave
python py\conexion.py
```

En `cmd.exe` la activación es `.venv\Scripts\activate.bat`.

**macOS y Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env                # una sola vez; edita GLOB_GUSTERS_PASSWORD si tu root tiene clave
python3 py/conexion.py
```

> `requirements.txt` incluye `mariadb`, que necesita MariaDB Connector/C ≥ 3.3.1 instalado
> en el sistema (ver la tabla de instalación). Si solo quieres usar PyMySQL, comenta esa
> línea antes de instalar: todo `py/` funciona igual salvo `conexion_mariabd.py`. En macOS,
> ejecuta antes `bash shell/bash/instalar-connector-c.sh`: instala `mariadb-connector-c` con
> Homebrew y define `LDFLAGS`, `CPPFLAGS` y `MARIADB_CONFIG` (también en `~/.zshrc`). Así
> `pip` no falla con «requires MariaDB Connector/C >= 3.3.1» (el Connector/C 3.1.x de XAMPP es
> más antiguo). El lanzador `ejecutar-python.sh` lo hace solo en macOS.

> **Requisito previo (obligatorio):** antes de ejecutar cualquier script de Python, el entorno
> virtual `.venv` debe estar **instalado y activado**. Si no existe, créalo con
> `python3 -m venv .venv`; actívalo con `source .venv/bin/activate` (macOS y Linux),
> `.venv\Scripts\Activate.ps1` (PowerShell) o `.venv\Scripts\activate.bat` (CMD), e instala
> las dependencias con `pip install -r requirements.txt`. El indicador `(.venv)` en la
> terminal confirma que está activo. En **macOS y Linux los scripts se ejecutan con el
> comando `python3`** (no `python`); en Windows se usa `python`.

Con el entorno activo y **desde la raíz del proyecto**, ejecuta los scripts en el mismo orden
que los SQL. En Windows las rutas llevan `\`.

**Windows (PowerShell):**

```powershell
python py\conexion.py             # comprueba la conexión
python py\ddl.py                  # 01_DDL
python py\dml.py                  # 02_DML
python py\dql.py                  # 03_DQL  (o: python py\dql.py disponibles)
python py\vdl.py                  # 04_VDL  (python py\vdl.py --drop elimina las vistas)
python py\dcl.py                  # 05_DCL  (requiere una cuenta administrativa)
python py\tcl.py                  # 06_TCL
python py\conexion_mariabd.py     # ejemplo con el conector oficial `mariadb`
```

**Windows (CMD):**

```bat
python py\conexion.py
python py\ddl.py
python py\dml.py
python py\dql.py
python py\vdl.py
python py\dcl.py
python py\tcl.py
python py\conexion_mariabd.py
```

**macOS y Linux:**

```bash
python3 py/conexion.py
python3 py/ddl.py                  # 01_DDL
python3 py/dml.py                  # 02_DML
python3 py/dql.py                  # 03_DQL  (o: python3 py/dql.py disponibles)
python3 py/vdl.py                  # 04_VDL  (python3 py/vdl.py --drop elimina las vistas)
python3 py/dcl.py                  # 05_DCL  (requiere una cuenta administrativa)
python3 py/tcl.py                  # 06_TCL
python3 py/conexion_mariabd.py     # ejemplo con el conector oficial `mariadb`
```

Para ejecutar solo uno, escribe únicamente su línea (por ejemplo, `python py\ddl.py` en Windows o `python3 py/ddl.py` en macOS y Linux).
Sin activar el entorno se puede llamar a su intérprete directamente:
`.venv\Scripts\python.exe py\ddl.py` (Windows) o `.venv/bin/python3 py/ddl.py` (macOS/Linux).
Para salir del entorno: `deactivate`. Si prefieres no escribirlos a mano,
`shell\powershell\ejecutar-python.ps1` y `shell\cmd\ejecutar-python.cmd` crean el entorno, actualizan
`pip`, instalan las dependencias y ejecutan todo en orden (ver «Scripts de shell»).

### 5. Java

Requisitos: JDK 17+, el servidor en marcha y la base ya creada (paso 1). El driver JDBC se
descarga una sola vez a `java/lib/` (no se versiona). Los comandos se ejecutan desde la
carpeta `java/`; el programa encuentra el `.env` en la raíz del proyecto.

**Windows (PowerShell):**

```powershell
cd java
New-Item -ItemType Directory -Force lib | Out-Null
Invoke-WebRequest -Uri https://repo1.maven.org/maven2/org/mariadb/jdbc/mariadb-java-client/3.5.3/mariadb-java-client-3.5.3.jar -OutFile lib\mariadb-java-client-3.5.3.jar
javac -encoding UTF-8 -d out (Get-ChildItem *.java).Name
java -cp "out;lib/*" Conexion
```

**macOS y Linux:**

```bash
cd java
mkdir -p lib
curl -L -o lib/mariadb-java-client-3.5.3.jar \
  https://repo1.maven.org/maven2/org/mariadb/jdbc/mariadb-java-client/3.5.3/mariadb-java-client-3.5.3.jar
javac -encoding UTF-8 -d out *.java
java -cp "out:lib/*" Conexion
```

La única diferencia entre sistemas al ejecutar es el **separador del classpath**: `;` en
Windows (`"out;lib/*"`) y `:` en macOS/Linux (`"out:lib/*"`). Escribe siempre el classpath
**entre comillas**: en PowerShell y en CMD el `;` separa comandos y el `*` se expandiría. Los
programas se ejecutan en el mismo orden que los SQL, desde la carpeta `java/` y después de
compilar (`javac ...` de arriba).

**Windows (PowerShell):**

```powershell
cd java
java -cp "out;lib/*" Conexion     # comprueba la conexión
java -cp "out;lib/*" Ddl          # 01_DDL
java -cp "out;lib/*" Dml          # 02_DML
java -cp "out;lib/*" Dql          # 03_DQL  (o: ... Dql disponibles)
java -cp "out;lib/*" Vdl          # 04_VDL  (... Vdl --drop elimina las vistas)
java -cp "out;lib/*" Dcl          # 05_DCL  (requiere una cuenta administrativa)
java -cp "out;lib/*" Tcl          # 06_TCL
```

**Windows (CMD):**

```bat
cd java
java -cp "out;lib/*" Conexion
java -cp "out;lib/*" Ddl
java -cp "out;lib/*" Dml
java -cp "out;lib/*" Dql
java -cp "out;lib/*" Vdl
java -cp "out;lib/*" Dcl
java -cp "out;lib/*" Tcl
```

Para ejecutar solo uno, escribe únicamente su línea (por ejemplo,
`java -cp "out;lib/*" Ddl`). Si cambias algún `.java`, vuelve a compilar antes. Si prefieres no
escribirlos a mano, `shell\powershell\ejecutar-java.ps1` y `shell\cmd\ejecutar-java.cmd` descargan el
driver, compilan y ejecutan todo en orden (ver «Scripts de shell»).

**macOS y Linux:**

```bash
java -cp "out:lib/*" Conexion
java -cp "out:lib/*" Ddl          # 01_DDL
java -cp "out:lib/*" Dml          # 02_DML
java -cp "out:lib/*" Dql          # 03_DQL  (o: ... Dql disponibles)
java -cp "out:lib/*" Vdl          # 04_VDL  (... Vdl --drop elimina las vistas)
java -cp "out:lib/*" Dcl          # 05_DCL  (requiere una cuenta administrativa)
java -cp "out:lib/*" Tcl          # 06_TCL
```

### 6. Windows CMD (Símbolo del sistema)

Guía equivalente a las anteriores para quien trabaja en **`cmd.exe`** en lugar de PowerShell.
Abre el Símbolo del sistema (`Win + R`, escribe `cmd` y pulsa Enter), ve a la raíz del
proyecto con `cd` y sigue los pasos. Diferencias con PowerShell: las variables se definen con
`set` y se leen como `%VARIABLE%`, los comentarios son `REM`, la continuación de línea es `^`
y la redirección de archivos con `<` sí funciona (pasa el contenido tal cual, sin problemas de
tildes ni `ñ`).

> Los comandos de esta sección usan herramientas estándar de Windows pero **no se ejecutaron
> en esta máquina** (el proyecto se verificó en macOS). Si tu proyecto está en una carpeta
> con espacios, entrecomilla las rutas.

```bat
cd C:\ruta\a\glob-gusters-videoclub
```

#### 6.1 Archivos SQL

Los 8 scripts, en orden (el servidor de XAMPP debe estar en marcha, módulo **MySQL** en
verde). El comando `for` va en una sola instrucción; el `^` al final de línea la continúa:

```bat
set MARIADB=C:\xampp\mysql\bin\mariadb.exe

for %f in (sql\mariadb\glob_gusters.sql sql\mariadb\glob_gusters_insert.sql ^
           sql\mariadb\commands\01_DDL.sql sql\mariadb\commands\02_DML.sql ^
           sql\mariadb\commands\03_DQL.sql sql\mariadb\commands\04_VDL.sql ^
           sql\mariadb\commands\05_DCL.sql sql\mariadb\commands\06_TCL.sql) do ^
    @echo ^>^>^> %f & "%MARIADB%" -u root -h 127.0.0.1 -P 3306 --default-character-set=utf8mb4 < "%f"
```

- Si `root` tiene contraseña, define antes `set MYSQL_PWD=tu_clave` (sin comillas ni espacios
  alrededor del `=`) o agrega `-p` al comando (la pedirá en cada script).
- Si pones estos comandos dentro de un archivo `.bat`, duplica el signo de porcentaje:
  `%%f` en lugar de `%f`.
- Para ejecutar un solo archivo:
  `"%MARIADB%" -u root -h 127.0.0.1 -P 3306 --default-character-set=utf8mb4 < sql\mariadb\glob_gusters.sql`

#### 6.2 Diagnóstico del servidor

```bat
REM Diagnóstico del servidor (solo lectura; usa la base glob_gusters)
"%MARIADB%" -u root -h 127.0.0.1 -P 3306 --default-character-set=utf8mb4 --force < sql\mariadb\check-mariadb.sql

REM Con otra base: agrega --init-command="SET @glob_gusters_db = 'mi_base'"
```

El lanzador `sql\mariadb\check-mariadb.sh` no se puede usar en CMD (es un script `sh`); en
su lugar usa `sql\mariadb\check-mariadb.cmd`, que lee el `.env` igual que el `.sh`.

#### 6.3 Python

```bat
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
copy .env.example .env
REM (edita .env si tu root tiene contraseña: GLOB_GUSTERS_PASSWORD=...)

python py\conexion.py
python py\ddl.py
python py\dml.py
python py\dql.py
python py\vdl.py
python py\dcl.py
python py\tcl.py
python py\conexion_mariabd.py
```

- Al activar el entorno el indicador cambia a `(.venv) C:\...>`. Para salir: `deactivate`.
- Si `python` no se reconoce, prueba con `py -m venv .venv` (lanzador de Python para Windows).
- `copy .env.example .env` solo se hace una vez; si `.env` ya existe, pregunta antes de
  sobrescribirlo.
- `requirements.txt` incluye `mariadb`, que necesita MariaDB Connector/C (ver «Dependencias
  requeridas»); si solo usas PyMySQL, comenta esa línea antes de instalar.

#### 6.4 Java

```bat
cd java
mkdir lib
curl -L -o lib\mariadb-java-client-3.5.3.jar https://repo1.maven.org/maven2/org/mariadb/jdbc/mariadb-java-client/3.5.3/mariadb-java-client-3.5.3.jar
javac -encoding UTF-8 -d out *.java

java -cp "out;lib/*" Conexion
java -cp "out;lib/*" Ddl
java -cp "out;lib/*" Dml
java -cp "out;lib/*" Dql
java -cp "out;lib/*" Vdl
java -cp "out;lib/*" Dcl
java -cp "out;lib/*" Tcl
```

- El separador del classpath en Windows es `;` (y va entre comillas).
- `curl` viene incluido en Windows 10 (1803) y posteriores; si no lo tienes, descarga el JAR
  desde el enlace en el navegador y guárdalo en `java\lib\`.
- Para ejecutar una sola consulta: `java -cp "out;lib/*" Dql disponibles`; para eliminar las
  vistas: `java -cp "out;lib/*" Vdl --drop`.
- El programa encuentra el `.env` de la raíz estando dentro de `java\`.

#### 6.5 Si las tildes o la `ñ` se ven mal en la consola

La consola de CMD usa por defecto una página de códigos antigua. Antes de ejecutar los
programas, cambia a UTF-8 (solo afecta a esa ventana):

```bat
chcp 65001
```

Esto solo afecta a **cómo se muestra** el texto; los datos en la base están guardados
correctamente en `utf8mb4`. Los lanzadores de `shell\cmd\` ya lo hacen por ti; el resto de
capas está en [Tildes y `ñ` en la terminal](#tildes-y-ñ-en-la-terminal).

### Probar la creación desde cero sin tocar tu base

Para comprobar que los scripts funcionan sobre un servidor vacío sin eliminar tu base
`glob_gusters`, levanta una segunda instancia de MariaDB con datos temporales (ejemplo de
macOS con XAMPP; ajusta las rutas en otros sistemas):

```bash
B=/Applications/XAMPP/xamppfiles; T=$(mktemp -d)
$B/bin/mysql_install_db --no-defaults --basedir=$B --datadir=$T/data \
    --auth-root-authentication-method=normal --skip-test-db
$B/sbin/mysqld --no-defaults --basedir=$B --datadir=$T/data --port=3399 \
    --bind-address=127.0.0.1 --socket=/tmp/gg3399.sock --pid-file=$T/mysqld.pid &
# ... ejecuta los scripts con -P 3399; Python, Java y check-mariadb.sh con GLOB_GUSTERS_PORT=3399 ...
$B/bin/mariadb-admin -u root -h 127.0.0.1 -P 3399 shutdown; rm -rf "$T" /tmp/gg3399.sock
```

El socket debe tener una ruta corta (el límite es de 103 caracteres), por eso se usa `/tmp`.

### Tildes y `ñ` en la terminal

Todo el proyecto trabaja en **UTF-8**: los archivos están guardados en UTF-8, la base usa
`utf8mb4` y cada capa fija la codificación para que las tildes y la `ñ` se lean y se
impriman igual en cualquier sistema.

| Capa | Qué se hace | Dónde |
|---|---|---|
| SQL (MariaDB) | `SET NAMES utf8mb4;` al inicio de cada script, además de `--default-character-set=utf8mb4` en los lanzadores: el texto se interpreta bien aunque el cliente no se lance con esa opción (phpMyAdmin, otro cliente). | `sql/mariadb/` y `sql/mariadb/commands/` |
| Python | `conexion.py` fuerza UTF-8 en `stdout` y `stderr` al importarse (`reconfigure`), así que `ddl.py`, `dml.py`, `dql.py`, `vdl.py`, `dcl.py`, `tcl.py` y `conexion_mariabd.py` imprimen UTF-8 aunque la salida se redirija a un archivo o a una bitácora. | `py/conexion.py` |
| Java | `Conexion.configurarSalida()` (llamada en la primera línea de cada `main`) fuerza UTF-8 en `System.out` y `System.err` cuando la salida no va a una terminal; los fuentes se compilan con `javac -encoding UTF-8`. | `java/Conexion.java` |
| PowerShell | `lib.ps1` pone la consola y `$OutputEncoding` en UTF-8 (sin BOM) y `PYTHONIOENCODING=utf-8`; los `.ps1` se guardan con BOM para que Windows PowerShell 5.1 lea bien sus tildes. | `shell/powershell/lib.ps1` |
| CMD | `lib.cmd` ejecuta `chcp 65001`. Los mensajes de los `.cmd` no llevan tildes a propósito (el intérprete de lotes las trata mal según la página de códigos); la salida de SQL, Python y Java sí sale con tildes. | `shell/cmd/lib.cmd` |
| Bash | Los lanzadores no necesitan ajustes: `bash` pasa los bytes tal cual y la terminal de Linux/macOS ya es UTF-8. Para la terminal interactiva está `configurar-utf8.sh`. | `shell/bash/` |

Con los lanzadores de `shell/` y `sql/mariadb/check-mariadb.*` no hay que hacer nada. Si
ejecutas los programas **a mano** en una consola de Windows, pon antes la consola en UTF-8
(solo afecta a esa ventana):

```powershell
# Windows PowerShell
[Console]::OutputEncoding = [Text.UTF8Encoding]::new($false); $OutputEncoding = [Console]::OutputEncoding
```

```bat
:: Windows CMD
chcp 65001
```

Para no escribirlo cada vez, la carpeta `shell/` trae un script por intérprete que deja
**la terminal actual** en UTF-8. Hay que cargarlo en esa terminal (con punto, `call` o
`source`); si se ejecuta sin eso, el cambio vale solo para el proceso del script y se pierde.

| Intérprete | Comando | Qué configura |
|---|---|---|
| PowerShell | `. .\shell\powershell\configurar-utf8.ps1` | Página de códigos 65001, `[Console]::OutputEncoding`/`InputEncoding`, `$OutputEncoding` y `PYTHONIOENCODING`. Con `-Persistente` agrega el bloque a `$PROFILE` (una sola vez) para todas las sesiones nuevas. |
| CMD | `call shell\cmd\configurar-utf8.cmd` | `chcp 65001` y `PYTHONIOENCODING`. |
| Bash | `source shell/bash/configurar-utf8.sh` | `LANG`/`LC_ALL` con un *locale* UTF-8 disponible (si ya lo es, no lo cambia) y `PYTHONIOENCODING`. |

Cada uno imprime una línea de prueba (`áéíóú ñ Ñ ü ¿¡ €`). En CMD y PowerShell la ventana
debe usar una fuente TrueType (Consolas, Cascadia Mono o Lucida Console). Para el cliente
`mariadb` a mano añade además `--default-character-set=utf8mb4`.

En macOS y Linux basta con una terminal y un *locale* UTF-8 (`echo $LANG` debe terminar en
`UTF-8`; si no, `export LANG=es_ES.UTF-8` o `export LANG=C.UTF-8`). En clientes gráficos,
la codificación la gestiona la propia herramienta, por lo que conviene usar un cliente que
soporte `utf8mb4` o definir la codificación de la sesión antes de ejecutar los scripts.

Esto solo afecta a **cómo se muestra** el texto: los datos se guardan correctamente en
`utf8mb4` en cualquier caso.

### Errores frecuentes

| Mensaje | Causa y solución |
|---|---|
| `Acceso denegado para 'root' en localhost:3306 sin contraseña` (Python/Java) o `Access denied for user 'root'@'localhost'` (SQL) | El usuario tiene contraseña y no se envió. Define `GLOB_GUSTERS_PASSWORD` en `.env` (Python/Java) o agrega `-p` (SQL). |
| `Acceso denegado para ...: el usuario o la contraseña son incorrectos` | Se envió una contraseña y el servidor la rechazó: revisa `GLOB_GUSTERS_USER` y `GLOB_GUSTERS_PASSWORD` en el `.env` o en las variables del sistema. Si además tienes MySQL de Oracle instalado, comprueba que conectas al servidor correcto (`-h 127.0.0.1 -P 3306`) y no a su socket. |
| `Got error 176 "Read page with wrong checksum" from storage engine Aria` (o «tabla dañada») | Una tabla del esquema `mysql` quedó dañada, normalmente por un cierre sucio de XAMPP. Los programas de `py/` y `java/` imprimen los pasos: `mysqlcheck -u root -p --check --databases mysql`, luego `--repair`; si no basta, con MySQL detenido `aria_chk --recover --force *.MAI` en `mysql\data\mysql`. Para evitarlo, detén MySQL con **Stop** antes de apagar el equipo. |
| `Unknown database 'glob_gusters'` / error 1049 | Aún no ejecutaste `glob_gusters.sql` (paso 1). |
| `requires MariaDB Connector/C >= 3.3.1` al hacer `pip install` | Falta el Connector/C del sistema (ver tabla de instalación) o comenta `mariadb` en `requirements.txt`. |
| `ModuleNotFoundError: No module named 'pymysql'` | No activaste el entorno virtual o no ejecutaste `pip install -r requirements.txt`. |
| `ClassNotFoundException` / `No suitable driver` en Java | Falta el JAR en `java/lib/`, o el separador del classpath es incorrecto para tu sistema (`;` Windows, `:` macOS/Linux). |
| `class file has wrong version` / `invalid source release` | El JDK es anterior a 17. |
| Tildes o `ñ` mal mostradas (`Ã³`, `Ã±`, `?`) | La terminal no está en UTF-8: ver [Tildes y `ñ` en la terminal](#tildes-y-ñ-en-la-terminal) (en Windows, `chcp 65001`). Ejecuta los SQL con `-e "source ..."` (no canalices con `Get-Content`) y `--default-character-set=utf8mb4`. |

## Scripts de shell (`shell/`)

La carpeta `shell/` reúne lanzadores listos para ejecutar **todo el proyecto con un solo
comando**: los scripts SQL de MariaDB, el diagnóstico del servidor, los programas de Python
y los de Java. Hay una versión por sistema operativo y cada una hace lo mismo:

| Sistema | Carpeta | Extensión | Intérprete |
|---|---|---|---|
| Linux y macOS | `shell/bash/` | `.sh` | Bash |
| Windows (PowerShell) | `shell/powershell/` | `.ps1` | Windows PowerShell 5.1 o PowerShell 7 |
| Windows (CMD) | `shell/cmd/` | `.cmd` | `cmd.exe` |

| Lanzador | Qué ejecuta |
|---|---|
| `ejecutar-sql` | Primero muestra la versión del cliente y del servidor y avisa si el servidor es anterior a MariaDB 10.2.1 (no instala nada; sin conexión avisa y sigue). Luego ejecuta los scripts del proyecto en orden y, al final, el diagnóstico `check-mariadb`. Si falla la creación de la base (los 2 primeros scripts: tablas e inserción de datos), muestra el error y detiene SQL, Python y Java; si falla cualquiera de los otros 6, muestra el error y detiene el programa. |
| `ejecutar-python` | Primero verifica que exista el entorno virtual `.venv` y lo confirma en pantalla; si falta, lo crea y confirma la creación. Si no se puede crear, muestra un aviso y se detiene (no instala ni ejecuta nada de Python). Después actualiza `pip` (si no hay Internet avisa y sigue); **solo en macOS** ejecuta antes `instalar-connector-c.sh` (ver abajo) para que el paquete `mariadb` compile; en Linux no hace nada extra. Instala `requirements.txt`, muestra la lista de dependencias instaladas con sus versiones y ejecuta `conexion`, `ddl`, `dml`, `dql`, `vdl`, `dcl`, `tcl` y `conexion_mariabd` de `py/`. |
| `instalar-connector-c` (solo `.sh`, macOS) | Instala `mariadb-connector-c` con Homebrew (si falta), exporta `LDFLAGS`, `CPPFLAGS` y `MARIADB_CONFIG` con la ruta de `brew --prefix` (Apple Silicon o Intel) y las guarda sin duplicar en `~/.zshrc`. En Linux no hace nada. Lo llama `ejecutar-python.sh`; también puede ejecutarse solo. |
| `ejecutar-java` | Primero actualiza el driver JDBC: consulta en Maven Central la última versión **3.x** de MariaDB Connector/J y, si `java/lib/` no la tiene, la descarga y borra las anteriores (sin Internet usa el que haya; si no hay ninguno, baja la 3.5.3). Solo avanza dentro de la serie 3.x: la 4.x exige TLS y no conecta con el MariaDB de XAMPP sin configurarlo. Al descargar muestra «Driver JDBC descargado correctamente» y, antes de compilar, verifica que haya un `.jar` válido en `java/lib/` («Driver JDBC verificado»); si no lo hay, muestra un error y se detiene sin ejecutar nada de Java. Luego compila `java/*.java` y ejecuta `Conexion`, `Ddl`, `Dml`, `Dql`, `Vdl`, `Dcl` y `Tcl`. |
| `ejecutar-todo` | Los tres anteriores, en ese orden. Se detiene en el primer fallo de SQL o de Java. Si falla **Python** (por ejemplo, no se pudo crear `.venv`), muestra un aviso, **continúa con Java** y al final indica «Proyecto ejecutado con advertencias»; en ese caso termina con código 0. |
| `lib` | Funciones comunes (no se ejecuta directamente): lee el `.env`, localiza el cliente `mariadb` y define el orden de los scripts SQL. |

**Qué pasa si algo falla.** Todos los lanzadores muestran el error en la terminal y se detienen así:

| Falla | Resultado |
|---|---|
| Creación de la base (`glob_gusters.sql`, tablas, o `glob_gusters_insert.sql`, datos) | Error y mensaje «Se detiene la ejecución de los demás scripts SQL, de Python y de Java». `ejecutar-todo` termina con error. |
| Cualquiera de los otros 6 scripts SQL (`01_DDL` a `06_TCL`) | Error y «Se detiene la ejecución del programa». |
| Diagnóstico (`check-mariadb`) | Solo un aviso (se ejecuta con `--force` y es informativo); no detiene nada. |
| Entorno virtual de Python o sus scripts | Aviso; `ejecutar-todo` continúa con Java y cierra con «Proyecto ejecutado con advertencias». |
| Driver JDBC ausente o no descargado | Error y se detienen los scripts de Java. |

### Antes de empezar

1. Arranca el servidor MariaDB (módulo **MySQL** de XAMPP en verde).
2. Ten instalado lo que vayas a ejecutar: el cliente `mariadb` para SQL, Python 3.9+ para
   Python y JDK 17+ para Java (ver [Dependencias requeridas](#dependencias-requeridas)).
3. No hace falta crear el `.env` a mano: si no existe, `ejecutar-python` y `ejecutar-java` lo
   copian desde `.env.example`. Si tu usuario `root` **tiene contraseña**, escríbela en
   `GLOB_GUSTERS_PASSWORD` dentro del `.env` (o defínela como variable de entorno).
4. Los lanzadores se pueden llamar **desde cualquier carpeta**: ubican solos la raíz del
   proyecto.

Todos leen la conexión con la misma prioridad que Python y Java: variable de entorno del
sistema, luego `.env`, luego el valor por defecto (`127.0.0.1:3306`, usuario `root`, base
`glob_gusters`).

### Linux y macOS (Bash)

```bash
# Todo el proyecto
bash shell/bash/ejecutar-todo.sh

# Por partes
bash shell/bash/ejecutar-sql.sh
bash shell/bash/ejecutar-python.sh
bash shell/bash/ejecutar-java.sh
```

Opciones: `ejecutar-sql.sh --sin-diagnostico` y `ejecutar-todo.sh --sin-python --sin-java`; `-h`
muestra la ayuda de cada script. Los archivos ya se versionan como ejecutables (`chmod +x`),
así que también sirve `./shell/bash/ejecutar-todo.sh`.

Si el cliente `mariadb` no está en el `PATH` (es lo habitual con XAMPP), indica su ruta:

```bash
# macOS (XAMPP)
MARIADB_BIN=/Applications/XAMPP/xamppfiles/bin/mariadb bash shell/bash/ejecutar-todo.sh
# Linux (XAMPP)
MARIADB_BIN=/opt/lampp/bin/mariadb bash shell/bash/ejecutar-todo.sh
```

### Windows (PowerShell)

```powershell
# Todo el proyecto
powershell -ExecutionPolicy Bypass -File shell\powershell\ejecutar-todo.ps1

# Por partes
powershell -ExecutionPolicy Bypass -File shell\powershell\ejecutar-sql.ps1
powershell -ExecutionPolicy Bypass -File shell\powershell\ejecutar-python.ps1
powershell -ExecutionPolicy Bypass -File shell\powershell\ejecutar-java.ps1
```

- `-ExecutionPolicy Bypass` solo vale para esa ejecución y evita el bloqueo de scripts de
  PowerShell. En PowerShell 7 se usa `pwsh` en lugar de `powershell`. Si prefieres no
  escribirlo, abre la sesión con `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`
  y llama a los scripts directamente: `.\shell\powershell\ejecutar-todo.ps1`.
- Opciones: `-SinDiagnostico` (`ejecutar-sql.ps1`), `-SinPython` y `-SinJava`
  (`ejecutar-todo.ps1`).
- Si `mariadb.exe` no está en el `PATH` y XAMPP no está en `C:\xampp`:
  `$env:MARIADB_BIN = "D:\xampp\mysql\bin\mariadb.exe"` antes de ejecutar.
- Si Windows marca los scripts como descargados de Internet: `Unblock-File shell\powershell\*.ps1`.

### Windows (CMD)

```bat
REM Todo el proyecto
shell\cmd\ejecutar-todo.cmd

REM Por partes
shell\cmd\ejecutar-sql.cmd
shell\cmd\ejecutar-python.cmd
shell\cmd\ejecutar-java.cmd
```

- Opciones: `--sin-diagnostico` (`ejecutar-sql.cmd`), `--sin-python` y `--sin-java`
  (`ejecutar-todo.cmd`).
- Si `mariadb.exe` no está en el `PATH` y XAMPP no está en `C:\xampp`:
  `set MARIADB_BIN=D:\xampp\mysql\bin\mariadb.exe` antes de ejecutar.
- Los mensajes de los `.cmd` no llevan tildes a propósito: `cmd.exe` las muestra mal según la
  página de códigos. Los scripts activan UTF-8 (`chcp 65001`) solo para esa ventana.
- Una contraseña con caracteres especiales de CMD (`%`, `^`, `&`) puede interpretarse mal desde
  el `.env`; en ese caso usa los lanzadores de PowerShell.

### Qué hacen y qué no

- Los lanzadores solo **orquestan** los mismos comandos de la [Guía de ejecución](#guía-de-ejecución-por-sistema-operativo);
  no cambian ningún script SQL, Python ni Java. Son repetibles.
- El script `dcl` (SQL, Python y Java) crea cuentas de ejemplo y requiere un usuario con
  privilegios administrativos (el `root` de XAMPP los tiene).
- En macOS, `ejecutar-python.sh` instala antes MariaDB Connector/C (`instalar-connector-c.sh`). Si el paquete `mariadb` de pip aun así no se puede instalar, el lanzador de
  Python instala solo PyMySQL, omite `conexion_mariabd.py` con un aviso y termina bien.
- Código de salida: `0` si todo terminó bien, distinto de `0` en cuanto algo falla (útil para
  automatizar). En el diagnóstico completo (comentado por defecto) pueden verse algunos errores
  1558 si la base se ejecuta en un entorno con configuraciones no estándar.
- Verificación: los lanzadores se ejecutan sobre la misma secuencia SQL del proyecto y deben
  dejar la base funcional y consistente en phpMyAdmin o en el cliente `mariadb`.

## Ejecución paso a paso en XAMPP MariaDB

Todos los ejemplos usan la misma conexión en los tres sistemas operativos
(`-u root -p -h 127.0.0.1 -P 3306 --default-character-set=utf8mb4`); sólo cambia la
ruta del binario y cómo el shell redirige la entrada estándar. Por defecto, XAMPP
configura el usuario `root` **sin contraseña**: cuando el comando pida `Enter password:`,
basta con presionar Enter.

### 1. Iniciar los servicios

**Windows y macOS:** abre el **Panel de Control de XAMPP** y arranca el módulo
**MySQL** (usa el motor MariaDB internamente). Verifica que el estado quede en verde
("Running").

**Linux:** inicia XAMPP desde la terminal con:

```bash
sudo /opt/lampp/lampp start
```

o abre el panel gráfico con `sudo /opt/lampp/manager-linux-x64.run` si está instalado.
Verifica que el módulo MySQL/MariaDB quede activo.

### 2. Verificar que el cliente `mariadb` es accesible

**Windows (PowerShell):**

```powershell
# Agrega C:\xampp\mysql\bin al PATH si el comando no se reconoce.
C:\xampp\mysql\bin\mariadb.exe --version
```

**macOS:**

```bash
/Applications/XAMPP/xamppfiles/bin/mariadb --version
# o, si ya agregaste esa ruta al PATH:
mariadb --version
```

**Linux:**

```bash
/opt/lampp/bin/mariadb --version
# o, si ya agregaste esa ruta al PATH:
mariadb --version
```

También puedes usar el script de diagnóstico incluido en el proyecto,
`sql/mariadb/check-mariadb.sql`, para confirmar de un vistazo:

- Versión, host y puerto del servidor.
- Sesión actual (usuario autenticado, base de datos seleccionada) y procesos
  activos.
- Estado del servidor (uptime, conexiones, consultas totales) y configuración
  relevante (charset, collation, `sql_mode`).
- Motores de almacenamiento disponibles (confirma que InnoDB, requerido por el
  proyecto, esté activo).
- Tablas, vistas y triggers ya creados en `glob_gusters`, y un resumen de filas
  por tabla.
- Usuarios del servidor y su estado de seguridad, sin exponer contraseñas.

Ajusta la ruta del binario según tu sistema operativo (como en el paso 3) y usa
siempre **`--force`**: el script está pensado para poder correrse en cualquier
momento (incluso antes de crear la base de datos del proyecto), y algunas de sus
secciones esperan condiciones que pueden no cumplirse todavía —por ejemplo, que
`glob_gusters` ya exista, o que el *event scheduler* esté activo—; sin `--force`
el cliente se detendría en la primera de ellas. El encabezado del script documenta
las tres limitaciones conocidas del entorno y por qué no son errores del proyecto.

```bash
mariadb -u root -p -h 127.0.0.1 -P 3306 --default-character-set=utf8mb4 \
    --force < sql/mariadb/check-mariadb.sql
```

**Con la configuración del `.env`:** un archivo SQL no puede leer el `.env`, así que el
lanzador `sql/mariadb/check-mariadb.sh` lo hace por él. Lee `GLOB_GUSTERS_HOST`,
`GLOB_GUSTERS_PORT`, `GLOB_GUSTERS_USER`, `GLOB_GUSTERS_PASSWORD` y `GLOB_GUSTERS_DB`
(el sistema tiene prioridad sobre el `.env`), se conecta con ellos —usa TCP aunque el host
sea `localhost`— y ya lleva `--force`. El nombre de la base llega al script SQL por la
variable de sesión `@glob_gusters_db`; si se ejecuta el `.sql` directamente se usa
`glob_gusters`.

```bash
sh sql/mariadb/check-mariadb.sh
```

### 3. Ejecutar los scripts en orden

El orden de ejecución **es obligatorio**, porque cada script depende de que la
estructura o los datos del anterior ya existan (ver `docs/steps-create-project-database.pdf`).

**Windows (PowerShell)** — PowerShell no admite `<` para redirigir un archivo a la
entrada estándar, por lo que se usa `Get-Content` junto con una función auxiliar:

```powershell
function Invoke-GlobGustersScript($Path) {
    Get-Content $Path | & "C:\xampp\mysql\bin\mariadb.exe" -u root -p -h 127.0.0.1 -P 3306 --default-character-set=utf8mb4
}

Invoke-GlobGustersScript "sql\mariadb\glob_gusters.sql"          # 1. Base de datos, tablas, constraints y trigger de negocio
Invoke-GlobGustersScript "sql\mariadb\glob_gusters_insert.sql"   # 2. Datos de prueba
Invoke-GlobGustersScript "sql\mariadb\commands\01_DDL.sql"       # 3. CREATE / ALTER / DROP de ejemplo
Invoke-GlobGustersScript "sql\mariadb\commands\02_DML.sql"       # 4. INSERT / UPDATE / DELETE de ejemplo
Invoke-GlobGustersScript "sql\mariadb\commands\03_DQL.sql"       # 5. SELECT / JOIN / GROUP BY de ejemplo
Invoke-GlobGustersScript "sql\mariadb\commands\04_VDL.sql"       # 6. CREATE VIEW / consulta / DROP VIEW de ejemplo
Invoke-GlobGustersScript "sql\mariadb\commands\05_DCL.sql"       # 7. CREATE USER / GRANT / REVOKE de ejemplo
Invoke-GlobGustersScript "sql\mariadb\commands\06_TCL.sql"       # 8. START TRANSACTION / SAVEPOINT / COMMIT / ROLLBACK
```

**macOS:**

```bash
run_mariadb() {
    /Applications/XAMPP/xamppfiles/bin/mariadb -u root -p -h 127.0.0.1 -P 3306 --default-character-set=utf8mb4 "$@"
}

run_mariadb < sql/mariadb/glob_gusters.sql          # 1. Base de datos, tablas, constraints y trigger de negocio
run_mariadb < sql/mariadb/glob_gusters_insert.sql   # 2. Datos de prueba
run_mariadb < sql/mariadb/commands/01_DDL.sql       # 3. CREATE / ALTER / DROP de ejemplo
run_mariadb < sql/mariadb/commands/02_DML.sql       # 4. INSERT / UPDATE / DELETE de ejemplo
run_mariadb < sql/mariadb/commands/03_DQL.sql       # 5. SELECT / JOIN / GROUP BY de ejemplo
run_mariadb < sql/mariadb/commands/04_VDL.sql       # 6. CREATE VIEW / consulta / DROP VIEW de ejemplo
run_mariadb < sql/mariadb/commands/05_DCL.sql       # 7. CREATE USER / GRANT / REVOKE de ejemplo
run_mariadb < sql/mariadb/commands/06_TCL.sql       # 8. START TRANSACTION / SAVEPOINT / COMMIT / ROLLBACK
```

**Linux:**

```bash
run_mariadb() {
    /opt/lampp/bin/mariadb -u root -p -h 127.0.0.1 -P 3306 --default-character-set=utf8mb4 "$@"
}

run_mariadb < sql/mariadb/glob_gusters.sql          # 1. Base de datos, tablas, constraints y trigger de negocio
run_mariadb < sql/mariadb/glob_gusters_insert.sql   # 2. Datos de prueba
run_mariadb < sql/mariadb/commands/01_DDL.sql       # 3. CREATE / ALTER / DROP de ejemplo
run_mariadb < sql/mariadb/commands/02_DML.sql       # 4. INSERT / UPDATE / DELETE de ejemplo
run_mariadb < sql/mariadb/commands/03_DQL.sql       # 5. SELECT / JOIN / GROUP BY de ejemplo
run_mariadb < sql/mariadb/commands/04_VDL.sql       # 6. CREATE VIEW / consulta / DROP VIEW de ejemplo
run_mariadb < sql/mariadb/commands/05_DCL.sql       # 7. CREATE USER / GRANT / REVOKE de ejemplo
run_mariadb < sql/mariadb/commands/06_TCL.sql       # 8. START TRANSACTION / SAVEPOINT / COMMIT / ROLLBACK
```

> Si prefieres usar `cmd.exe` en Windows en vez de PowerShell, la redirección `<`
> funciona igual que en macOS/Linux:
> `C:\xampp\mysql\bin\mariadb.exe -u root -p -h 127.0.0.1 -P 3306 --default-character-set=utf8mb4 < sql\mariadb\glob_gusters.sql`

#### Ejecución segura: se puede repetir y desordenar sin miedo

Todos los scripts del proyecto están diseñados para ejecutarse **varias veces y en
secuencias no lineales** sin generar errores ni datos duplicados:

- Toda `CREATE DATABASE`, `CREATE TABLE`, `CREATE TRIGGER`, `ADD COLUMN` y
  `CREATE INDEX` usa `IF [NOT] EXISTS`.
- `glob_gusters_insert.sql` localiza cada llave foránea por su nombre natural (país,
  título+año, DNI, etc.) en vez de un ID numérico fijo, y protege cada fila con
  `INSERT IGNORE` (tablas con `UNIQUE`) o `WHERE NOT EXISTS` (tablas sin `UNIQUE`
  natural, como `director`/`actor`, o con trigger de negocio, como `ejemplar_renta`).
- `02_DML.sql` y `06_TCL.sql` localizan sus registros por llave natural y verifican
  si el dato de ejemplo ya existe antes de insertarlo, para no acumular préstamos
  activos y terminar chocando con el trigger de máximo 4 ejemplares.
- `03_DQL.sql` y `04_VDL.sql` son de sólo lectura o usan `CREATE OR REPLACE VIEW`.
- `05_DCL.sql` usa `CREATE USER IF NOT EXISTS`; repetir el `GRANT`/`REVOKE` no falla.

Esto se validó ejecutando los 8 scripts tres veces seguidas sin recrear la base de
datos, y en una secuencia desordenada con repeticiones (`05 → 01 → 05 → insert →
06 → 06 → 02 → 02 → glob_gusters.sql → 04 → 03`): en ambos casos, cero errores y los
mismos conteos de filas en todas las tablas.

### 4. Verificar la instalación desde phpMyAdmin (opcional)

1. Abre `http://localhost/phpmyadmin` con XAMPP en ejecución.
2. Selecciona la base de datos `glob_gusters` en el panel izquierdo.
3. Confirma que existan las 11 tablas del modelo, las vistas `v_ejemplares_detalle` y
   `v_clientes_con_aval`, y que la pestaña **Triggers** muestre los cuatro disparadores
   de reglas de negocio:
   - `trg_ejemplar_renta_max_4` y `trg_ejemplar_renta_max_4_update` (en
     `ejemplar_renta`): máximo 4 ejemplares sin devolver por socio.
   - `trg_cliente_aval_diferente_insert` y `trg_cliente_aval_diferente_update` (en
     `cliente`): un socio no puede ser su propio aval.

## Configuración de la conexión (`.env`)

Python y Java leen los datos de conexión de variables de entorno. Para no escribirlas en
la terminal cada vez, ambos cargan automáticamente el archivo `.env` de la **raíz del
proyecto**. Ese archivo es local y está en `.gitignore`, así que tu contraseña no se
sube a GitHub; la plantilla versionada es `.env.example`:

```bash
cp .env.example .env      # y edita GLOB_GUSTERS_PASSWORD si tu root tiene contraseña
```

| Variable | Valor por defecto | Uso |
|---|---|---|
| `GLOB_GUSTERS_HOST` | `localhost` | Servidor MariaDB. |
| `GLOB_GUSTERS_PORT` | `3306` | Puerto de conexión. |
| `GLOB_GUSTERS_USER` | `root` | Usuario. |
| `GLOB_GUSTERS_PASSWORD` | *(vacía)* | Contraseña del usuario. |
| `GLOB_GUSTERS_DB` | `glob_gusters` | Base de datos. |
| `GLOB_GUSTERS_PASS_REPORTES` | `Reportes#2024` | Clave de la cuenta de ejemplo que crean `dcl.py` / `Dcl`. |
| `GLOB_GUSTERS_PASS_MOSTRADOR` | `Mostrador#2024` | Ídem para la cuenta de mostrador. |

Formato: una línea `CLAVE=valor` por variable; se ignoran las líneas vacías y las que
empiezan con `#`. Una variable ya definida en el sistema (`export GLOB_GUSTERS_PORT=...`)
tiene prioridad sobre el `.env`. Si no hay `.env`, se usan los valores por defecto.

## Conexión y consultas desde Python

La carpeta `py/` conecta la base `glob_gusters` a Python y reproduce, con los mismos
datos de ejemplo, cada grupo de comandos SQL de `sql/mariadb/commands/`. La conexión
equivale a `mysql -u root -p -h localhost -P 3306 -D glob_gusters`.

**Requisitos:** Python 3.9+ y el servidor MariaDB de XAMPP en ejecución, con la base ya
creada (pasos 1 a 3 de la sección anterior).

```bash
python3 -m venv .venv                # crea el entorno virtual (una sola vez; .venv/ no se versiona)
source .venv/bin/activate            # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python3 py/conexion.py     # prueba de conexión: versión, base y cuenta (en Windows: python)
```

Los valores por defecto son los de XAMPP (`localhost`, `3306`, `root` sin contraseña,
base `glob_gusters`). Se pueden cambiar sin editar el código con las variables de entorno
`GLOB_GUSTERS_HOST`, `GLOB_GUSTERS_PORT`, `GLOB_GUSTERS_USER`, `GLOB_GUSTERS_PASSWORD` y
`GLOB_GUSTERS_DB`. `dcl.py` también acepta `GLOB_GUSTERS_PASS_REPORTES` y
`GLOB_GUSTERS_PASS_MOSTRADOR` para las contraseñas de las cuentas de ejemplo.

| Script | Equivale a | Qué hace |
|---|---|---|
| `py/ddl.py` | `01_DDL.sql` | CREATE / ALTER / CREATE INDEX / DROP con `IF [NOT] EXISTS`. |
| `py/dml.py` | `02_DML.sql` | INSERT / UPDATE / DELETE con parámetros y llaves naturales. |
| `py/dql.py` | `03_DQL.sql` | SELECT, JOIN y GROUP BY; `python3 py/dql.py <nombre>` (macOS/Linux; en Windows `python`) ejecuta una sola consulta. |
| `py/vdl.py` | `04_VDL.sql` | Crea y consulta las dos vistas; `--drop` las elimina. |
| `py/dcl.py` | `05_DCL.sql` | CREATE USER / GRANT / REVOKE / SHOW GRANTS (requiere cuenta administrativa). |
| `py/tcl.py` | `06_TCL.sql` | Transacción con SAVEPOINT y COMMIT, y otra descartada con ROLLBACK. |

`py/conexion_mariabd.py` es un ejemplo aparte, mínimo, con el conector oficial `mariadb`
(`mariadb` está en `requirements.txt`, pero necesita instalar antes en el sistema MariaDB Connector/C ≥ 3.3.1 —en macOS `brew install mariadb-connector-c`; el de XAMPP es más antiguo—): lista la tabla `nacionalidad`.
Tiene el usuario, la clave y el puerto escritos en el código; edítalos si tu servidor difiere.

Se ejecutan en el mismo orden que los scripts SQL (`ddl` → `dml` → `dql` → `vdl` →
`dcl` → `tcl`) y, como ellos, se pueden repetir sin errores ni datos duplicados. Las
sentencias usan parámetros (`%s`) y nunca concatenan valores dentro del SQL.

## Conexión y consultas desde Java

La carpeta `java/` hace lo mismo que `py/` pero con **JDBC**: una clase `Conexion` y un
programa por grupo de comandos SQL. La conexión equivale a
`mysql -u root -p -h localhost -P 3306 -D glob_gusters`.

**Requisitos:** JDK 17 o superior (usa *text blocks* y `record`) y el servidor MariaDB
de XAMPP en ejecución, con la base ya creada (pasos 1 a 3 de arriba). El driver
[MariaDB Connector/J](https://mariadb.com/kb/en/about-mariadb-connector-j/) no se
versiona; se descarga a `java/lib/`:

```bash
cd java
mkdir -p lib
curl -L -o lib/mariadb-java-client-3.5.3.jar \
  https://repo1.maven.org/maven2/org/mariadb/jdbc/mariadb-java-client/3.5.3/mariadb-java-client-3.5.3.jar
javac -encoding UTF-8 -d out *.java
java -cp "out:lib/*" Conexion      # prueba de conexión: versión, base y cuenta
```

En Windows el separador del *classpath* es `;`: `java -cp "out;lib/*" Conexion`.

Los valores por defecto son los de XAMPP (`localhost`, `3306`, `root` sin contraseña,
base `glob_gusters`) y se cambian con las mismas variables de entorno de Python:
`GLOB_GUSTERS_HOST`, `GLOB_GUSTERS_PORT`, `GLOB_GUSTERS_USER`,
`GLOB_GUSTERS_PASSWORD` y `GLOB_GUSTERS_DB`. `Dcl` también acepta
`GLOB_GUSTERS_PASS_REPORTES` y `GLOB_GUSTERS_PASS_MOSTRADOR`.

| Clase | Equivale a | Qué hace |
|---|---|---|
| `Ddl` | `01_DDL.sql` | CREATE / ALTER / CREATE INDEX / DROP con `IF [NOT] EXISTS`. |
| `Dml` | `02_DML.sql` | INSERT / UPDATE / DELETE con parámetros y llaves naturales. |
| `Dql` | `03_DQL.sql` | SELECT, JOIN y GROUP BY; `java -cp "out:lib/*" Dql <nombre>` ejecuta una sola consulta. |
| `Vdl` | `04_VDL.sql` | Crea y consulta las dos vistas; `--drop` las elimina. |
| `Dcl` | `05_DCL.sql` | CREATE USER / GRANT / REVOKE / SHOW GRANTS (requiere cuenta administrativa). |
| `Tcl` | `06_TCL.sql` | Transacción con SAVEPOINT y COMMIT, y otra descartada con ROLLBACK. |

Se ejecutan en el mismo orden que los scripts SQL (`Ddl` → `Dml` → `Dql` → `Vdl` →
`Dcl` → `Tcl`) y, como ellos, se pueden repetir sin errores ni datos duplicados. Las
sentencias usan parámetros (`?`) con `PreparedStatement` y nunca concatenan valores
dentro del SQL.

## Documentación detallada de cada archivo

Esta sección describe, archivo por archivo, qué hace cada uno y qué hace cada línea o
bloque de código. Los números de línea se evitan a propósito (cambian al editar): cada
elemento se identifica por su nombre, que se puede buscar en el archivo. Los propios
archivos de código también llevan comentarios línea por línea.

Todos los scripts de `sql/mariadb/` comienzan (tras su encabezado) con `SET NAMES
utf8mb4;`, que fija la codificación de la sesión para las tildes y la `ñ`; no se repite
en cada tabla de descripciones. Ver [Tildes y `ñ` en la terminal](#tildes-y-ñ-en-la-terminal).

Índice: [raíz](#archivos-de-la-raíz) ·
[docs/](#carpeta-docs) ·
[sql/mariadb/](#carpeta-sqlmariadb) ·
[py/](#carpeta-py) ·
[java/](#carpeta-java) ·
[shell/](#scripts-de-shell-shell) ·
[flujo completo](#flujo-completo-de-ejecución-y-dependencias-entre-archivos)

### Archivos de la raíz

#### `.env.example` — plantilla de configuración

Archivo de ejemplo que se versiona. Sirve como plantilla: se copia a `.env` y se edita.
Todas las líneas que empiezan con `#` son comentarios; las demás son `CLAVE=valor`.

| Línea | Qué hace |
|---|---|
| Encabezado `# ====` | Explica que es un archivo de configuración de ejemplo/plantilla, cómo copiarlo (`cp .env.example .env`), quién lo lee, las reglas de formato y la prioridad de los valores (sistema > `.env` > valor por defecto del código). |
| `GLOB_GUSTERS_HOST=localhost` | Servidor de MariaDB. |
| `GLOB_GUSTERS_PORT=3306` | Puerto TCP de MariaDB (3306 es el de XAMPP). |
| `GLOB_GUSTERS_USER=root` | Usuario de la conexión; `root` es necesario para `dcl.py`/`Dcl.java`. |
| `GLOB_GUSTERS_PASSWORD=` | Contraseña; vacía = sin contraseña (valor de XAMPP). |
| `GLOB_GUSTERS_DB=glob_gusters` | Base de datos a la que se conecta. |
| `GLOB_GUSTERS_PASS_REPORTES=Reportes#2024` | Contraseña con la que se crea la cuenta `glob_gusters_reportes`. |
| `GLOB_GUSTERS_PASS_MOSTRADOR=Mostrador#2024` | Contraseña con la que se crea la cuenta `glob_gusters_mostrador`. |

#### `.env` — configuración real y local

Misma estructura y mismos valores que `.env.example`, pero es el archivo que realmente
leen `py/conexion.py` y `java/Conexion.java`. Está en `.gitignore`, así que no se sube a
Git: es el lugar para escribir contraseñas reales. Cada variable tiene el mismo
significado que en la tabla anterior.

#### `.gitignore` — archivos que Git no versiona

| Sección | Patrones | Qué excluye |
|---|---|---|
| Configuración y secretos | `.env`, `.env.*`, `!.env.example` | Variables reales de conexión; la excepción `!` mantiene versionada la plantilla. |
| Registros | `*.log`, `/logs/` | Bitácoras de ejecución. |
| SQL / MariaDB / XAMPP / Oracle | `*.ibd`, `*.frm`, `*.err`, `*.pid`, `ib_logfile*`, `ibdata*` | Archivos de datos que genera el servidor. |
| | `.mysql_history`, `.mariadb_history`, `.sqlplus_history` | Historiales de los clientes de consola. |
| | `*.dump`, `*.sql.gz`, `*.sql.zip`, `*.sql.bak` | Volcados y respaldos locales. |
| | `*.lst`, `*.trc`, `*.mwb.bak`, `*.mwbhistory/` | Temporales de Oracle y MySQL Workbench. |
| Python | `.venv/`, `venv/`, `env/` | Entorno virtual. |
| | `__pycache__/`, `*.py[cod]`, `*$py.class` | Código compilado. |
| | `.pytest_cache/`, `.mypy_cache/`, `.ruff_cache/`, `.cache/`, `.coverage`, `htmlcov/` | Cachés y cobertura. |
| | `build/`, `dist/`, `*.egg-info/`, `*.egg`, `pip-log.txt`, `pip-delete-this-directory.txt`, `.ipynb_checkpoints/` | Empaquetado, logs de pip y Jupyter. |
| Java | `java/out/`, `java/bin/`, `java/target/`, `java/build/`, `*.class` | Clases compiladas. |
| | `*.jar`, `*.war`, `*.ear`, `hs_err_pid*`, `replay_pid*` | Empaquetados y volcados de error de la JVM. |
| | `java/lib/` | Driver JDBC descargado (no se versiona). |
| | `.gradle/`, `.mvn/wrapper/maven-wrapper.jar`, `.idea/`, `*.iml`, `.classpath`, `.project`, `.settings/`, `.factorypath`, `nbproject/` | Gradle/Maven y configuración de IDEs. |
| Editores | `.vscode/`, `*.code-workspace` | Configuración de Visual Studio Code. |
| Sistema y temporales | `Thumbs.db`, `.DS_Store`, `*.bak`, `*.tmp`, `*.swp` | Basura del sistema operativo y de editores. |

#### `requirements.txt` — dependencias de Python

| Línea | Qué hace |
|---|---|
| Bloque de comentarios | Explica cómo crear el entorno virtual e instalar (`python3 -m venv .venv`, `source .venv/bin/activate`, `pip install -r requirements.txt`). |
| `PyMySQL>=1.1` | Conector MySQL/MariaDB en Python puro; lo usa `py/conexion.py` y, a través de él, todos los scripts de `py/`. |
| `mariadb>=1.1` | Conector oficial, solo para `py/conexion_mariabd.py`. Requiere MariaDB Connector/C ≥ 3.3.1 instalado en el sistema (no es un paquete de pip; en macOS `brew install mariadb-connector-c`); el de XAMPP (3.1.x) es más antiguo. Los comentarios del archivo explican cómo instalarlo; si no se necesita, se puede comentar la línea. |

#### `LICENSE`

Texto de la licencia MIT del proyecto: permite usar, copiar, modificar y distribuir el
software conservando el aviso de copyright, sin garantía.

#### `README.md`

Este documento: descripción del ejercicio, modelo de datos, reglas de negocio,
instrucciones de ejecución en Windows/macOS/Linux, configuración del `.env`, uso desde
Python y Java, y esta documentación por archivo.

### Carpeta `docs/`

Documentos de apoyo en PDF/imagen (no contienen código):

| Archivo | Contenido |
|---|---|
| `MER.pdf` / `MER.png` | Modelo Entidad-Relación del proyecto (el PNG es la misma imagen para verla sin visor de PDF). |
| `glob_gusters_diccionario.pdf` | Diccionario de datos: tablas, columnas, tipos y llaves. |
| `relational-database.pdf` | Taller resuelto: enunciado e identificación de entidades, relaciones N-M, campos multivaluados y llaves. |
| `sql_scripts_commands.pdf` | Resumen de los grupos de comandos SQL (DDL/DML/DQL/VDL/DCL/TCL) en que se basan los scripts `01` a `06`. |
| `steps-create-project-database.pdf` | Orden de ejecución recomendado de los scripts. |

### Carpeta `sql/mariadb/`

#### `glob_gusters.sql` — esquema completo (DDL)

Crea la base de datos, las 11 tablas, las restricciones y los 4 triggers. Es idempotente:
tablas y triggers del aval usan `IF NOT EXISTS`; los triggers del límite de 4 usan
`CREATE OR REPLACE TRIGGER`, así una base ya creada recibe su versión actual.

| Bloque | Qué hace |
|---|---|
| Encabezado | Autor, fecha, motor y explicación de la normalización: 1FN (atributos atómicos; `nacionalidad`, `productora` y `estado` salen como catálogos), 2FN (las llaves compuestas de `reparto` y `ejemplar_renta` se sustituyen por llave subrogada y la combinación pasa a `UNIQUE`) y 3FN (sin dependencias transitivas). |
| `CREATE DATABASE IF NOT EXISTS glob_gusters ... utf8mb4 / utf8mb4_general_ci` | Crea la base con soporte completo de UTF-8. |
| `-- DROP DATABASE ...` (comentada) | Borrado completo, comentado por seguridad. |
| `USE glob_gusters` | Selecciona el esquema para las sentencias siguientes. |
| Tabla de comentarios de relaciones | Lista cada FK: tabla origen, campo, tabla destino, campo y cardinalidad. |
| `nacionalidad` | `Nacionalidad_ID` (PK autoincremental), `Nombre` VARCHAR(60) con `UNIQUE`. |
| `productora` | `Productora_ID`, `Nombre` VARCHAR(100) con `UNIQUE`. |
| `estado` | `Estado_ID`, `Nombre` VARCHAR(30) con `UNIQUE` (Nuevo, Bueno, Regular, Dañado). |
| `director` | `Director_ID`, `Nombre`, `Nacionalidad_ID` → `nacionalidad` (`ON UPDATE CASCADE ON DELETE RESTRICT`). |
| `pelicula` | `Pelicula_ID`, `Titulo`, `Anio` (tipo `YEAR`), FK a `nacionalidad`, `productora` y `director` (todas `RESTRICT` al borrar); `UNIQUE (Titulo, Anio)`. |
| `actor` | `Actor_ID`, `Nombre`, `Nacionalidad_ID`, `Sexo ENUM('M','F')`. |
| `reparto` | Tabla puente película↔actor: `Reparto_ID`, `Pelicula_ID`, `Actor_ID`, `Rol ENUM('Principal','Secundario')`; `UNIQUE (Pelicula_ID, Actor_ID)`; FK con `ON DELETE CASCADE`. |
| `cliente` | `Cliente_ID`, `Dni` (`UNIQUE`), `Nombre`, `Direccion`, `Telefono` VARCHAR(20), `Aval_Cliente_ID` (nulo) con FK a `cliente` (autorreferencia, `RESTRICT`). El comentario explica por qué "no ser su propio aval" no es un `CHECK`: MariaDB prohíbe usar una columna `AUTO_INCREMENT` en un `CHECK`. |
| `ejemplar` | `Ejemplar_ID`, `Numero`, `Pelicula_ID` (`CASCADE`), `Estado_ID` (`RESTRICT`); `UNIQUE (Pelicula_ID, Numero)`. |
| `renta` | `Renta_ID`, `Cliente_ID` (`RESTRICT`), `Inicia` DATE, `Termina` DATE nulo; `CHECK chk_renta_fechas (Termina IS NULL OR Termina >= Inicia)`. |
| `ejemplar_renta` | Tabla puente renta↔ejemplar: `Ejemplar_Renta_ID`, `Renta_ID` (`CASCADE`), `Ejemplar_ID` (`RESTRICT`), `Entrega` DATE nulo (nulo = aún sin devolver); `UNIQUE (Renta_ID, Ejemplar_ID)`. |
| `DELIMITER $$ ... DELIMITER ;` | Cambia temporalmente el delimitador para poder escribir `;` dentro del cuerpo de un trigger. |
| `trg_cliente_aval_diferente_insert` / `_update` | `BEFORE INSERT/UPDATE` en `cliente`: si `Aval_Cliente_ID` no es nulo e igual a `Cliente_ID`, lanza `SIGNAL SQLSTATE '45000'` con el mensaje «Un cliente no puede ser su propio aval.» |
| `trg_ejemplar_renta_max_4` | `BEFORE INSERT` en `ejemplar_renta`: declara `ejemplares_activos`, cuenta con un `SELECT COUNT(*) INTO` los ejemplares con `Entrega IS NULL` de todas las rentas del cliente dueño de la renta nueva, y si ya son 4 o más lanza `SIGNAL` con «El cliente ya tiene 4 ejemplares alquilados sin devolver.» |

#### `glob_gusters_insert.sql` — datos de prueba (DML)

Inserta datos ficticios respetando el orden de las llaves foráneas. Es repetible: las FK
se resuelven con subconsultas por llave natural (nombre, título+año, DNI), nunca con IDs
fijos. Tablas con `UNIQUE` usan `INSERT IGNORE`; `director`, `actor`, `renta` y
`ejemplar_renta` usan `INSERT ... SELECT ... FROM DUAL WHERE NOT EXISTS` (en las dos
últimas porque `IGNORE` no evita que el trigger se dispare).

| Bloque | Datos que carga |
|---|---|
| `nacionalidad` | Estados Unidos, España, Reino Unido, Francia, México. |
| `productora` | M.G.M., Warner Bros., Universal Pictures, El Deseo. |
| `estado` | Nuevo, Bueno, Regular, Dañado. |
| `director` | Mervyn LeRoy (EE. UU.), Pedro Almodóvar (España), Christopher Nolan (Reino Unido), Luc Besson (Francia). |
| `pelicula` | Quo Vadis (1951), Todo sobre mi madre (1999), Interstellar (2014), El quinto elemento (1997), cada una con su nacionalidad, productora y director. |
| `actor` | Robert Taylor, Deborah Kerr, Cecilia Roth, Matthew McConaughey, Anne Hathaway, Milla Jovovich. |
| `reparto` | 6 filas: Taylor y Kerr (Quo Vadis, Principal), Roth (Todo sobre mi madre), McConaughey (Interstellar, Principal), Hathaway (Interstellar, Secundario), Jovovich (El quinto elemento). |
| `cliente` | 4 socios: Laura Gómez (`1000000001`, sin aval, socia fundadora), Carlos Pérez (`…02`, avalado por Laura), María Rodríguez (`…03`, avalada por Laura) y Andrés Torres (`…04`, avalado por Carlos). El aval se envuelve en una tabla derivada para evitar el `ERROR 1093`. |
| `ejemplar` | 6 copias: Quo Vadis #1 (Bueno) y #2 (Regular), Todo sobre mi madre #1 (Nuevo), Interstellar #1 (Nuevo) y #2 (Bueno), El quinto elemento #1 (Bueno). |
| `renta` | 3 rentas: Laura (2024-05-01, abierta), Carlos (2024-05-02 a 2024-05-05) y María (2024-05-03, abierta). |
| `ejemplar_renta` | 4 renglones: Laura se lleva Quo Vadis #1 e Interstellar #1 (sin devolver), Carlos Todo sobre mi madre #1 (devuelto el 2024-05-05) y María El quinto elemento #1 (sin devolver). |

> Los conteos de la tabla «Datos de prueba» de arriba (5 clientes, 5 en `reparto`, 4
> rentas, 5 en `ejemplar_renta`) corresponden al estado final tras ejecutar también
> `02_DML.sql` (agrega un socio y borra un reparto) y `06_TCL.sql` (agrega una renta con su
> ejemplar).

#### `check-mariadb.sql` — diagnóstico del servidor (solo lectura)

Todo son `SELECT`/`SHOW`: no modifica nada. Por defecto solo imprime la verificación de
la conexión y sus parámetros (versión, host, puerto, cuenta, base seleccionada, id de
conexión y juego de caracteres de la sesión); el diagnóstico completo sigue en el archivo,
comentado con `/* ... */`, y se reactiva quitando esos marcadores. Se ejecuta con `--force` porque algunas
secciones pueden fallar por limitaciones del entorno (descritas en su encabezado: base
inexistente, `event_scheduler` apagado y `mysql.proc` desactualizada).

| Sección | Sentencias | Qué muestra |
|---|---|---|
| 1. Identidad y versión | `SELECT VERSION()`; `SELECT @@version, @@version_comment, @@version_compile_machine, @@version_compile_os`; `SELECT @@hostname`; `SHOW VARIABLES LIKE 'port'` | Versión, compilación, host y puerto. |
| 2. Sesión | `SELECT CURRENT_USER()`; `SELECT DATABASE()`; `SHOW PROCESSLIST` | Cuenta autenticada, base activa y procesos. |
| 3. Estado | `SHOW STATUS LIKE 'Uptime'`, `'Threads_connected'`, `'Questions'`; `SHOW STATUS` | Tiempo encendido, clientes conectados, consultas atendidas y el estado completo. |
| 4. Configuración | `SHOW VARIABLES LIKE 'character_set%'`, `'collation%'`, `'sql_mode'`; `SHOW VARIABLES` | Juegos de caracteres, collations y modo SQL. |
| 5. Motores | `SHOW ENGINES` | Confirma que InnoDB está disponible. |
| 6. Usuarios | `SELECT host, user, plugin FROM mysql.user` | Cuentas sin exponer el hash de contraseña. |
| 7. Objetos del proyecto | `SHOW TABLES`, `SHOW FULL TABLES ... WHERE Table_type = 'VIEW'`, `SHOW TRIGGERS` y `SHOW EVENTS`, todos con `FROM` la base `@db` (armados con `CONCAT` y ejecutados con `PREPARE`/`EXECUTE`, porque `USE` no admite parámetros) | Tablas, vistas, triggers y eventos (se espera lista vacía). |
| 8. Estado del proyecto | consulta a `information_schema.schemata` y a `information_schema.tables`, filtradas por `@db` | Existencia de la base y filas aproximadas/tamaño en KB por tabla. |
| 9. Rutinas | `SHOW PROCEDURE STATUS`; `SHOW FUNCTION STATUS`; `SELECT * FROM information_schema.routines LIMIT 10` | Procedimientos y funciones (el proyecto no define ninguno). |

Al inicio ejecuta `SET @db = COALESCE(@glob_gusters_db, 'glob_gusters')`: el nombre de la
base sale de `@glob_gusters_db` (que define el lanzador a partir de `GLOB_GUSTERS_DB`) o,
si no existe, es `glob_gusters`.

#### `check-mariadb.sh` — lanzador con la configuración del `.env`

Script `sh` que ejecuta `check-mariadb.sql` con los datos de conexión del proyecto.

| Elemento | Qué hace |
|---|---|
| `RAIZ`, `ENV_ARCHIVO` | Calcula la raíz del proyecto desde la ubicación del script (funciona desde cualquier carpeta) y la ruta del `.env`. |
| `leer CLAVE DEFECTO` | Busca `CLAVE=valor` en el `.env` con `sed` (admite `export ` y comillas) y devuelve la última coincidencia o el valor por defecto. No usa `source` ni `eval`, así que no ejecuta nada del archivo. |
| `HOST`, `PORT`, `USUARIO`, `CLAVE`, `BASE` | Resuelven cada variable con la prioridad sistema > `.env` > defecto (`localhost`, `3306`, `root`, vacía, `glob_gusters`). |
| `[ "$HOST" = "localhost" ] && HOST=127.0.0.1` | Fuerza TCP: con `localhost` el cliente usaría el socket Unix, que puede ser de otro servidor, e ignoraría el puerto. |
| Búsqueda de `CLIENTE` | Usa `MARIADB_BIN` si está definida; si no, `mariadb` del `PATH`, las rutas de XAMPP en macOS/Linux o `mysql`. Sale con error si no encuentra ninguno. |
| `MYSQL_PWD` | Pasa la contraseña por variable de entorno (no aparece en la lista de procesos); si está vacía no se define y se conecta sin contraseña. |
| `BASE_SQL` | Escapa barras y comillas simples del nombre de la base para el literal SQL. |
| `exec "$CLIENTE" ... --force --init-command="SET @glob_gusters_db = '...'" < check-mariadb.sql` | Ejecuta el cliente con `--force` (las secciones que fallan por limitaciones conocidas no detienen el reporte), define `@glob_gusters_db` al conectar y envía el script SQL por la entrada estándar. |

#### `commands/01_DDL.sql` a `06_TCL.sql` — ejemplos por grupo de comandos SQL

Se ejecutan en orden después del esquema y de los datos. Todos son repetibles.

| Archivo | Sentencias, en orden | Qué hace |
|---|---|---|
| `01_DDL.sql` | `USE`; `CREATE TABLE IF NOT EXISTS tabla_prueba`; `ALTER TABLE cliente ADD COLUMN IF NOT EXISTS Email VARCHAR(120)`; `ALTER TABLE pelicula ADD COLUMN IF NOT EXISTS Duracion_Minutos SMALLINT UNSIGNED`; `ALTER TABLE cliente MODIFY COLUMN Telefono VARCHAR(25)`; `CREATE INDEX IF NOT EXISTS idx_pelicula_titulo`; `DROP TABLE IF EXISTS tabla_prueba` | Crea una tabla de prueba, agrega las columnas `Email` y `Duracion_Minutos`, amplía el teléfono, crea un índice por título y elimina la tabla de prueba. |
| `02_DML.sql` | `INSERT IGNORE INTO cliente` (Sofía Ramírez, DNI `1000000005`, avalada por Laura, con email); `UPDATE ejemplar` (Quo Vadis #2 pasa a «Dañado»); `UPDATE pelicula` (Interstellar dura 169 min); `DELETE r FROM reparto` (quita a Anne Hathaway de Interstellar) | Muestra INSERT, UPDATE y DELETE localizando registros por llave natural. |
| `03_DQL.sql` | 4 `SELECT` | (1) ejemplares disponibles (sin `Entrega` pendiente); (2) rentas activas con `JOIN` de 5 tablas; (3) películas por nacionalidad con `GROUP BY`; (4) ejemplares por estado con `GROUP BY`. Solo lectura. |
| `04_VDL.sql` | `CREATE OR REPLACE VIEW v_ejemplares_detalle` + su `SELECT`; `CREATE OR REPLACE VIEW v_clientes_con_aval` + su `SELECT`; dos `DROP VIEW IF EXISTS` comentados | Crea y consulta las dos vistas (la segunda con `LEFT JOIN` para conservar a los socios sin aval). |
| `05_DCL.sql` | `CREATE USER IF NOT EXISTS glob_gusters_reportes`; `GRANT SELECT`; `CREATE USER IF NOT EXISTS glob_gusters_mostrador`; `GRANT SELECT, INSERT, UPDATE`; `REVOKE DELETE`; `FLUSH PRIVILEGES`; dos `SHOW GRANTS` | Crea las dos cuentas de ejemplo, les concede permisos, revoca el borrado al mostrador y muestra los permisos resultantes. Requiere `root`. |
| `06_TCL.sql` | `SET @cliente_demo_tcl`, `@ejemplar_demo_tcl`, `@ya_existe_tcl`; `START TRANSACTION`; `INSERT INTO renta ... WHERE NOT @ya_existe_tcl`; `SAVEPOINT sp_renta_creada`; `INSERT INTO ejemplar_renta ... LAST_INSERT_ID()`; `COMMIT`; segunda transacción con `UPDATE cliente` y `ROLLBACK` | Registra una renta con su detalle de forma atómica (omitida si ya existe) y demuestra un `ROLLBACK` que no deja efectos. El `ROLLBACK TO SAVEPOINT` queda como ejemplo comentado. |

| 11 `CREATE TABLE` | Mismas tablas y relaciones que en MariaDB. Diferencias: `pelicula.anio` lleva `CHECK (anio BETWEEN 1888 AND 2100)`; `actor.sexo` y `reparto.rol` llevan `CHECK ... IN`; `cliente` lleva `chk_cliente_aval (aval_cliente_id IS NULL OR aval_cliente_id <> cliente_id)`; `ejemplar.numero` lleva `CHECK (numero >= 0)`; `renta` lleva `chk_renta_fechas`. |
| 10 `CREATE INDEX ix_...` | Oracle no indexa las llaves foráneas automáticamente; se crean índices sobre las FK que lo necesitan. |
| 11 `COMMENT ON TABLE` | Descripción de cada tabla en el diccionario de datos. |
| `trg_ejemplar_renta_max_4` | `COMPOUND TRIGGER ... FOR INSERT OR UPDATE OF entrega, renta_id ON ejemplar_renta`: en `AFTER EACH ROW` guarda en una colección (`g_renta_ids`) las rentas de los renglones que quedan sin devolver (`entrega` nula); en `AFTER STATEMENT` recorre esa colección, obtiene el cliente de cada renta, cuenta sus ejemplares con `entrega IS NULL` y, si son más de 4, lanza `RAISE_APPLICATION_ERROR(-20001, ...)`. Se hace así para evitar el error ORA-04091 (tabla mutante). |
| Verificación (comentada) | Dos consultas para comprobar que hay 11 tablas y el trigger en estado `VALID`. |

### Carpeta `py/`

Todos los scripts usan PyMySQL a través de `conexion.py`, con consultas parametrizadas
(`%s`). Se ejecutan desde la raíz con el entorno virtual instalado y activado, por ejemplo
`python3 py/ddl.py` en macOS y Linux (`python py\ddl.py` en Windows).

#### `conexion.py` — módulo base

| Elemento | Qué hace |
|---|---|
| Docstring | Explica el módulo, el comando equivalente de consola y las variables de entorno. |
| `_salida_utf8()` | Se ejecuta al importar el módulo: fuerza UTF-8 (`reconfigure(encoding="utf-8", errors="replace")`) en `stdout` y `stderr` para que las tildes y la `ñ` salgan bien aunque la salida se redirija. Cubre todos los scripts de `py/`. |
| `principal(funcion, *args)` | Ejecuta `funcion(*args)` (todos los scripts de `py/` la usan en su bloque `__main__`). Si el servidor informa una tabla dañada (errores 1030, 144, 145, 1194, 1195) termina con los pasos de reparación (`explicar_tabla_danada`) en lugar del traceback; cualquier otro error se propaga igual. |
| `import os`, `sys`, `contextmanager`, `Path`, `pymysql`, `DictCursor` | Variables de entorno, bloques `with`, rutas portables, el conector y el cursor que devuelve diccionarios. |
| `_cargar_env(ruta)` | Si el `.env` existe, lo lee línea por línea; ignora vacías, comentarios y líneas sin `=`; quita el prefijo `export `; separa en el primer `=`; y usa `os.environ.setdefault` para no pisar variables ya definidas en el sistema (quita comillas del valor). |
| `_cargar_env(Path(__file__)...parent.parent / ".env")` | La ejecuta al importar el módulo, apuntando al `.env` de la raíz. |
| `CONFIG` | Diccionario de parámetros: `host` (`localhost`), `port` (entero, `3306`), `user` (`root`), `password` (vacía por defecto), `database` (`glob_gusters`), `charset` `utf8mb4` y `cursorclass` `DictCursor`. |
| `conectar(**cambios)` | Mezcla `CONFIG` con los cambios; normaliza la contraseña `None` a `""`; abre la conexión con `autocommit=False` y la bandera `CLIENT.FOUND_ROWS`, para que un `UPDATE` informe las filas que coinciden con el `WHERE` (igual que el driver JDBC de Java y el cliente de MariaDB) y las salidas de Python y Java sean idénticas. Ante `OperationalError` 1045 (acceso denegado) sale sin traza con un mensaje que indica usuario, host y puerto: «sin contraseña» (apunta a `GLOB_GUSTERS_PASSWORD` del `.env`) si no se envió clave, o «el usuario o la contraseña son incorrectos» (apunta a `GLOB_GUSTERS_USER` y `GLOB_GUSTERS_PASSWORD`) si se envió; nunca imprime la contraseña. Ante 1049 (base inexistente) sale pidiendo ejecutar los SQL de creación; cualquier otro error se relanza. |
| `conexion(**cambios)` | Context manager: entrega la conexión con `yield` y la cierra en `finally`. |
| `consultar(con, sql, params)` | Ejecuta un `SELECT`/`SHOW` y devuelve todas las filas como lista de diccionarios. |
| `ejecutar(con, sql, params)` | Ejecuta una escritura sin hacer commit y devuelve las filas afectadas. |
| `imprimir(titulo, filas)` | Imprime una tabla de texto: título, columnas de la primera fila, ancho de cada columna (el mayor entre nombre y valores), encabezado, separador `-+-` y filas; avisa «(sin filas)» si está vacío. |
| `if __name__ == "__main__"` | Prueba rápida: muestra versión del servidor, base y cuenta. |

#### `conexion_mariabd.py`

Ejemplo mínimo con el conector oficial `mariadb`. Importa `CONFIG` de `conexion.py` (que
lee el `.env`), por lo que usuario, contraseña, host, puerto y base salen de las variables
`GLOB_GUSTERS_*` y no hay valores escritos en el código; convierte `localhost` en `127.0.0.1`
para conectar por TCP, abre la conexión con `mariadb.connect(...)` (si falla imprime el error y
sale con código 1), crea un cursor, ejecuta `SELECT * FROM nacionalidad`, imprime
`ID` y `Nombre` de cada fila y cierra cursor y conexión.

#### `ddl.py`, `dml.py`, `dql.py`, `vdl.py`, `dcl.py`, `tcl.py`

| Archivo | Equivale a | Estructura y funcionamiento |
|---|---|---|
| `ddl.py` | `01_DDL.sql` | La lista `SENTENCIAS` contiene el mismo DDL del `.sql`. `main()` abre la conexión, ejecuta cada sentencia imprimiendo `OK:` y los primeros 90 caracteres, hace `commit()` y consulta `information_schema.columns` para mostrar las columnas `Email`, `Telefono` y `Duracion_Minutos`. |
| `dml.py` | `02_DML.sql` | `main()` ejecuta con parámetros: `INSERT IGNORE` del socio nuevo (aval en tabla derivada), `UPDATE` del estado de Quo Vadis #2, `UPDATE` de la duración de Interstellar y `DELETE` del reparto de Anne Hathaway; imprime las filas afectadas de cada uno, hace `commit()` y muestra el socio nuevo. |
| `dql.py` | `03_DQL.sql` | El diccionario `CONSULTAS` mapea cuatro nombres (`disponibles`, `rentas_activas`, `peliculas_por_nacionalidad`, `ejemplares_por_estado`) a su título y SQL. `main(argv)` ejecuta todas o solo las nombradas; si alguna no existe sale con un mensaje y las opciones válidas. |
| `vdl.py` | `04_VDL.sql` | El diccionario `VISTAS` guarda, por vista, su `CREATE OR REPLACE VIEW` y su consulta de verificación. Con `--drop` ejecuta `DROP VIEW IF EXISTS` de ambas y termina; sin él crea y muestra cada vista. Siempre confirma con `commit()`. |
| `dcl.py` | `05_DCL.sql` | El diccionario `USUARIOS` lee las contraseñas de `GLOB_GUSTERS_PASS_*` (con los mismos valores por defecto). `main()` crea cada usuario con `CREATE USER IF NOT EXISTS ... IDENTIFIED BY %s`, concede sus privilegios, revoca `DELETE` al mostrador, ejecuta `FLUSH PRIVILEGES` y muestra `SHOW GRANTS` de cada cuenta. |
| `tcl.py` | `06_TCL.sql` | Busca el cliente por DNI y el ejemplar por título+año+número (sale con mensaje si faltan). Calcula `ya_existe`. Ejemplo 1: `con.begin()`; si no existe, inserta la renta, guarda `lastrowid`, crea `SAVEPOINT`, inserta el detalle y, si el trigger de máximo 4 lo rechaza, hace `ROLLBACK TO SAVEPOINT`; cualquier otro error hace `rollback()` y se relanza; luego `commit()`. Ejemplo 2: cambia una dirección, la lee, hace `rollback()` y la lee de nuevo para mostrar que se restauró. |

### Carpeta `java/`

Todas las clases están en el paquete por defecto y usan `Conexion`. Compilación y
ejecución: ver «Conexión y consultas desde Java».

#### `Conexion.java` — clase base

| Elemento | Qué hace |
|---|---|
| Imports y Javadoc | Entrada/salida de archivos, `java.sql.*` (JDBC) y colecciones; el Javadoc describe el comando equivalente y las variables. |
| `configurarSalida()` | Si la salida no va a una terminal, reemplaza `System.out` y `System.err` por `PrintStream` en UTF-8 (en una terminal respeta la codificación que el JDK eligió para la consola). Cada `main` la llama en su primera línea. `esTerminal()` decide con `System.console()` y, en JDK 22+, con `Console.isTerminal()` por reflexión. |
| `correr(Principal)` | Ejecuta el programa; si el servidor informa una tabla dañada (mismos errores que en Python) imprime los pasos de reparación y sale con código 1; cualquier otro error se propaga igual. Cada `main` la usa (`Conexion.correr(() -> principal(args))`). |
| `ENV_ARCHIVO` | Mapa que se llena al iniciar la clase con `cargarEnv()`; se declara antes que las constantes que lo usan. |
| `HOST`, `PORT`, `USER`, `PASSWORD`, `DB` | Constantes de configuración obtenidas con `env(...)` (el puerto se convierte con `Integer.parseInt`). |
| `env(nombre, defecto)` | Devuelve primero la variable del sistema, luego la del `.env` y por último el valor por defecto. |
| `cargarEnv()` | Busca `.env` en el directorio actual y, si no está, en el padre; lee cada línea, ignora vacías/comentarios/sin `=`, quita `export ` de la clave y las comillas del valor, y usa solo el primer archivo encontrado. Si no puede leerlo, avisa por `stderr`. |
| `conectar()` / `conectar(usuario, clave)` | Arma la URL `jdbc:mariadb://host:puerto/base?characterEncoding=utf8`, abre la conexión y apaga el autocommit. Ante el error 1045 imprime en `stderr` el mismo mensaje que Python (sin contraseña / usuario o contraseña incorrectos, con usuario, host y puerto, sin mostrar la clave) y sale con código 1; el 1049 (base inexistente) imprime en `stderr` que hay que ejecutar primero `glob_gusters.sql` y `glob_gusters_insert.sql` y también sale con código 1; relanza los demás. (La línea `[ WARN]` que aparece antes es del propio driver JDBC.) |
| `consultar(con, sql, params...)` | Prepara y ejecuta un `SELECT`/`SHOW` y devuelve una lista de mapas columna→valor en orden; las columnas `YEAR` se leen como `Integer` para mostrar solo el año. |
| `ejecutar(con, sql, params...)` | Ejecuta una escritura con `executeUpdate()` y devuelve las filas afectadas (sin commit). |
| `preparar(...)` | Crea el `PreparedStatement` y asigna los parámetros por posición (desde 1). |
| `imprimir(titulo, filas)` y `unir(...)` | Calculan el ancho de cada columna y escriben la tabla alineada (encabezado, separador `-+-`, filas); «(sin filas)» si está vacío. |
| `main` | Prueba rápida: versión del servidor, base y cuenta. |

#### `Ddl.java`, `Dml.java`, `Dql.java`, `Vdl.java`, `Dcl.java`, `Tcl.java`

Son los equivalentes en Java de `ddl.py`, `dml.py`, `dql.py`, `vdl.py`, `dcl.py` y `tcl.py`;
la tabla de «Conexión y consultas desde Java» resume cada una. Diferencias de
implementación:

| Clase | Detalle |
|---|---|
| `Ddl` | `SENTENCIAS` es un `List.of(...)` de *text blocks*; el resumen impreso limita a 90 caracteres con `substring`. |
| `Dml` | Usa `?` como marcador y `Conexion.ejecutar` con los mismos valores que Python. |
| `Dql` | `record Consulta(titulo, sql)` y un `LinkedHashMap` llenado en un bloque `static`; valida los nombres recibidos antes de conectar y sale con código 1 si alguno es desconocido. |
| `Vdl` | `record Vista(crear, consulta)`; con `--drop` elimina las vistas y termina. |
| `Dcl` | `record Cuenta(clave, privilegios)`; las contraseñas salen de `Conexion.env(...)`. |
| `Tcl` | Usa `Savepoint` de JDBC (`con.setSavepoint` / `con.rollback(sp)`) y el método auxiliar `insertarRenta`, que pide `RETURN_GENERATED_KEYS` para obtener el `Renta_ID`. |

### Flujo completo de ejecución y dependencias entre archivos

```
.env.example ──copia──▶ .env ──leído por──▶ py/conexion.py ──▶ py/ddl|dml|dql|vdl|dcl|tcl.py
                                       └──▶ java/Conexion.java ──▶ java/Ddl|Dml|Dql|Vdl|Dcl|Tcl.java

sql/mariadb/glob_gusters.sql ▶ sql/mariadb/glob_gusters_insert.sql ▶ commands/01 ▶ 02 ▶ 03 ▶ 04 ▶ 05 ▶ 06
requirements.txt ──▶ .venv (Python)        java/lib/*.jar (JDBC) ──▶ java/out (clases compiladas)
```

- Los scripts `py/` y `java/` dependen de que la base ya exista (`sql/mariadb/glob_gusters.sql`
  y sus datos iniciales) y, `dml`/`dql`/`vdl`, de que `ddl` haya agregado las columnas y
  cambios de estructura requeridos.
- `dcl` necesita una cuenta administrativa; `tcl` necesita los datos de ejemplo.

## Cómo subir este proyecto a GitHub

Estos comandos de `git` son idénticos en Windows (PowerShell o cmd.exe), macOS y
Linux:

```bash
git init
git add .
git commit -m "Primer commit: modelo normalizado Glob-Gusters"
git branch -M main
git remote add origin https://github.com/<usuario>/glob-gusters-videoclub.git
git push -u origin main
```

## Protección de la rama `main`

La rama `main` de este repositorio tiene activada la protección de rama de GitHub,
con la siguiente configuración:

| Regla | Estado |
|---|---|
| Requiere Pull Request para fusionar cambios | ✅ Activado |
| Aprobaciones mínimas por PR | **1** |
| Se aplica también al propietario/administrador | ❌ Desactivado |
| Permite `force-push` a `main` | ❌ Bloqueado |
| Permite eliminar la rama `main` | ❌ Bloqueado |

En la práctica, esto significa:

- **El propietario del repositorio** conserva permiso para hacer `git push` directo
  a `main`, sin necesidad de abrir un Pull Request.
- **Cualquier otro colaborador** (sin permisos de administrador) que quiera
  modificar el proyecto o agregar una nueva funcionalidad debe crear una rama,
  subir sus cambios y abrir un Pull Request contra `main`; ese PR necesita al menos
  **una aprobación humana** antes de poder fusionarse.

Esta configuración se administra desde **Settings → Branches → Branch protection
rules** en GitHub, o mediante la API:

```bash
gh api repos/<usuario>/glob-gusters-videoclub/branches/main/protection
```

## Licencia

Este proyecto se distribuye bajo licencia MIT. Véase el archivo [LICENSE](LICENSE).
