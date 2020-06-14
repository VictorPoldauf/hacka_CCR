from app import app,MessagingResponse,request
from dao import *
import time

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    msg_quebrada = msg.split(',')
    msg_quebrada = msg_quebrada[0]
    cliente_number = request.form.get('From').split(':')
    cliente_number = cliente_number[1]
    print(cliente_number)
    resp = MessagingResponse()
    #Mensagem de boas vinda 
    if msg == ('Oi'):
        resp.message('Bem vindo caminhoneiro! \nPara saber oque eu posso fazer digite *Ajuda* e envie ')
    elif msg == ('OI'):
        resp.message('Bem vindo caminhoneiro! \nPara saber oque eu posso fazer digite *Ajuda* e envie ')
    elif msg == ('Ajuda'):
        resp.message('Aqui esta uma lista doque eu posso fazer por você meu consagrado:')
        time.sleep(2)
        resp.message('Cadastrar você no clube de pontos, onde voce recebe beneficios exclusivos da CCR envie *Cadastrar* e te farei algumas perguntas')
        time.sleep(2)
        resp.message('Que tal uma lista de melhores postos de parada perto de você? Envie *Paradas*')
        time.sleep(2)
        resp.message('Quer saber quantos ponstos você tem no nosso sitema? envie a palavra *Pontos*')
        time.sleep(5)
        consulta = consultar(cliente_number)
        if consulta:
            resp.message('Voce ja esta cadastrado na nossa comunidade')
        else:
            resp.message('Voce ainda não é cadastrado para se cadastrar basta enviar *Cadastrar*')
    elif msg == ('AJUDA'):
        resp.message('Aqui esta uma lista doque eu posso fazer por você meu consagrado:\nCadastrar você no clube de pontos, onde voce recebe beneficios exclusivos da CCR envie *Cadastrar* e te farei algumas perguntas\nQue tal uma lista de melhores postos de parada perto de você? Envie *Paradas*\nQuer saber quantos ponstos você tem no nosso sitema? envie a palavra *Pontos*')
    elif msg == ('Cadastrar'):
        resp.message('Mande uma mensagem no formato:\nCadastrando, *nome* , *Sigla do estado* , *cidade* , *Autonomo ou CLT* , *Fabricante do caminhão* , *0* , *Sua idade* , *Sexo: M/F/Outros*')
    elif msg_quebrada == 'Cadastrando':
        mensagem_total = msg.split(',')
        salvar(cliente_number,mensagem_total[1],mensagem_total[2],mensagem_total[3],mensagem_total[4],mensagem_total[5],mensagem_total[6],mensagem_total[7],mensagem_total[8])
    else:
        pass





    # if msg == 'Sou caminhoneiro':
    #     resp = MessagingResponse()
    #     resp.message('Siga bem caminhoneiro')
    # else:
    #     resp = MessagingResponse()
    #     resp.message('Vai procurar um grupo de motoqueiro')


    # Create reply
    return str(resp)