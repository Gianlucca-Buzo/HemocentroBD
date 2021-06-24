USE HEMOCENTRO;

INSERT INTO Doador VALUES
    ('04048884026','Gianlucca de Mendonca Buzo', 'gdmbuzo@inf.ufpel.edu.br', 'M', '2001-03-01','O+'),
    ('44334528821','Isabela Fernandes Gomes Dias','ifgdias@inf.ufpel.edu.br','F', '2000-09-13','B+'),
    ('88731247132','Joaz Fernando', 'jfernando@inf.ufpel.edu.br', 'M', '1999-07-21','A-');

INSERT INTO Telefones_Doador VALUES
    ('04048884000','53981304077'),
    ('04048884025','53981349629'),
    ('04048884090','11981552981'),
    ('04048884026','11981552998'),
    ('88731247132','11981552777'),
    ('44334528821','53981256763');

INSERT INTO Endereco_Doador VALUES 
    ('04048884000', 'General Osorio', '1085', 'Apartamento 402'),
    ('04048884025', 'Tres de maio', '679', 'Apartamento 708'),
    ('44334528821', 'Dom Joaquim', '675', null),
    ('04048884090', 'Fernando Osorio', '1027','Bloco c, Apartamento 204')
    ('04048884026', 'Dom Joaquim', '676', null),
    ('88731247132', 'Fernando Osorio', '1028','Bloco c, Apartamento 204');

INSERT INTO Funcionario VALUES 
    ('04027738102', 'Jose da Silva Cardoso', 'jose.cardoso@gmail.com', 'M', '1983-02-18',4000.0,null),
    ('32412412373', 'Alerquina Duarte Mendes', 'ale.duarte@hotmail.com', 'F', '1998-05-24',4500.0,null),
    ('32412412002', 'Jorge Silveira Pinto', 'pinto.jorge@hotmail.com', 'M', '1970-11-01',2000.0,'Faxineiro'),
    ('32412412003', 'Alice Cardoso', 'alice.cardoso@hotmail.com', 'F', '2003-12-09',1500.0,'Recepcionista'),
    ('81231726312', 'Joao Carlos Lunardi', 'jcarlos.lunardi@hotmail.com','M', '1995-07-12',8000.0,null);

INSERT INTO Telefones_Funcionario VALUES 
    ('04027738102', '51981627312'),
    ('32412412373', '51981512533'),
    ('32412412002', '51981723999'),
    ('32412412003', '51981723677'),
    ('81231726312', '51981723671'),
    ('81231726312', '51981723688');

INSERT INTO Endereco_Funcionario VALUES 
    ('04027738102', 'Gonçalves chaves', '257', null),
    ('32412412373', 'Dom Joaquim', '854', 'Apartamento 201'),
    ('32412412002', 'Fernando Osório', '2691', 'Apartamento 402'),
    ('32412412003', 'Marechal Barroso', '127', null),
    ('81231726312', 'Dom Pedro II', '1932', null);

INSERT INTO Enfermeiro VALUES 
    ('04027738102', '64812831082','32710485761'),
    ('32412412373', '37887126631','87491023124');

INSERT INTO Administrador VALUES 
    ('81231726312', '81231726312', MD5('joaoadmin'));

INSERT INTO Hospital (Nome, Email) VALUES
    ('Unimed', 'unimed.pelotas@hotmail.com'),
    ('Santa Joana', 'santajoana@hotmail.com'),
    ('Santa Casa', 'santacasa.pelotas@hotmail.com'),
    ('São Camilo', 'saocamilohospital@gmail.com');

INSERT INTO Telefones_Hospital VALUES 
    (1,'53981232787'),
    (3,'5332278609'),
    (4,'5332278344'),
    (1,'5332278657'),
    (2,'53981765368');

INSERT INTO Endereco_Hospital VALUES 
    (1,'Doutor Floriano', '465',null),
    (3,'Alberto Rosa', '1086',null),
    (4,'Dom Pedro II', '1536',null),
    (2,'Alberto Rosa', '338',null);

INSERT INTO Pedido (ID_Hospital,TipoSanguineo,DataPedido,Quantidade) VALUES 
    (1, 'A-', '2021-03-12',20.0),
    (1, 'AB-', '2021-03-12',35.0),
    (2, 'O-', '2021-04-17',15.0),
    (1, 'AB+', '2021-01-04',50.0),
    (3, 'B+', '2021-06-24',50.0),
    (4, 'A+', '2021-06-23',50.0),
    (2, 'O+', '2021-01-02',37.0);

INSERT INTO Transacao (ID_Pedido,DataTransacao) VALUES 
    (4,'2021-02-04'),
    (5,'2021-03-15'),
    (3,'2021-01-10');

INSERT INTO Estoque VALUES 
    ('A-', 525.0 ),
    ('A+', 760.0 ),
    ('B-', 420.0 ),
    ('B+', 463.0 ),
    ('AB-', 358.0 ),
    ('AB+', 234.0 ),
    ('O-', 198.0 ),
    ('O+', 768.0 );

INSERT INTO Doacao (ID_Doador,ID_Enfermeiro,DataDoacao,Quantidade) VALUES 
    ('04048884000', '32412412373', '2021-03-01',1.5),
    ('44334528821', '04027738102', '2021-06-20',1.0),
    ('04048884025', '04027738102', '2021-01-25',1.0);