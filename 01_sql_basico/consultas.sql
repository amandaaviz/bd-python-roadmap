-- Seleciona todos os dados da tabela "clientes"
SELECT * FROM clientes;

-- Seleciona clientes com idade acima de 30
SELECT nome, idade FROM clientes WHERE idade > 30;

-- Conta quantos clientes há por cidade
SELECT cidade, COUNT(*) as total FROM clientes GROUP BY cidade;

-- Ordena clientes por nome
SELECT nome, email FROM clientes ORDER BY nome ASC;

-- Usa JOIN entre clientes e pedidos
SELECT c.nome, p.data_pedido
FROM clientes c
JOIN pedidos p ON c.id = p.cliente_id;

-- Subquery: clientes que fizeram pedidos com valor acima de 500
SELECT nome FROM clientes
WHERE id IN (
    SELECT cliente_id FROM pedidos WHERE valor > 500
);
