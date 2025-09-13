EVIDENCIA INTEGRADORA Nº 3

YA HECHO:
- ARCHIVOS BASE SUBIDOS
- PRIMERAS CORRECCIONES REALIZADAS
- reorganizar funciones donde corresponda para poder despues borrar el archivo funciones.py
- mejorar dichas funciones y agregar las que hagan falta para funcionalidad nueva
- que el borrado de dispositivos se haga en su modulo como funcion extra
- cambiar rol de usuario
- testear todo
- tener pensado el caso especifico que se va a usar como ejemplo para 

EVIDENCIA INTEGRADORA Nº 3 // CORRECCIONES POR HACER

¡Buen trabajo! A continuación algunos puntos para revisar/mejorar:

    Faltan validaciones. Ej, si en el menú ingresa un carácter en lugar de un número, falla.
    No utilizar try except para validaciones de tipos de datos. Existen métodos que Python nos provee para esto o bien utilizar try except ValueError
    Eliminar dispositivo. Al no solicitar el id, el usuario difícilmente sabe el identificador. A menos que le muestra una lista de los dispositivos con su id
    No hace falta pasar las listas por argumentos, en su lugar utilizar variables no locales.
    Revisar la modularidad. El módulo funciones quizás deba separarse en varios módulos (respetar principio de responsabilidad unica)
    Falta modo día.

Vamos bien, no olvidar correcciones previas para futuras entregas. A continuación algunos puntos para revisar/corregir:

    Cerrar sesión no debería sacarme del menú. Especificar una opción para ello.
    Al ejecutar la automatización, sea que esté o no activada, debe brindar información al usuario.
    Buscar por nombre, no informa al usuario si encontró o no el dispositivo. Revisar el resto.
    EV2. Faltan algunas correcciones

// QUE CAMBIAMOS:
Correcciones de la Evidencia 3 implementadas

- Archivos base subidos al repositorio.

- Primeras correcciones realizadas y funciones reorganizadas.

- Reorganización de funciones para poder, en el futuro, eliminar funciones.py.

- Mejoras en funciones existentes y agregado de funciones necesarias para nuevas funcionalidades.

- Borrado de dispositivos implementado en su módulo correspondiente como función extra, mostrando la lista con IDs.

- Cambio de rol de usuario implementado.

- Testeo completo de todas las funciones realizadas.

- Caso específico definido para demo.

- Búsqueda por nombre de dispositivo revisada y funcionando correctamente, informa si encuentra o no el dispositivo.

- Validaciones de entrada mejoradas para el menú: evita errores por caracteres no numéricos.

- Validación de tipos de datos realizada sin uso indiscriminado de try-except, usando try-except ValueError de manera específica.

- Uso de variables no locales en lugar de pasar listas por argumentos.

- Modularidad revisada, respetando principio de responsabilidad única.

- Modo día implementado correctamente.

- Automatizaciones ahora informan al usuario sobre su estado, esté activada o no.

-Cerrar sesión implementado correctamente (opción de logout presente).

