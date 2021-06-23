CREATE DATABASE HEMOCENTRO;
USE HEMOCENTRO;

CREATE TABLE Doador (
    CPF VARCHAR(11) NOT NULL,
    Nome TEXT NOT NULL,
    Email VARCHAR(256) BINARY NOT NULL UNIQUE,
    Sexo ENUM('F', 'M'),
    DataNascimento DATE NOT NULL,
    TipoSanguineo ENUM('A+', 'A-','AB-','AB+','B-','B+','O-','O+'),
    PRIMARY KEY (`CPF`)
);

CREATE TABLE Telefones_Doador (
    CPF_Doador VARCHAR(11) NOT NULL REFERENCES `Doador` (`CPF`),
    Numero VARCHAR(12) NOT NULL,
    PRIMARY  KEY (`CPF_Doador`,`Numero`)
);

CREATE TABLE Endereco_Doador (
    CPF_Doador VARCHAR(11) NOT NULL REFERENCES `Doador` (`CPF`),
    Rua TEXT NOT NULL,
    Numero VARCHAR(6) NOT NULL,
    Complemento TEXT,
    PRIMARY  KEY (`CPF_Doador`)
);

CREATE TABLE Funcionario (
    CPF VARCHAR(11) NOT NULL,
    Nome TEXT NOT NULL,
    Email VARCHAR(256) BINARY NOT NULL UNIQUE,
    Sexo ENUM('F', 'M'),
    DataNascimento DATE NOT NULL,
    Salario FLOAT NOT NULL,
    Cargo TEXT,
    PRIMARY KEY (`CPF`)
);

CREATE TABLE Telefones_Funcionario (
    CPF_Funcionario VARCHAR(11) NOT NULL REFERENCES `Funcionario` (`CPF`),
    Numero VARCHAR(12) NOT NULL,
    PRIMARY  KEY (`CPF_Funcionario`,`Numero`)
);

CREATE TABLE Endereco_Funcionario (
    CPF_Funcionario VARCHAR(11) NOT NULL REFERENCES `Funcionario` (`CPF`),
    Rua TEXT NOT NULL,
    Numero VARCHAR(6) NOT NULL,
    Complemento TEXT,
    PRIMARY  KEY (`CPF_Funcionario`)
);

CREATE TABLE Enfermeiro (
    CPF_Funcionario VARCHAR(11) NOT NULL REFERENCES `Funcionario` (`CPF`),
    Registro_COREN VARCHAR(15) NOT NULL,
    Registro_COFEN VARCHAR(15) NOT NULL,
    PRIMARY  KEY (`CPF_Funcionario`)
);

CREATE TABLE Administrador (
    CPF_Funcionario VARCHAR(11) NOT NULL REFERENCES `Funcionario` (`CPF`),
    ID_Estoque VARCHAR(11) NOT NULL,
    Senha_Estoque VARCHAR(50) NOT NULL,
    PRIMARY  KEY (`CPF_Funcionario`)
);

CREATE TABLE Doacao (
    ID_Doacao BIGINT NOT NULL AUTO_INCREMENT,
    ID_Doador VARCHAR(11) NOT NULL REFERENCES `Doador` (`CPF`),
    ID_Enfermeiro VARCHAR(11) NOT NULL REFERENCES `Enfermeiro` (`CPF_Funcionario`),
    DataDoacao DATE NOT NULL,
    Quantidade FLOAT NOT NULL,
    PRIMARY KEY (`ID_Doacao`)
);

CREATE TABLE Hospital (
    ID_Hospital BIGINT NOT NULL AUTO_INCREMENT,
    Nome TEXT NOT NULL,
    Email VARCHAR(256) BINARY NOT NULL UNIQUE,
    PRIMARY KEY (`ID_Hospital`)
);

CREATE TABLE Telefones_Hospital (
    ID_Hospital BIGINT NOT NULL REFERENCES `Hospital` (`ID_Hospital`),
    Numero VARCHAR(12) NOT NULL,
    PRIMARY  KEY (`ID_Hospital`,`Numero`)
);

CREATE TABLE Endereco_Hospital (
    ID_Hospital BIGINT NOT NULL REFERENCES `Hospital` (`ID_Hospital`),
    Rua TEXT NOT NULL,
    Numero VARCHAR(6) NOT NULL,
    Complemento TEXT,
    PRIMARY  KEY (`ID_Hospital`)
);

CREATE TABLE Pedido (
    ID_Pedido BIGINT NOT NULL AUTO_INCREMENT,
    ID_Hospital BIGINT NOT NULL REFERENCES `Hospital` (`ID_Hospital`),
    TipoSanguineo ENUM('A+', 'A-','AB-','AB+','B-','B+','O-','O+'),
    DataPedido DATE NOT NULL,
    Quantidade FLOAT NOT NULL,
    PRIMARY  KEY (`ID_Pedido`)
);

CREATE TABLE Transacao (
    ID_Transacao BIGINT NOT NULL AUTO_INCREMENT,
    ID_Pedido BIGINT NOT NULL REFERENCES `Pedido` (`ID_Pedido`),
    DataTransacao DATE NOT NULL,
    PRIMARY  KEY (`ID_Transacao`)
);

CREATE TABLE Estoque (
    TipoSanguineo ENUM('A+', 'A-','AB-','AB+','B-','B+','O-','O+'),
    Quantidade FLOAT NOT NULL,
    PRIMARY KEY (`TipoSanguineo`)
);




