-- DATABASE
create database ColprystFastApi;
use ColprystFastApi;

-- TABLA CARGO
CREATE TABLE Cargo (
  IdCargo INTEGER AUTO_INCREMENT NOT NULL,
  NombreCargo varchar (80),
  Descripcion varchar (80),
  CONSTRAINT PK_Cargo PRIMARY KEY(IdCargo)
);

-- TABLA USUARIO
CREATE TABLE Usuario (
  IdUsuario INTEGER AUTO_INCREMENT NOT NULL,
  Tipo_doc varchar (80),
  numero_doc varchar (80),
  Nombre_empleado varchar (80),
  Email_empleado varchar (80),
  constraint PK_Usuario primary key (IdUsuario),
  IdCargoUsu INTEGER
);

alter table Usuario add constraint fk_IdCargoUsu foreign key (IdCargoUsu) references Cargo (IdCargo);

-- INSERT
-- Inserción de registros en la tabla Cargo
INSERT INTO Cargo (NombreCargo, Descripcion) VALUES 
('Gerente', 'Gerente de operaciones'),
('Desarrollador', 'Desarrollador de software'),
('Contador', 'Encargado de finanzas'),
('Soporte Técnico', 'Soporte de IT'),
('Marketing', 'Especialista en marketing'),
('Recursos Humanos', 'Gestión de personal'),
('Vendedor', 'Venta de productos'),
('Analista', 'Analista de datos'),
('Director', 'Director de la empresa'),
('Administrativo', 'Administración general');

-- Inserción de registros en la tabla Usuario
INSERT INTO Usuario (Tipo_doc, numero_doc, Nombre_empleado, Email_empleado, IdCargoUsu) VALUES 
('DNI', '12345678A', 'Carlos Pérez', 'carlos.perez@colpryst.com', 1),
('DNI', '23456789B', 'Ana Gómez', 'ana.gomez@colpryst.com', 2),
('DNI', '34567890C', 'Luis Martínez', 'luis.martinez@colpryst.com', 3),
('DNI', '45678901D', 'Marta Rodríguez', 'marta.rodriguez@colpryst.com', 4),
('DNI', '56789012E', 'Jorge Fernández', 'jorge.fernandez@colpryst.com', 5),
('DNI', '67890123F', 'Lucía Díaz', 'lucia.diaz@colpryst.com', 6),
('DNI', '78901234G', 'Juan López', 'juan.lopez@colpryst.com', 7),
('DNI', '89012345H', 'Elena Sánchez', 'elena.sanchez@colpryst.com', 8),
('DNI', '90123456I', 'Pedro Gutiérrez', 'pedro.gutierrez@colpryst.com', 9),
('DNI', '01234567J', 'Sara Ruiz', 'sara.ruiz@colpryst.com', 10),
-- 5 veces el cargo 'Soporte Técnico' (IdCargoUsu = 4)
('DNI', '11111111A', 'Laura Moreno', 'laura.moreno@colpryst.com', 4),
('CC', '22222222B', 'Andrés Torres', 'andres.torres@colpryst.com', 4),
('CC', '33333333C', 'Gabriel Núñez', 'gabriel.nunez@colpryst.com', 4),
('DNI', '44444444D', 'Natalia Herrera', 'natalia.herrera@colpryst.com', 4),
('DNI', '55555555E', 'Emilio Castro', 'emilio.castro@colpryst.com', 4),

-- 5 veces el cargo 'Vendedor' (IdCargoUsu = 7)
('CC', '66666666F', 'Carla Vega', 'carla.vega@colpryst.com', 7),
('DNI', '77777777G', 'Ricardo Flores', 'ricardo.flores@colpryst.com', 7),
('DNI', '88888888H', 'Alejandro Ortiz', 'alejandro.ortiz@colpryst.com', 7),
('DNI', '99999999I', 'Raquel Sánchez', 'raquel.sanchez@colpryst.com', 7),
('DNI', '10101010J', 'Pablo Díaz', 'pablo.diaz@colpryst.com', 7),

-- 2 veces el cargo 'Marketing' (IdCargoUsu = 5)
('DNI', '11122233K', 'Marta Blanco', 'marta.blanco@colpryst.com', 5),
('DNI', '22233344L', 'Esteban Suárez', 'esteban.suarez@colpryst.com', 5),

-- 1 vez el cargo 'Desarrollador' (IdCargoUsu = 2)
('DNI', '33344455M', 'Rosa Delgado', 'rosa.delgado@colpryst.com', 2),

-- 1 vez el cargo 'Contador' (IdCargoUsu = 3)
('DNI', '44455566N', 'Tomás Gil', 'tomas.gil@colpryst.com', 3),

-- 1 vez el cargo 'Recursos Humanos' (IdCargoUsu = 6)
('DNI', '55566677O', 'Valeria Rojas', 'valeria.rojas@colpryst.com', 6);


-- drop database ColprystFastApi;