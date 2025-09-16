DIAGRAMA DE CLASES

Para que cada clase sea como una caja negra se definieron los atributos de forma privada para que otras clases no puedan acceder de forma libre a los componentes y tener cierto nivel de abstracción donde solo pueden tener acceso a lo que les corresponde.
Al ser atributos privados se evita la fácil modificación de los valores y la dependencia entre clases, aumentando la encapsulación. Solo la clase propia tiene poder sobre la interacción con otras.
En cuanto a la clase Dispositivo, debido a que puede ser de distintos tipos y cada tipo tener sus particularidades, se hizo uso de la herencia especialización para definir Luz, Electrodomestico y Camara.
En caso de estas sufrir cambios, sus implementaciones estan separadas de la clase base, pero tienen elementos en común.

En cuanto a relaciones, para que haya un dispositivo si o si tiene que haber un usuario. Como el usuario es el que registra los dispositivos la relación es de 0 a muchos en ese extremo.
Las automatizaciones estan vinculadas a un usuario y pueden ser muchas aparte de las predefinidas.
Las automatizaciones impactan a los dispositivos por lo que hay una asociación entre una automatización y 1 a muchos dispositivos, ya que tiene que haber al menos uno.