# Proyecto POO - SmartHome

## Compilador y motor de base de datos elegidos

- **Compilador online:** OneCompiler
- **Motor de base de datos:** MySQL

---

## Instrucciones de uso

Debido a que **OneCompiler para MySQL** no permite adjuntar archivos locales, es necesario **copiar el código de los scripts** (DDL y DML) en dos archivos distintos dentro del editor online.

---

### Usar el editor ya configurado

**[Abrir editor en OneCompiler con código pre-cargado](https://onecompiler.com/mysql/43z779gat)**  

> Luego de abrir el enlace, tocar el botón **rosa “RUN”** para ejecutar el código.

---

### Opción manual

1. Ingresar a [https://onecompiler.com/](https://onecompiler.com/)
2. Seleccionar el motor **MySQL**.
3. Borrar el código predefinido que aparece.
4. En el panel lateral izquierdo, presionar el **símbolo “+”** → seleccionar **“Add init schema”** → aceptar y borrar el contenido predefinido.
5. En el archivo **`init.sql`**, pegar todo el script DDL (estructura de la base de datos).
6. En el archivo **`queries.sql`**, pegar todo el script DML (consultas o inserciones de datos).
7. Finalmente, hacer click en el botón **RUN** (ubicado arriba a la derecha).

---

- **Comentarios:**  
  OneCompiler acepta el símbolo `#` como comentario en MySQL.  
  Por eso, se utilizó `#` para explicar qué hace cada consulta dentro de los scripts.

---

## Cambio en el script DDL

El único cambio respecto a la versión anterior es en la tabla **`usuarios`**:  
Ahora el campo `rol` se define como un **ENUM** (en lugar de `VARCHAR`), para garantizar la consistencia de los valores permitidos.

```sql
CREATE TABLE usuarios (
    id_usuario INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    rol ENUM('admin', 'estandar') NOT NULL,
    PRIMARY KEY (id_usuario)
);