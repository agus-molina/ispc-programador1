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
    intensidad INT,
    volumen INT,
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
