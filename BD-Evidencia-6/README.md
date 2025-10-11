. COMPILADOR ONLINE ELEGIDO: OneCompiler
. MOTOR DE BASES DE DATOS ELEGIDO: MySQL

INSTRUCCIONES DE USO:
    Debido a que OneCompiler para MySQL no nos permite adjuntar archivos locales del computador,
    es necesario copiar el codigo de los scripts a dos archivos distintos dentro del editor online.

    - Link de editor ya preparado para su ejecución con código incorporado:
        https://onecompiler.com/mysql/43z779gat

        (Hay que presionar el botón rosa que dice "RUN" para correr el código)

    - En caso de no funcionar el link, a continuación explicaremos como hacerlo manualmente:
     1- Ingresar a https://onecompiler.com/
     2- Seleccionar el motor MySQL
     3- Borrar el código predefinido
     4- Seleccionar el simbolo + que se encuentra del lado izquierdo de la página, seleccionar Add init schema, aceptar y borrar todo lo que aparece predefinido.
     5- En el archivo init.sql pegar todo el script de DLL que sigue siendo el mismo de la evidencia anterior.
     6- En el archivo queries.sql pegar el script de DML.
     7- Por último hacer click en el botón RUN ubicado en la parte superior derecha.

     OneCompiler acepta el # como símbolo de comentario, por lo que fue el elegido para explicar que hace cada consulta

El unico cambio DLL sería a la tabla de usuarios siguiendo las correcciones dadas de forma que el rol
sea un ENUM en vez de solo string:

    CREATE TABLE usuarios (
        id_usuario INT NOT NULL AUTO_INCREMENT,
        username VARCHAR(255) NOT NULL UNIQUE,
        contrasena VARCHAR(255) NOT NULL,
        correo VARCHAR(255) NOT NULL,
        rol ENUM('admin', 'estandar') NOT NULL,
        PRIMARY KEY (id_usuario)
    );

