import asyncio
import telegram

# Configura el token del bot y el chat ID de destino
bot_token = '5723725362:AAHM-OxcJdcZSBEN-DA4wXSE13PPmND3irE'
chat_id = '-929326885'

# Crea el objeto bot
bot = telegram.Bot(token=bot_token)

last_message = ""

async def send_logs():
    global last_message

    # Lee el contenido del archivo de log
    with open('logfile.txt', 'r') as f:
        log_text = f.read()

    # Si el texto del log es diferente al último mensaje enviado, enviar el mensaje
    if log_text != last_message:
        # Divide el texto en líneas y envía cada línea como un mensaje separado
        log_lines = log_text.split('\n')
        for line in log_lines:
            if line.strip() != "":
                try:
                    await bot.send_message(chat_id=chat_id, text=line)
                except telegram.error.TimedOut:
                    print("Timed out while sending message. Retrying in next iteration.")

        # Actualiza la variable last_message
        last_message = log_text

    # Borra el contenido del archivo de log
    open('logfile.txt', 'w').close()
    await asyncio.sleep(10)


while True:
    try:
        # Llama a la función asincrónica
        asyncio.run(send_logs())
    except Exception as e:
        print(f"Error: {e}. Retrying in next iteration.")
    # Espera 10 segundos antes de volver a llamar a la función
