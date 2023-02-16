import telegram
from telegram.ext import Updater, CommandHandler
import datetime

# Configurações do Bot
TOKEN = "5533392014:AAFqC8Pzliv_2gFzfOAD2nR3FLvNfD4rYmk"
CHAT_ID = "1698409133"

atendimentos = {}

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Olá! Eu sou o seu bot de atendimento. Digite /ajuda para ver a lista de comandos disponíveis.")

def ajuda(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Os comandos disponíveis são:\n/registrar - Registrar um novo atendimento\n/relatorio - Exibir o relatório de atendimentos")

def registrar(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Registrando atendimento...")
    data = datetime.date.today().strftime("%d/%m/%Y")
    cliente = update.message.text.replace("/registrar ", "")
    atendimentos[data] = {"cliente": cliente}
    context.bot.send_message(chat_id=update.message.chat_id, text="Atendimento registrado com sucesso!")

def exibir_relatorio(update, context):
    relatorio = "Relatório de atendimentos:\n\n"
    for data, atendimento in atendimentos.items():
        relatorio += f"Data: {data}\n"
        relatorio += f"Cliente: {atendimento['cliente']}\n"
        relatorio += "\n"
    context.bot.send_message(chat_id=update.message.chat_id, text=relatorio)

# Cria o objeto do Bot
updater = Updater(TOKEN, use_context=True)

# Cria os handlers dos comandos
start_handler = CommandHandler('start', start)
ajuda_handler = CommandHandler('ajuda', ajuda)
registrar_handler = CommandHandler('registrar', registrar)
relatorio_handler = CommandHandler('relatorio', exibir_relatorio)

# Adiciona os handlers ao dispatcher
dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(ajuda_handler)
dispatcher.add_handler(registrar_handler)
dispatcher.add_handler(relatorio_handler)

# Inicia o bot
updater.start_polling()
