INSERT INTO usuarios (username, contrasena, correo, rol)
VALUES
    ('susana', '123', 'hola@ispc.com', 'admin'),
    ('clara', '1234', 'probando@ispc.com', 'admin'),
    ('carlos', '1235', 'estoesunmail@ispc.com', 'estandar'),
    ('pepe', '123456', 'email@ispc.com', 'estandar'),
    ('meme', '1234567', 'correo@ispc.com', 'estandar'),
    ('juan', '12345678', 'posta@ispc.com', 'admin'),
    ('alma', '123456789', 'que@gmail.com', 'estandar'),
    ('emma', '12345678910', 'mas@hotmail.com', 'estandar'),
    ('pablo', '1234567891011', 'podemos@yahoo.com', 'estandar'),
    ('fran', '123456789101112', 'poner@ispc.com', 'estandar');
    
INSERT INTO dispositivos (nombre, tipo, estado, intensidad, volumen, infrarrojo, id_usuario)
VALUES
    ('luz de living', 'luz', false, 0, NULL, NULL, 1),
    ('luz de pieza principal', 'luz', true, 20, NULL, NULL, 1),
    ('luz de comedor', 'luz', true, 10, NULL, NULL, 1),
    ('televisor de pieza principal', 'electrodomestico', true, NULL, 15, NULL, 1),
    ('televisor de living', 'electrodomestico', false, NULL, 0, NULL, 1),
    ('camara patio', 'camara', true, NULL, NULL, true, 1),
    ('camara cochera', 'camara', false, NULL, NULL, false, 1),
    ('camara frontal', 'camara', false, NULL, NULL, false, 2),
    ('luz oficina', 'luz', true, 30, NULL, NULL, 2),
    ('luz pieza niños', 'luz', false, 0, NULL, NULL, 2),
    ('microondas', 'electrodomestico', false, 1, 5, NULL, 1),
    ('parlantes living', 'electrodomestico', false, 1, 20, NULL, 2),
    ('parlantes oficina', 'electrodomestico', true, 1, 15, NULL, 2),
    ('puerta cochera', 'electrodomestico', false, NULL, NULL, NULL, 1),
    ('puerta patio','electrodomestico', true, NULL, NULL, NULL, 1),
    ('puerta frontal','electrodomestico', false, NULL, NULL, NULL, 1),
    ('camara timbre', 'camara', true, NULL, NULL, false, 1),
    ('cortina living 1','electrodomestico', false, NULL, NULL, NULL, 1),
    ('cortina living 2','electrodomestico', false, NULL, NULL, NULL, 1),
    ('cortina pieza principal 1', 'electrodomestico', true, NULL, NULL, NULL, 1),
    ('cortina pieza principal 2', 'electrodomestico', true, NULL, NULL, NULL, 1),
    ('cortina niños', 'electrodomestico', true, NULL, NULL, NULL, 1);
    
INSERT INTO automatizaciones (nombre, estado, hora_activacion, hora_desactivacion, id_usuario)
VALUES
    ('modo noche', true, '23:59:59', '06:00:00', 1),
    ('meditacion', true, '15:00:00', '16:00:00', 1),
    ('siesta pieza principal', true, '14:00:00', '15:00:00', 2),
    ('siesta pieza niños', true, '14:00:00', '16:00:00', 2),
    ('living tranquilo', true, '14:00:00', '16:00:00', 2),
    ('despertar pieza principal', true, '06:00:00', '07:00:00', 2),
    ('despertar pieza niños', true, '08:00:00', '09:00:00', 2),
    ('cine en casa living', false, '17:00:00', '22:00:00', 1),
    ('ahorro energia', false, '06:00:00', '18:00:00', 1),
    ('fiesta casa completa', false, '20:00:00', '23:59:59', 2);
    
# CONSULTAS SIMPLES

# Para que devuelva todos los usuarios admin

SELECT *
FROM usuarios
WHERE rol = 'admin';

# Para que devuelva que automatizaciones estan activas

SELECT nombre, estado
FROM automatizaciones
WHERE estado = true;

# Para que devuelva que luces estan prendidas

SELECT nombre, estado
FROM dispositivos
WHERE estado = true
  AND tipo = 'luz';
  
# CONSULTAS MULTITABLAS

# Para que devuelva que electrodomesticos estan asociados a un usuario especifico

SELECT dispositivos.nombre, dispositivos.tipo, usuarios.username
FROM dispositivos
INNER JOIN usuarios
  ON dispositivos.id_usuario = usuarios.id_usuario
  AND dispositivos.tipo = 'electrodomestico'
  AND usuarios.username = 'clara';
  
# Para que devuelva la cantidad de dispositivos asociados por usuario y el rol de este ultimo

SELECT username, rol, COUNT(dispositivos.id_dispositivo) AS cantidad_dispositivos
FROM usuarios
LEFT JOIN dispositivos
  ON usuarios.id_usuario = dispositivos.id_usuario
GROUP BY username, rol;

# Para que devuelva los dispositivos encendidos que tiene cada usuario asociados

SELECT username, nombre, tipo ,estado
FROM usuarios
INNER JOIN dispositivos
  ON usuarios.id_usuario = dispositivos.id_usuario
WHERE estado = true;

# Para que devuelva cuantos dispositivos son afectados por una automatizacion

SELECT 
    aut.nombre AS automatizacion,
    COUNT(disp.id_dispositivo) AS cantidad_dispositivos
FROM automatizaciones aut
JOIN dispositivos disp
  ON
  (
      (aut.nombre LIKE '%living%' AND disp.nombre LIKE '%living%')
      OR (aut.nombre LIKE '%pieza principal%' AND disp.nombre LIKE '%pieza principal%')
      OR (aut.nombre LIKE '%pieza niños%' AND disp.nombre LIKE '%pieza niños%')
  )
GROUP BY aut.nombre;
  
# SUBCONSULTAS

# Para que devuelva las automatizaciones encendidas que involucren al living
# y los dispositivos que tengan que ver con el mismo

SELECT 
    aut.nombre AS automatizacion,
    aut.estado AS estado_automatizacion,
    disp.nombre AS dispositivo,
    disp.estado AS estado_dispositivo
FROM automatizaciones aut
JOIN (
    SELECT nombre, estado
    FROM dispositivos
    WHERE nombre LIKE '%living%'
) AS disp
  ON aut.nombre LIKE '%living%'
WHERE aut.estado = 1;

# Para que devuelva el usuario con más dispositivos vinculados

SELECT username as usuario_con_mas_dispositivos, rol
FROM usuarios
WHERE id_usuario = (
    SELECT id_usuario
    FROM dispositivos
    GROUP BY id_usuario
    ORDER BY COUNT(id_usuario) DESC
    LIMIT 1
);