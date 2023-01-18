import telebot
from telebot import types
from bs4 import BeautifulSoup
import requests


api_token = '5631034261:AAE_E7aSmTiQMug0ikyW4srwkVsSX24Xaks'

bot = telebot.TeleBot(api_token)

def usd():
    url = 'https://finance.rambler.ru/currencies/USD/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    result = soup.find('div', class_="finance-currency-plate__currency")
    return result.text
def eur():
    url = 'https://finance.rambler.ru/currencies/EUR/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    result = soup.find('div', class_="finance-currency-plate__currency")
    return result.text
def cn():
    url = 'https://finance.rambler.ru/currencies/CNY/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    result = soup.find('div', class_="finance-currency-plate__currency")
    print(result.text)
    return result.text


@bot.message_handler(commands=['start'])
def get_weather(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Спроси меня')
    btn2 = types.KeyboardButton('Курс денег')
    markup.add(btn1,btn2)
    bot.send_message(message.chat.id,'Меня создал крутой программист',reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text_text(message):
    if message.text == 'Спроси меня':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Хто ты?')
        btn2 = types.KeyboardButton('Что ты можешь? ')
        back = types.KeyboardButton('Вернуться на главную')
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id,'Что ты хочешь спросить?',reply_markup=markup)
    if message.text =='Хто ты?':
        bot.send_message(message.chat.id,'Генералисимус')
    if message.text == 'Что ты можешь?':
        bot.send_message(message.chat.id,'Я показать курс валют')
    if message.text == 'Вернуться на главную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Спроси меня')
        btn2 = types.KeyboardButton('Курс денег')
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id,'Ты вернулся на главную',reply_markup=markup)

    if message.text =="Курс денег":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('USD')
        btn2 = types.KeyboardButton('EUR')
        btn3 = types.KeyboardButton("CNY")
        back = types.KeyboardButton("Вернуться на главную")
        markup.add(btn1,btn2,btn3,back)
        bot.send_message(message.chat.id,'Выбери Валюту',reply_markup=markup)

    if message.text == 'USD':
        bot.send_message(message.chat.id,f'Доллар: {usd()}')
    if message.text =='EUR':
        bot.send_message(message.chat.id,f'EURO: {eur()}')
    if message.text == 'CNY':
        bot.send_message(message.chat.id,f'CNY: {cn()}')
    if message.text == 'Вернуться на главную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Спроси меня')
        btn2 = types.KeyboardButton('Курс денег')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, 'Ты вернулся на главную', reply_markup=markup)

bot.polling(none_stop=True)



