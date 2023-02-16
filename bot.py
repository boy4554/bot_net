import telegram
import datetime


# Configurações do Bot
TOKEN = "5533392014:AAFqC8Pzliv_2gFzfOAD2nR3FLvNfD4rYmk"
CHAT_ID = '1698409133'

# Cria o objeto do Bot
bot = telegram.Bot(token="5533392014:AAFqC8Pzliv_2gFzfOAD2nR3FLvNfD4rYmk")
CHAT_ID = "1698409133"
atendimentos = {}

def registrar_atendimento():
    print("Registrando atendimento...")
    data = datetime.date.today().strftime("%d/%m/%Y")
    cliente = input("Nome do cliente: ")
    problema = input("Descrição do problema: ")
    os = input("Necessário abrir ordem de serviço? (S/N) ")
    if os.upper() == "S":
        os = "Sim"
    else:
        os = "Não"
    resolvido_remotamente = input("O problema foi resolvido remotamente? (S/N) ")
    if resolvido_remotamente.upper() == "S":
        resolvido_remotamente = "Sim"
    else:
        resolvido_remotamente = "Não"
    atendimentos[data] = {"cliente": cliente, "problema": problema, "os": os, "resolvido_remotamente": resolvido_remotamente}
    print("Atendimento registrado com sucesso!")

def exibir_relatorio():
    print("Exibindo relatório de atendimentos...")
    relatorio = "Relatório de atendimentos:\n\n"
    for data, atendimento in atendimentos.items():
        relatorio += f"Data: {data}\n"
        relatorio += f"Cliente: {atendimento['cliente']}\n"
        relatorio += f"Problema: {atendimento['problema']}\n"
        relatorio += f"Necessário abrir ordem de serviço? {atendimento['os']}\n"
        relatorio += f"Resolvido remotamente? {atendimento['resolvido_remotamente']}\n"
        relatorio += "\n"
    bot.send_message(chat_id=CHAT_ID, text=relatorio)

# Menu principal
while True:
    print("1 - Registrar atendimento")
    print("2 - Exibir relatório de atendimentos")
    print("3 - Sair")
    opcao = input("Digite uma opção: ")
    if opcao == "1":
        registrar_atendimento()
    elif opcao == "2":
        exibir_relatorio()
    elif opcao == "3":
        break
    else:
        print("Opção inválida. Digite novamente.")
