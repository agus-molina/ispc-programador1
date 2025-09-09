EVIDENCIA INTEGRADORA Nº 3 // CORRECCIONES POR HACER

¡Buen trabajo! A continuación algunos puntos para revisar/mejorar:
- Faltan validaciones. Ej, si en el menú ingresa un carácter en lugar de un número, falla.
- No utilizar try except para validaciones de tipos de datos. Existen métodos que Python nos provee para esto o bien utilizar try except ValueError
- Eliminar dispositivo. Al no solicitar el id, el usuario difícilmente sabe el identificador. A menos que le muestra una lista de los dispositivos con su id
- No hace falta pasar las listas por argumentos, en su lugar utilizar variables no locales.
- Revisar la modularidad. El módulo funciones quizás deba separarse en varios módulos (respetar principio de responsabilidad unica)
- Falta modo día.

Vamos bien, no olvidar correcciones previas para futuras entregas.
A continuación algunos puntos para revisar/corregir:
- Cerrar sesión no debería sacarme del menú. Especificar una opción para ello.
- Al ejecutar la automatización, sea que esté o no activada, debe brindar información al usuario.
- Buscar por nombre, no informa al usuario si encontró o no el dispositivo. Revisar el resto.
- EV2. Faltan algunas correcciones

// QUE CAMBIAMOS:
