import openai
import telebot

openai.api_key = "sk-ZJavI6qH1LGrN2322Bb3K49XT3BlbkFJT8M5sddfgdfdweweYMI38kzIHA6z6o"
bot = telebot.TeleBot("5965873984:AAF2niWb88VUhNJus-Ry0bswqw3442NUw1RXN553VJmyaQ")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=1500,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    print(message)
    bot.send_message(chat_id=message.from_user.id, text=response["choices"][0]["text"])


bot.polling()

