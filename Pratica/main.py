# 1 --> ouvir
# 2 --> pensar
# 3 --> responder

from google import search

# abrir facebook
def buscar():
    chave = input("Digite a sua busca: ")
    for result in search(chave, stop=10):
        print(result)

#ouvir
def ouvir():
    return input("Digite algo: ")

# pensar / analisar mensagem
def pensar(mensagem):
    if mensagem == "Oi":
        resposta = "Ola, como vai?"

    elif mensagem == "Ola":
        resposta = "Oi, como você esta?"

    elif mensagem == "sair":
        print("Até mais chefe!")
        exit()

    elif mensagem == "buscar":
        buscar()

    else:
        resposta = "Desculpe, eu não consegui entender!"

    return resposta

# falar
def falar(mensagem, resposta):
    print("Você: " + mensagem)
    print("------------------------")
    print("Chat: " + resposta + "\n")

# main loop
while True:
    mensagem = ouvir()
    resposta = pensar(mensagem)
    falar(mensagem, resposta)
    