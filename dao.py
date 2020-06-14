import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="he comes the sun",
  database="crr_bot"

  
)

def salvar (NUMERO_DE_TELEFONE, NOME, ESTADO, CIDADE_NATAL, REGIME_DE_TRABALHO, MARCA_DO_CAMINHAO, PONTOS, IDADE, SEXO ):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tbclientes(NUMERO_DE_TELEFONE, NOME, ESTADO, CIDADE_NATAL, REGIME_DE_TRABALHO , MARCA_DO_CAMINHAO , PONTOS, IDADE,SEXO) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(NUMERO_DE_TELEFONE, NOME, ESTADO, CIDADE_NATAL, REGIME_DE_TRABALHO, MARCA_DO_CAMINHAO, PONTOS, IDADE,SEXO))
    conn.commit()   
    return

def consultar (numero):
    cursor = conn.cursor()
    sql = "SELECT * FROM tbclientes WHERE NUMERO_DE_TELEFONE = '{}'".format(numero)
    cursor.execute(sql)
    myresult = cursor.fetchall()
    conn.commit()
    if len(myresult) >= 1:
        return True
    return False