from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    cliente = request.form.get('From')
    print(cliente)
    resp = MessagingResponse()
    #Mensagem de boas vinda 
    if msg == ('Oi'):
        resp.message('Bem vindo caminhoneiro! \nPara saber oque eu posso fazer digite *Ajuda* e envie ')
    elif msg == ('OI'):
        resp.message('Bem vindo caminhoneiro! \nPara saber oque eu posso fazer digite *Ajuda* e envie ')
    elif msg == ('Ajuda'):
        resp.message('Aqui esta uma lista doque eu posso fazer por você meu consagrado:')
        resp.message('Cadastrar você no clube de pontos, onde voce recebe beneficios exclusivos da CCR envie *Cadastrar* e te farei algumas perguntas')
        resp.message('Que tal uma lista de melhores postos de parada perto de você? Envie *Paradas*')
        resp.message('Quer saber quantos ponstos você tem no nosso sitema? envie a palavra *Pontos*')
        #Consulta 
        #if 
    elif msg == ('AJUDA'):
        resp.message('Aqui esta uma lista doque eu posso fazer por você meu consagrado:\nCadastrar você no clube de pontos, onde voce recebe beneficios exclusivos da CCR envie *Cadastrar* e te farei algumas perguntas\nQue tal uma lista de melhores postos de parada perto de você? Envie *Paradas*\nQuer saber quantos ponstos você tem no nosso sitema? envie a palavra *Pontos*')
    elif msg == ('Cadastrar'):
        resp.message('Bem vindo caminhoneiro! \nPara saber oque eu posso fazer digite *Ajuda* e envie ')
    else:
        resp.message('Não')





    # if msg == 'Sou caminhoneiro':
    #     resp = MessagingResponse()
    #     resp.message('Siga bem caminhoneiro')
    # else:
    #     resp = MessagingResponse()
    #     resp.message('Vai procurar um grupo de motoqueiro')


    # Create reply
    

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True,port=8080)