-- SUBQUERY: clientes com maior valor de pedido
SELECT nome FROM clientes
WHERE id IN (
    SELECT cliente_id FROM pedidos
    WHERE valor = (SELECT MAX(valor) FROM pedidos)
);

-- CTE: pedidos com média e se valor está acima dela
WITH media_valores AS (
    SELECT AVG(valor) AS media_geral FROM pedidos
)
SELECT p.id, p.cliente_id, p.valor,
       CASE
           WHEN p.valor > m.media_geral THEN 'Acima da média'
           ELSE 'Abaixo da média'
       END AS comparacao
FROM pedidos p, media_valores m;
