import openai
import keys

api_key = keys.openai.api_key
bot_api = keys.bot


@bot_api.message_handler(func=lambda message: True)
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
    bot_api.send_message(chat_id=message.from_user.id, text=response["choices"][0]["text"])


bot_api.polling()

