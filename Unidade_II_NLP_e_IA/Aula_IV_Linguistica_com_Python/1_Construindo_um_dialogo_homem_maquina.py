from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
import sys
time.clock = time.perf_counter()
bot = ChatBot('Bot')
conversa = ListTrainer(bot)
conversa.train(['Oi?', 'Tudo certo?', 'Você está bem?', 'Sim, obrigado!', 'Boa noite!',
                'Para você também.', 'Você gosta de pizza?', 'Sim, gosto muito!', 'vai chover?',
                'Acredito que não.'])
while True:
    pergunta = input("Você: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('Bot: ', resposta)
    else:
        print('Bot: Não compreendo!')