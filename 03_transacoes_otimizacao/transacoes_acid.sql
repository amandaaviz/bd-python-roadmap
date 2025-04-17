-- Início de uma transação manual
START TRANSACTION;

-- Exemplo de movimentação entre contas (simulação bancária)
UPDATE contas SET saldo = saldo - 500 WHERE id = 1;
UPDATE contas SET saldo = saldo + 500 WHERE id = 2;

-- Confirma a transação
COMMIT;

-- Caso haja erro em algum passo, cancela tudo
-- ROLLBACK;

-- Simulando violação do ACID
-- Por exemplo: dois usuários tentando atualizar o mesmo saldo ao mesmo tempo (problema de concorrência)
-- Use InnoDB e faça LOCKS explícitos quando necessário

-- Bloqueando uma linha até o commit
START TRANSACTION;
SELECT * FROM contas WHERE id = 1 FOR UPDATE;

-- Atualiza e libera após o COMMIT
UPDATE contas SET saldo = saldo + 100 WHERE id = 1;
COMMIT;
