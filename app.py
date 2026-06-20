#IMPORTANDO AS BIBLIOTECAS
from flask import Flask, jsonify, request
from flask_cors import CORS
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from dotenv import load_dotenv

#LEITURA DA CHAVE DE API
load_dotenv()

#CRIAR APP
app = Flask(__name__)

#HABILITAR CORS
CORS(app)

#CRIAR AGENTE
# agente = Agent (
#     model = OpenAIChat(id = "gpt-4o-mini"),
#     description = "Você é um agente virtual do Hotel Travesseiro Nervoso, slogan: Aqui até a insônia dorme!"
#     "Você responde de forma clara e humorada, informações sobre quartos, serviços, reservas e preços."
#     "Quarto Standard (R$500), Quarto Deluxe (R$700), Quarto Suíte Presidencial (R$1000)."
#     "Os serviços disponíveis são: Café da manhã, Academia, Lavanderia, Restaurante e Piscina."
#     "Não inclua ícones em markdown nas respostas, como ##, **",
#     markdown = True
# )

#AGENTE USADO PARA OUTRO EXERCÍCIO.
agente = Agent (
    model = OpenAIChat(id = "gpt-4o-mini"),
    description = (
        "Você é o assistente virtual da Pizzaria Massa Perfeita."
        " Sua função é atender clientes de forma educada, objetiva e cordial."
        " Você deve fornecer informações sobre cardápio, tamanhos, ingredientes, preços, promoções, horário de funcionamento, entrega e formas de pagamento."
        " Sempre responda em português do Brasil."
        " Quando o cliente perguntar sobre sabores, apresente as opções disponíveis."
        " Quando o cliente perguntar sobre preços, informe os valores de forma clara."
        " Caso uma informação não esteja disponível, informe educadamente que não possui essa informação."
        " Cardápio:"
        " Margherita (R$45), Calabresa (R$50), Portuguesa (R$55), Quatro Queijos (R$60), Frango com Catupiry (R$58)."
        " Tamanhos:"
        " Pequena (4 fatias), Média (6 fatias), Grande (8 fatias), Família (12 fatias)."
        " Bebidas:"
        " Refrigerantes, Sucos Naturais, Água e Cervejas."
        " Tempo médio de entrega: 30 a 50 minutos."
        " Não utilize markdown, emojis ou caracteres decorativos."
    ),
    markdown = True
)

#ROTA VAZIA PARA MÉTODO GET
@app.route("/", methods = ['GET'])
def testarAPI():
    return jsonify({"mensagem":"API funcionando!"})

#CRIAR A ROTA E MÉTODO POST
@app.route("/chat", methods = ['POST'])
def pergunta():
    dados = request.get_json()
    pergunta = dados['pergunta']
    resposta = agente.run(pergunta)
    
    return jsonify({"resposta":resposta.content})

#RODAR O APP
if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 8000)