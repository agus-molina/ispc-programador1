CREATE TABLE usuarios (
    id_usuario INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL UNIQUE,
    contraseña VARCHAR(255) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    rol VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_usuario)
);

CREATE TABLE dispositivos (
    id_dispositivo INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL UNIQUE,
    tipo VARCHAR(100) NOT NULL,
    estado BOOLEAN NOT NULL,
    intensidad INT UNSIGNED,
    volumen INT UNSIGNED,
    infrarrojo BOOLEAN,
    id_usuario INT NOT NULL,
    PRIMARY KEY (id_dispositivo),
    CONSTRAINT fk_dispositivos
        FOREIGN KEY (id_usuario)
        REFERENCES usuarios(id_usuario)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE automatizaciones (
    id_automatizacion INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL UNIQUE,
    estado BOOLEAN NOT NULL,
    hora_activacion TIME NOT NULL,
    hora_desactivacion TIME NOT NULL,
    id_usuario INT NOT NULL,
    PRIMARY KEY (id_automatizacion),
    CONSTRAINT fk_automatizaciones
        FOREIGN KEY (id_usuario)
        REFERENCES usuarios(id_usuario)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

INSERT INTO usuarios (username, contraseña, correo, rol)
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
    ('camara puerta', 'camara', true, NULL, NULL, true, 2),
    ('luz oficina', 'luz', true, 30, NULL, NULL, 2);