from flask import Flask

# criando uma aplicação flask

app = Flask(__name__)

# rota para a página inicial


@app.route("/")
def hello():
    return "Bem vindo ao back-end simples com Flask!"


# executa a aplicação no host e na porta especificados
if __name__ == "__main__":
    app.run(host="localhost", port=5000)
