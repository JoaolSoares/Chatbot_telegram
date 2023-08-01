from	defines		import *
from	callback	import menuMarkup


@bot.message_handler(commands=['start'])
def commandStart(message):
    user = User(message.from_user.id, message.from_user.first_name)
    bot.send_message(
        chat_id			=user.id,
		text			=f"Olá {user.name}!\nBem-Vindo ao menu da Luna!\nEscolha uma opção para prosseguir:",
		reply_markup	=menuMarkup()
    )

# @bot.message_handler(commands=[''])
    
if __name__ == "__main__":
    bot.infinity_polling()
