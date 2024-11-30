import telebot
import datetime
import random
import time
import threading


bot = telebot.TeleBot("7431785626:AAE-W9Z45IZ8Ux9DFsJdqZ3jJvPdmnJgqwU")

@bot.message_handler(commands=['start'])

def start_message(message):
    bot.reply_to(message, 'Привет! Я чат бот, который будет напоминать тебе включать голову!')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))

    reminder_thread.start()

@bot.message_handler(commands=['help'])

def help_message(message):
    bot.reply_to(message, 'Напишите ващи вопросы администратору сюда адресс')

@bot.message_handler(commands=['fact'])
def fact_message(message):



    list = ["**Улучшение решения проблем**: Включение головы позволяет более эффективно анализировать ситуации и принимать взвешенные решения. Это помогает находить оптимальные решения как в работе, так и в повседневных задачах.",
"**Развитие креативности и инноваций**: Когда мы включаем голову, мы стимулируем креативное мышление. Это позволяет находить нестандартные подходы и предлагать инновационные решения в различных сферах, будь то наука, искусство или бизнес.",
"*Укрепление уверенности и независимости*: Включение головы помогает нам полагаться на собственные аналитические способности, что укрепляет уверенность в своих суждениях. Это способствует развитию независимости, так как мы меньше зависим от чужого мнения и способны принимать обоснованные решения самостоятельно.",]

    random_fact = random.choice(list)

    bot.reply_to(message, f'Лови факт о включении головы {random_fact}')

def send_reminders(chat_id):
    first_rem = "12:00"
    second_rem = "14:00"
    end_rem = "18:29"

    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        #print (now)
        if now == first_rem or now == second_rem or now == end_rem:
            bot.send_message(chat_id, "Напоминание - Включи ГОЛОВУ!")

            time.sleep(61)

        time.sleep(1)

bot.polling(none_stop=True)