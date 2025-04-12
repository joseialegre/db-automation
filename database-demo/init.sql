CREATE DATABASE Ventas;
GO

USE Ventas;
GO

CREATE TABLE Productos (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100) NOT NULL,
    Precio DECIMAL(10, 2) NOT NULL
);
GO

INSERT INTO Productos (Nombre, Precio)
VALUES
    ('Laptop', 1200.50),
    ('Mouse', 25.99),
    ('Teclado', 45.75);
GO