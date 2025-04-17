-- Usando EXPLAIN para entender o plano de execução
EXPLAIN
SELECT * FROM pedidos WHERE cliente_id = 5;

-- Criando um índice simples
CREATE INDEX idx_cliente_id ON pedidos(cliente_id);

-- Criando um índice composto (cliente_id + data_pedido)
CREATE INDEX idx_cliente_data ON pedidos(cliente_id, data_pedido);

-- Consultando os índices da tabela
SHOW INDEX FROM pedidos;

-- Consultas otimizadas com índice composto
EXPLAIN
SELECT * FROM pedidos WHERE cliente_id = 3 AND data_pedido >= '2024-01-01';

-- CUIDADO: funções em colunas podem ignorar o índice
-- EXEMPLO que não usa índice:
EXPLAIN
SELECT * FROM pedidos WHERE YEAR(data_pedido) = 2024;
