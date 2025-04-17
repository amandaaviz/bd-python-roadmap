-- PROCEDURE: retorna todos os pedidos de um cliente específico
DELIMITER //
CREATE PROCEDURE pedidos_por_cliente(IN cliente_id INT)
BEGIN
    SELECT * FROM pedidos WHERE cliente_id = cliente_id;
END;
//
DELIMITER ;

-- EXECUTANDO A PROCEDURE
CALL pedidos_por_cliente(3);

-- VIEW: lista de clientes com número de pedidos
CREATE VIEW clientes_com_pedidos AS
SELECT c.id, c.nome, COUNT(p.id) AS total_pedidos
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.id, c.nome;

-- TRIGGER: ao inserir pedido, atualiza automaticamente total de pedidos no cliente
ALTER TABLE clientes ADD COLUMN total_pedidos INT DEFAULT 0;

DELIMITER //
CREATE TRIGGER atualiza_total_pedidos
AFTER INSERT ON pedidos
FOR EACH ROW
BEGIN
    UPDATE clientes
    SET total_pedidos = total_pedidos + 1
    WHERE id = NEW.cliente_id;
END;
//
DELIMITER ;
