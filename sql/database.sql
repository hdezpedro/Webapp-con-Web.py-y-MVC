CREATE DATABASE ria_phl;

USE ria_phl;

create table producto(
id_producto       int(4)      not null primary key auto_increment,
nombre_producto   varchar(30) not null,
marca varchar(10) not null,
cantidad varchar(20) not null,
telefono         varchar(10) not null);


insert into producto(nombre_producto, marca, cantidad, telefono) values
('principe', 'marinela', '20', '7776876189'),
('trikitraket', 'gamesa', '80', '7757253858'),
('pan tostado', 'bimbo', '78', '7757658958');



CREATE USER 'ria'@'localhost' IDENTIFIED BY 'ria.2019';
GRANT ALL PRIVILEGES ON ria_iniciales.* TO 'ria'@'localhost';
FLUSH PRIVILEGES;
