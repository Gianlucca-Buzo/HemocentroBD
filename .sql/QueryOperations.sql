USE HEMOCENTRO;

-- Consulta 1: Recuperar as doacoes feitas pelo doador chamado 'Gianlucca de Mendonca Buzo'
SELECT doacao.* FROM Doacao as doacao
INNER JOIN Doador as doador on doador.CPF = doacao.ID_Doador
AND doador.Nome = 'Gianlucca de Mendonca Buzo';

-- Consulta 2: Retornar os registros do COREN e COFEN do enfermeiro que realizou a doacao da 'Isabela Fernandes Gomes Dias'
--no dia '2021-06-20'
SELECT enf.Registro_COREN, enf.Registro_COFEN FROM Enfermeiro as enf
INNER JOIN Doacao as doacao on doacao.ID_Enfermeiro = enf.CPF_Funcionario
AND doacao.DataDoacao = '2021-06-20'
INNER JOIN Doador as doador on doador.CPF = doacao.ID_Doador
AND doador.Nome = 'Isabela Fernandes Gomes Dias';

-- Consulta 3: Retornar todos os pedidos feitos pelo hospital chamado 'Unimed' ao Hemocentro
SELECT ped.* FROM Pedido as ped 
INNER JOIN Hospital as hosp on hosp.ID_Hospital = ped.ID_Hospital
AND hosp.Nome = 'Unimed';

-- Consulta 4: Retornar os tipos sanguineos (e suas quantidades) com quantidade superior a 500.0L no estoque ordenados pela quantidade
SELECT * FROM Estoque 
WHERE Quantidade > 500.0
ORDER BY Quantidade DESC;

-- Consulta 5: Retornar a data da ultima transacao efetuada entre o hospital 'Sao Camilo' e o Hemocentro
SELECT trans.DataTransacao from Transacao as trans
INNER JOIN Pedido as ped on ped.ID_Pedido = trans.ID_Pedido
INNER JOIN Hospital as hosp on hosp.ID_Hospital = ped.ID_Hospital
AND hosp.Nome = 'Sao Camilo'
ORDER BY trans.DataTransacao DESC 
LIMIT 1;

-- Consulta 6: Recuperar todos os telefones do administrador chamado 'Joao Carlos Lunardi'
SELECT tel.Numero FROM Telefones_Funcionario as tel 
INNER JOIN Funcionario as func on func.CPF = tel.CPF_Funcionario 
WHERE func.Nome = 'Joao Carlos Lunardi';

