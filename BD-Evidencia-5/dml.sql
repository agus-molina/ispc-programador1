INSERT INTO usuarios (username, contrasena, correo, rol)
VALUES
    ('susana', '123', 'hola@ispc.com', 'admin'),
    ('clara', '1234', 'probando@ispc.com', 'admin'),
    ('carlos', '1235', 'estoesunmail@ispc.com', 'estandar'),
    ('pepe', '123456', 'email@ispc.com', 'estandar'),
    ('meme', '1234567', 'correo@ispc.com', 'estandar'),
    ('antonio', '12345678', 'posta@ispc.com', 'estandar');
    
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
    ('modo noche', false, '23:59:59', '06:00:00', 1),
    ('meditacion', true, '15:00:00', '16:00:00', 2);
    
SELECT *
FROM usuarios
WHERE rol = 'admin';

SELECT dispositivos.nombre, dispositivos.tipo, usuarios.username
FROM dispositivos
INNER JOIN usuarios
  ON dispositivos.id_usuario = usuarios.id_usuario
  AND dispositivos.tipo = 'electrodomestico'
  AND usuarios.username = 'clara';
  
SELECT nombre, estado
FROM automatizaciones
WHERE estado = true;