-- Crear la base de datos 'citaexpress' si no existe
CREATE DATABASE IF NOT EXISTS citaexpress;

-- Cambiar a la base de datos 'citaexpress'
USE citaexpress;

-- Crear el usuario
CREATE USER 'admincitaexpress'@'localhost' IDENTIFIED BY 'C1ta3xpress*.';

-- Otorgar todos los privilegios al usuario sobre la base de datos 'citaexpress'
GRANT ALL PRIVILEGES ON citaexpress.* TO 'admincitaexpress'@'localhost';

-- Actualizar los privilegios
FLUSH PRIVILEGES;

-- Crear la tabla Clients en la base de datos 'citaexpress'
CREATE TABLE Clients (
    client_id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255)
);

-- Crear la tabla Professionals en la base de datos 'citaexpress'
CREATE TABLE Professionals (
    professional_id INT PRIMARY KEY,
    name VARCHAR(255),
    specialty VARCHAR(255),
    availability VARCHAR(255)
);

-- Crear la tabla Appointments en la base de datos 'citaexpress'
CREATE TABLE Appointments (
    appointment_id INT PRIMARY KEY,
    client_id INT,
    professional_id INT,
    date DATE,
    time TIME,
    status VARCHAR(50),
    FOREIGN KEY (client_id) REFERENCES Clients(client_id),
    FOREIGN KEY (professional_id) REFERENCES Professionals(professional_id)
);
