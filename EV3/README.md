
//  CAMBIOS:
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

- Cerrar sesión implementado correctamente (opción de logout presente).

 cambios (EVIDENCIA 5):

-Caso específico definido para demo fue eliminado.

-Se sustituyó Modo Día por Modo Noche y Modo Meditación.
         Modo Meditación: altera la intensidad de la luz para crear un ambiente más suave. Este modo ya está integrado en el flujo de automatización.

-Con estos cambios, se realizaron ajustes para que la transiciones entre modos sean posibles y coherentes con el estado actual del sistema.

-se ajusto para que el tipo sea Luz, no luces

-Se cambio la lógica de la automatización en el main para que se ejecute una vez que el usuario ya este logeado.

-se realizo cambios para que el programa tenga en cuenta la posibilidad de que no haya ninguna automatizacion activada.

