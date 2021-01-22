import requests
import traceback
import json
from flask import Flask, request

token = "EAAFZCiTBka90BAAwfYJCZBYdbxZCMQDWbgWmhuJ8udZAzN6DOpZABuQby54ZCU6BL4596rEd8ZAiWk3swvOwcxMmTss2ypmiWwddm9jrRZAM6ZACFo3SpSC2coUJnu0AhxZC6rSGHI1KCP6bd467gmqZAo64mBZBhrPXYXYIKLZC3jdfxd2dZBx6i5RgYL"
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        try:
            data = json.loads(request.data.decode())
            text = data['entry'][0]['messaging'][0]['message']['text']
            sender = data['entry'][0]['messaging'][0]['sender']['id']

            if text == "Olá":
                payload = {'recipient': {'id': sender}, 'message': {'text': "Olá, tudo bem com você?"}}
            elif text == "Tudo bem":
                payload = {'recipient': {'id': sender}, 'message': {'text': "Que bom! Em que posso ajudar hoje?"}}
            elif text == "Qual carro devo comprar?":
                payload = {'recipient': {'id': sender}, 'message': {'text': "Eu prefiro o Yaris ou o Rio. São os que mais valem a pena"}}
            elif text == "Quanto é o seguro do Yaris?":
                payload = {'recipient': {'id': sender}, 'message': {'text': "Em média varia da versão mas fica em torno dos R$1.500"}}
            elif text == "Obrigada":
                payload = {'recipient': {'id': sender}, 'message': {'text': "De nada, disponha! Volte sempre!"}}
            elif text == "Bom dia":
                payload = {'recipient': {'id': sender}, 'message': {'text': "Bom dia!!!"}}
            else:
                payload = {'recipient': {'id': sender}, 'message': {'text': "Não tenho a resposta."}}

            r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + 'EAAFZCiTBka90BAAwfYJCZBYdbxZCMQDWbgWmhuJ8udZAzN6DOpZABuQby54ZCU6BL4596rEd8ZAiWk3swvOwcxMmTss2ypmiWwddm9jrRZAM6ZACFo3SpSC2coUJnu0AhxZC6rSGHI1KCP6bd467gmqZAo64mBZBhrPXYXYIKLZC3jdfxd2dZBx6i5RgYL', json=payload)
        except Exception as e:
            print(traceback.format_exc())
    elif request.method == 'GET': # Para a verificação inicial (configuração facebook)
        if request.args.get('hub.verify_token') == 'teste@123':
            return request.args.get('hub.challenge')
        return "Token Inválido"
    return "Nada a retornar"

if __name__ == '__main__':
    app.run(debug=True)