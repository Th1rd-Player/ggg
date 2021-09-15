#!venv/bin/python


import logging


from aiogram import Bot, Dispatcher, executor, types

import os

# Объект бота

bot = Bot(token="1948363184:AAGWeoRpx_XiO5H41glKGaR7FB2g4A_fUQs")

# Диспетчер для бота

dp = Dispatcher(bot)

# Включаем логирование, чтобы не пропустить важные сообщения

logging.basicConfig(level=logging.INFO)

import paramiko





@dp.message_handler()

async def hh(message : types.Message):
	
	com = message.text
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect('185.22.153.234', username='root', password='08092005')

	
	stdin, stdout, stderr = client.exec_command(com)
	
	for line in stdout:
		
		await message.reply(line.strip('\n'))
	







#client.close()

if __name__ == "__main__":
    
    # Запуск бота
    
    executor.start_polling(dp, skip_updates=True)