import time
import datetime
import telepot


def handle(msg):
    bot.getFile()
    flavor = telepot.flance(msg)
    summary = telepot.glance(msg, flavor=flavor)
    print(flavor, summary)

    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Got command: %s' % command)

    if command == "/time":
        print(chat_id)
        bot.sendMessage(chat_id, str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute))


    elif command == "/cuandotepasa":
        print(chat_id)
        bot.sendMessage(chat_id, "si xD")

    elif command == "/conejo":
        print(chat_id)
        f = open('conejo.jpg', 'rb')  # some file on local disk
        bot.sendPhoto(chat_id, f)
        #bot.sendPhoto(chat_id, "D:/WorkspacePython/PycharmProyects/untitled/conejo.jpg")

    elif command == "/conejo_noel":
        print(chat_id)
        f = open('conejo_navideño.jpg', 'rb')  # some file on local disk
        bot.sendPhoto(chat_id, f)
        #bot.sendPhoto(chat_id, "D:/WorkspacePython/PycharmProyects/untitled/conejo.jpg")

    elif command == "/alarma":
        if chat_id in listaAlarma:
            listaAlarma.remove(chat_id)
        else:
            listaAlarma.add(chat_id)

    elif command == "/loquillo":
        if chat_id in listaLoquillo:
            listaLoquillo.remove(chat_id)
        else:
            listaLoquillo.add(chat_id)

    elif command == "/si":
        bot.sendSticker(chat_id, "BQADBAADvAIAAv6P5AGo7ISktATscwI") #no funciona aun

bot = telepot.Bot('227228541:AAFTcfqGjIH0-bKn7uSpWYvsdpK8ARDGero')
bot.message_loop(handle)
listaAlarma = set()
listaLoquillo = set()

print ('I am listening ...')

while 1:
    print(listaAlarma)
    print("^ ala")
    print(listaLoquillo)
    print("^ loq")
    if not listaLoquillo:
        time.sleep(10)
       # hora = str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)
        minute = datetime.datetime.now().minute
        if minute == 0:
            for id in listaAlarma:
                bot.sendMessage(id, ".")
        #alarma cada hora en punto.
    else:
        time.sleep(2)
        for id in listaLoquillo:
            bot.sendMessage(id, "¿Loquillo?")


#-5257768 ID Grupo Conejo
