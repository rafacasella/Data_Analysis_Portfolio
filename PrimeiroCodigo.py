import os
from dotenv import load_dotenv

# Carrega o arquivo .env da raiz
load_dotenv()

# Tenta ler a senha que você salvou lá dentro
senha_banco = os.getenv("DB_PASSWORD")

if senha_banco:
    print(f"Sucesso! O Python conseguiu ler o arquivo .env.")
    print(f"Sua senha começa com: {senha_banco[0]}... (escondida por segurança)")
else:
    print("Erro: O Python não encontrou o arquivo .env ou a variável DB_PASSWORD.")
