#!/usr/bin/env python3

from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')

nltk.download('punkt', quiet=True)

article = Article('https://g1.globo.com/ciencia-e-saude/noticia/2019/05/09/missao-dart-o-plano-da-nasa-para-desviar-asteroides.ghtml')
article.download()
article.parse()
article.nlp()
corpus = article.text

#print(corpus)

text = corpus

sentence_list = nltk.sent_tokenize(text)

#print(sentence_list)

def greeting_response(text):
    text = text.lower()
    bot_greetings = ['howdy', 'wassup', 'greetings', 'hola', 'hello', 'hi', 'oi', 'olá', 'ola']
    user_greetings = ['howdy', 'wassup', 'greetings', 'hola', 'hello', 'hi', 'oi', 'olá', 'ola']
    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)

def index_sort(list_var):
    lenght = len(list_var)
    list_index = list(range(0, lenght))

    x = list_var

    for i in range(lenght):
        for j in range(lenght):
            if x[list_index[i]] > x[list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index

def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
 #   print(similarity_scores_list)
  #  print(index)
    index = index[1:]
    response_flag = 0


    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response+' '+sentence_list[index[i]]
            response_flag = 1
            j = j+1
        if j > 2:
            break

    if response_flag == 0:
        bot_response = bot_response+''+'me desculpe, ainda nao estou pronto pra essa conversa'

    sentence_list.remove(user_input)

    return bot_response


print("""
Bom dia! sou o teste de argumentação, do robo que ainda não tem corpo...
mas eu já tenho um pouco de inteligencia artificial.
sou alimentado por uma URL, que é um endereço de site na internet, como por exemplo https://www.cnn.com/, um site de noticias internacional.
ainda estou pensando em um jeito de aprender de multiplos sites, mas por enquanto, posso tentar ajudar com um site de cada vez.
tente editar o arquivo urlconf com a url desejada, mas nao garanto que irá funcionar.
se nao estiver funcionando, peça para o Kevin verificar o metodo que lê do arquivo.
me pergunte algo sobre o site/artigo escolhido, ou digite fechar para sair:
        """)

exit_list = ['exit', 'bye', 'tchau', 'fechar']
whats_your_name_list = ['qual o seu nome?', 'como voce se chama?', 'qual seu nome?', 'what is your name', 'what\'s your name', 'qual é sua graça?']
while(True):
    user_input = input('entre com mensagem: ')
    if user_input.lower() in exit_list:
        print('fechando assistente')
        break
    elif user_input.lower() in whats_your_name_list:
        print('meu nome é caleb')
    else:
        if greeting_response(user_input) != None:
            print('assistente: ', greeting_response(user_input))
        else:
            print('assistente:', bot_response(user_input))
#bot_response('menor')

