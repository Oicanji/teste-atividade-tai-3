from html import escape

from flask import Flask
from flask import request, Response, jsonify
from classes.Pessoa import Pessoa

app = Flask("meu sitezinho")

@app.route("/todas-citacoes", methods=["GET"])
def todas_citacoes():
    return jsonify(lista_citacoes)


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


@app.route("/teste")
def teste():
    return "Rota teste OK"

# curl http://127.0.0.1:5000/teste


lista_pessoas: list[Pessoa] = [Pessoa("Andre", 30, "Brasileiro", "Professor"), Pessoa("Ignacio", 25, "Chileno", "Desenvolvedor")]
lista_citacoes: list[str] = []

def adicionar_citacao(pessoa: Pessoa, citacao: str):
    lista_citacoes.append(f"{pessoa.nome} - {citacao}")

adicionar_citacao(lista_pessoas[0], "No meu computador sempre funciona.")
adicionar_citacao(lista_pessoas[1], "O erro está entre o teclado e o assento.")
adicionar_citacao(lista_pessoas[0], "Não fui eu, foi a IA :v")
adicionar_citacao(lista_pessoas[1], "Tá, mas já tentou reiniciar seu roteador?")
adicionar_citacao(lista_pessoas[0], "Se ouver um erro, é só pressionar ctrl + shift + f4 varias vezes.")
adicionar_citacao(lista_pessoas[1], "PHP é a melhor linguagem de programação do mundo.")
adicionar_citacao(lista_pessoas[0], "Temos que dar um while no bug para que ele seja resolvido.")
adicionar_citacao(lista_pessoas[1], "Tá mas é no webalgo, ces viram isso né?")


@app.route("/")
def index():
    itens = ""
    for entrada in lista_citacoes:
        if not entrada:
            continue
        partes = entrada.split(" - ", 1)
        nome = partes[0]
        texto = partes[1] if len(partes) > 1 else ""
        itens += f"""
        <li>
            <blockquote>&ldquo;{escape(texto)}&rdquo;</blockquote>
            <footer>&mdash; {escape(nome)}</footer>
        </li>"""

    return f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Citações</title>
            <style>
                body {{ font-family: Georgia, serif; max-width: 40rem; margin: 2rem auto; padding: 0 1rem;
                    line-height: 1.5; color: #1a1a1a; background: #fafafa; }}
                h1 {{ font-weight: 600; border-bottom: 2px solid #2c5282; padding-bottom: 0.35rem; }}
                h2 {{ font-size: 1.15rem; color: #2d3748; margin-top: 2rem; }}
                ul.citacoes {{ list-style: none; padding: 0; margin: 0; }}
                ul.citacoes li {{ margin: 1.25rem 0; padding: 1rem 1.25rem; background: #fff;
                    border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,.08); border-left: 4px solid #2c5282; }}
                blockquote {{ margin: 0 0 0.5rem 0; font-style: italic; }}
                footer {{ font-size: 0.9rem; color: #4a5568; }}
            </style>
        </head>
        <body>
            <h1>Minha página inicial</h1>
            <p>Bem-vindo ao meu site de citações</p>
            <div>
                <h2>Lista de pessoas e suas citações</h2>
                <ul class="citacoes">{itens}</ul>
            </div>
        </body>
    </html>
    """



@app.route("/pessoa", methods=["POST"])
def post_pessoa():
    nome = request.json["nome"]
    idade = request.json["idade"]
    nacionalidade = request.json["nacionalidade"]
    profissao = request.json["profissao"]
    nova_pessoa = Pessoa(nome, idade, nacionalidade, profissao)
    lista_pessoas.append(nova_pessoa)
    
    return Response(jsonify(nova_pessoa.to_dict()), status=201)

# curl -X POST http://127.0.0.1:5000/pessoa -H "Content-Type: application/json" -d "{\"nome\":\"Fulano\",\"idade\":30,\"nacionalidade\":\"Brasileiro\",\"profissao\":\"Dev\"}"

@app.route("/pessoa", methods=["GET"])
def get_pessoas():
    texto = ""
    for pessoa in lista_pessoas:
        texto += pessoa.todas_citacoes() + "\n"

    return texto

# curl http://127.0.0.1:5000/pessoa

app.run(host="0.0.0.0", port=5000)
