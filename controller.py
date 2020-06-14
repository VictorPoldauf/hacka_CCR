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
        time.sleep(2)
        resp.message("Será que o frete vale a pena ? te ajudo a calcular basta você me enviar *Frete*  e te digo como ")
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
    elif msg == ('Paradas'):
        resp.message('Escreva para mim a sigla do seu estado, exemplo: *SP*')
    elif msg == ('SP'):
        resp.message('As paradas de SP são:\nTRANSBRASILIANA BR-153/SP Divisa MG/SP - Divisa SP/PR *nota: 3.8*\nNOVADUTRA BR-116/RJ/SP Rio de Janeiro/RJ - São Paulo/SP *nota: 3.2*')
    elif msg == ('RJ'):
        resp.message('As paradas de SP são:CONCER BR-040/MG/RJ Rio de Janeiro/RJ - Juiz de Fora/MG  *nota: 4.0*\nCRT BR-116/RJ Rio de Janeiro/RJ - Teresópolis/RJ – Além Paraíba/MG *nota: 3.9*\nFLUMINENSE BR-101/RJ Divisa RJ/ES – Ponte Presidente Costa e Silva\nRODOVIA DO AÇO BR-393/RJ Divisa MG/RJ - Entr.BR-116*nota: 2.6*')
    elif msg == ('Frete'):
        resp.message('Informe o tipo de carga, distacia (km) e numero de eixos\nExemplo-> Transporte, Carga Frigorifica,300 , 2')
    elif msg_quebrada == 'Transporte':
        mensagem_total = msg.split(',')
        tipo_de_carga = mensagem_total[1]
        distancia = mensagem_total[2]
        n_de_eixos = mensagem_total[3]
        const = 2.8788
        valor = const*int(distancia)
        resp.message("O valor minimo do frete é de *R${}* para um frete tipo {} à {} km de distancia com {} eixos".format(valor,tipo_de_carga,distancia,n_de_eixos))  
    else:
        resp.message("Não entendi oque voce disse poderia digita me enviar a palavra Ajuda e seguir nossas onstruções")
    return str(resp)