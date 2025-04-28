from flask import Flask, request, jsonify
from database import SessionLocal
from models import Cliente, Pedido
from schemas import cliente_to_dict

app = Flask(__name__)

@app.route("/clientes", methods=["POST"])
def criar_cliente():
    session = SessionLocal()
    data = request.json
    novo_cliente = Cliente(nome=data["nome"])
    session.add(novo_cliente)
    session.commit()
    session.close()
    return {"mensagem": "Cliente criado com sucesso."}, 201

@app.route("/clientes", methods=["GET"])
def listar_clientes():
    session = SessionLocal()
    clientes = session.query(Cliente).all()
    resultado = [cliente_to_dict(cliente) for cliente in clientes]
    session.close()
    return jsonify(resultado)

@app.route("/clientes/<int:id>", methods=["PUT"])
def atualizar_cliente(id):
    session = SessionLocal()
    cliente = session.query(Cliente).filter_by(id=id).first()
    if cliente:
        data = request.json
        cliente.nome = data.get("nome", cliente.nome)
        session.commit()
        session.close()
        return {"mensagem": "Cliente atualizado."}
    session.close()
    return {"erro": "Cliente não encontrado."}, 404

@app.route("/clientes/<int:id>", methods=["DELETE"])
def deletar_cliente(id):
    session = SessionLocal()
    cliente = session.query(Cliente).filter_by(id=id).first()
    if cliente:
        session.delete(cliente)
        session.commit()
        session.close()
        return {"mensagem": "Cliente deletado."}
    session.close()
    return {"erro": "Cliente não encontrado."}, 404

if __name__ == "__main__":
    app.run(debug=True)
