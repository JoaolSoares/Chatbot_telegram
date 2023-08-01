from	defines			import *
from	telebot.types	import InlineKeyboardMarkup, InlineKeyboardButton


@bot.callback_query_handler(func=lambda message: True)
def callback(call):
    user = User(call.from_user.id, call.from_user.first_name)
    if call.data == 'MENU_1':
        bot.edit_message_text(
			chat_id				=user.id,
			message_id			=call.message.id,
            text				="Escolha o Paciente:",
			reply_markup		=patientsMarkup()
        )
        bot.answer_callback_query(call.id)
    else:
        print("pegar dados dos pacientes no s3")
        bot.answer_callback_query(call.id)


def patientsMarkup():
	markup = InlineKeyboardMarkup(row_width=1)
	objects = s3.list_objects_v2(Bucket=bucket, Prefix="app/users/", Delimiter="/")
	if 'CommonPrefixes' in objects:
		for obj in objects['CommonPrefixes']:
			parts = obj['Prefix'].split('/')
			markup.add(InlineKeyboardButton(parts[2], callback_data=parts[2])) # pegar nomes ao inves dos codigos
	return markup


def menuMarkup():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("Pacientes", callback_data='MENU_1')
    )
    return markup

