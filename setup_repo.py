import os

folders = [
    "01_sql_basico",
    "02_sql_intermediario",
    "03_transacoes_otimizacao",
    "04_sqlalchemy_orm/crud_basico",
    "04_sqlalchemy_orm/crud_avancado",
    "05_flask_api_relacional",
    "06_mongodb/exemplos",
    "07_redis_cache",
    "08_projeto_final/api_completa",
    "08_projeto_final/docs"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Criar arquivos principais
with open("README.md", "w") as f:
    f.write("# Banco de Dados com Python - Roadmap\n\nEstudos e projetos voltados para dominar banco de dados relacionais e não relacionais com Python.\n")

open("01_sql_basico/consultas.sql", "w").close()
open("02_sql_intermediario/procedures_views_triggers.sql", "w").close()
open("02_sql_intermediario/subqueries_ctes.sql", "w").close()
open("03_transacoes_otimizacao/transacoes_acid.sql", "w").close()
open("03_transacoes_otimizacao/explain_indices.sql", "w").close()
open("05_flask_api_relacional/app.py", "w").close()
open("05_flask_api_relacional/models.py", "w").close()
open("05_flask_api_relacional/requirements.txt", "w").close()
open("06_mongodb/crud_mongo.py", "w").close()
open("07_redis_cache/redis_basico.py", "w").close()
open("07_redis_cache/cache_api.py", "w").close()
