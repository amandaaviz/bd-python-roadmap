def cliente_to_dict(cliente):
    return {
        "id": cliente.id,
        "nome": cliente.nome,
        "pedidos": [{"id": p.id, "valor": p.valor} for p in cliente.pedidos]
    }
