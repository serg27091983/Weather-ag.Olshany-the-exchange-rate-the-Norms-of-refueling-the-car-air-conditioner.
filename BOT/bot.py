from ctypes import resize
from lib2to3.pgen2 import token
import telebot
from telebot import types
import requests, bs4
from bs4 import BeautifulSoup as BS
import seting

token = seting.token

url = ("https://sinoptik.ua/погода-давид-городок")   ##Сайт погоды!

html = requests.get(url)
html = BS(html.content, 'html.parser')

#########################################################################################################################  Погода на севодня

###################################################### Погода на ноч
for e in html.select(".weatherDetails"):
      night_t = e.select(".temperature .p1")
      night_t = str(str(night_t).split('>')[1]).split ("<")[0]

#######################################################################
for el in html.select("#bd1 > div.temperature"):

    tmin = el.select(" #bd1 > div.temperature > div.min > span")
    tmin = str(str(tmin).split('>')[1]).split('<')[0]

    tmax = el.select(" #bd1 > div.temperature > div.max > span ")
    tmax = str(str(tmax).split('>')[1]).split('<')[0]




for i in html.select("#blockDays > div.tabsContent > div"):
    infa = i.select(".description ")
    infa = str(str(infa).split('>')[2]).split('<')[0]

######################################################################################################################### дата менсяц
for e in html.select("#blockDays > div.tabs"):
    data = e.select(" #bd1")
for el in html.select("#bd1"):
    data = el.select('#bd1 > p.date ')
    data = str(str(data).split('>')[1]).split('<')[0]

    mes = el.select('#bd1 > p.month ')
    mes = str(str(mes).split('>')[1]).split('<')[0]

#########################################################################################################################  Погода на завтра
for el in html.select("#bd2 > div.temperature"):

    tmin_next = el.select(" #bd2 > div.temperature > div.min > span")
    tmin_next = str(str(tmin_next).split('>')[1]).split('<')[0]

    tmax_next = el.select(" #bd2 > div.temperature > div.max > span ")
    tmax_next = str(str(tmax_next).split('>')[1]).split('<')[0]


#########################################################################################################################  дата месяц завтра
for k in html.select("#blockDays > div.tabs"):
    data_next = k.select(" #bd2")
for k in html.select("#bd2"):

    data_next = k.select('#bd2 > p.date ')
   # print(data_next)
    data_next = str(str(data_next).split('>')[1]).split('<')[0]

    mes_next = k.select('#bd2 > p.month ')
    mes_next = str(str(mes_next).split('>')[1]).split('<')[0]


##################################################################################################
##################################################################################################
urlbank = ("https://belarusbank.by")   ####Сайт банк!

html = requests.get(urlbank)
html = BS(html.content, 'html.parser')

for e in html.select('body > main > div > div > div > div.home-page-block.home-page-block--sm.home-page-block--white.home-page-block--bg-7.col-lg-3.col-md-4.col-sm-6.col-2xs-12'):

    dolarprodaza = e.select(" body > main > div > div > div > div.home-page-block.home-page-block--sm.home-page-block--white.home-page-block--bg-7.col-lg-3.col-md-4.col-sm-6.col-2xs-12 > section > div > table > tbody > tr:nth-child(1) > td:nth-child(2)")
    dolarprodaza = str(str(dolarprodaza).split('>')[1]).split('<')[0]

    dolarpokupka = e.select("body > main > div > div > div > div.home-page-block.home-page-block--sm.home-page-block--white.home-page-block--bg-7.col-lg-3.col-md-4.col-sm-6.col-2xs-12 > section > div > table > tbody > tr:nth-child(1) > td:nth-child(3)")
    dolarpokupka = str(str(dolarpokupka).split('>')[1]).split('<')[0]

    evroprodaza = e.select(" body > main > div > div > div > div.home-page-block.home-page-block--sm.home-page-block--white.home-page-block--bg-7.col-lg-3.col-md-4.col-sm-6.col-2xs-12 > section > div > table > tbody > tr:nth-child(2) > td:nth-child(2)")
    evroprodaza = str(str(evroprodaza).split('>')[1]).split('<')[0]
    evropokupka = e.select("body > main > div > div > div > div.home-page-block.home-page-block--sm.home-page-block--white.home-page-block--bg-7.col-lg-3.col-md-4.col-sm-6.col-2xs-12 > section > div > table > tbody > tr:nth-child(2) > td:nth-child(3)")
    evropokupka = str(str(evropokupka).split('>')[1]).split('<')[0]

    ruprodaza = e.select(" body > main > div > div > div > div.home-page-block.home-page-block--sm.home-page-block--white.home-page-block--bg-7.col-lg-3.col-md-4.col-sm-6.col-2xs-12 > section > div > table > tbody > tr:nth-child(3) > td:nth-child(2)")

    ruprodaza = str(str(ruprodaza).split('>')[1]).split('<')[0]

    rupokupka = e.select("body > main > div > div > div > div.home-page-block.home-page-block--sm.home-page-block--white.home-page-block--bg-7.col-lg-3.col-md-4.col-sm-6.col-2xs-12 > section > div > table > tbody > tr:nth-child(3) > td:nth-child(3)")
    rupokupka = str(str(rupokupka).split('>')[1]).split('<')[0]

#########################################################################################################################################################################################################################################################################

condey_url = ("https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=58")    ##Сайт кондей!

condey = requests.get(condey_url)
condey = BS(condey.content, 'html.parser')


for i in condey.select('body > article > div > div > div > div.content-blog'):
    d = i.select('body > article > div > div > div > div.content-blog > ol:nth-child(12) > li:nth-child(1)')



bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Помощь')
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton('Нормы заправок авто кондиционера!')
        item3 = types.KeyboardButton('Курс валюты')
        item4 = types.KeyboardButton('Погода в Ольшанах')
        markup.add(item1, item2, item3, item4)
        markup_reply.add(item1,)

        bot.send_message(message.chat.id, 'Привет! '+ str(message.from_user.first_name), reply_markup = markup)
        bot.send_message(message.chat.id, 'прочтите инструкцию!', reply_markup = markup_reply)


@bot.message_handler(content_types=['text'])
def bot_message(message):

        if message.chat.type == 'private':

############################################################################################################################### КУРС ВАЛЮТЫ
             if message.text == 'Курс валюты':
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        item1 = types.KeyboardButton('Долар')
                        item2 = types.KeyboardButton('Евро')
                        item3 = types.KeyboardButton('Рубль')
                        item4 = types.KeyboardButton('ДОМОЙ')
                        markup.add(item1, item2, item3, item4)
                        bot.send_message(message.chat.id, 'Сделайте выбор!', reply_markup=markup)

             if message.text == 'Долар':
                 bot.send_message(message.chat.id, f'Покупка {dolarprodaza}')
                 bot.send_message(message.chat.id, f'Продажа {dolarpokupka}')
             if message.text == 'Евро':
                 bot.send_message(message.chat.id, f'Покупка {evroprodaza}')
                 bot.send_message(message.chat.id, f'Продажа {evropokupka}')
             if message.text == 'Рубль':
                 bot.send_message(message.chat.id, f'Покупка {ruprodaza}')
                 bot.send_message(message.chat.id, f'Продажа {rupokupka}')


############################################################################################################################## Погода

             elif message.text == 'Погода в Ольшанах':

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Погода на завтра!')
                item2 = types.KeyboardButton('ДОМОЙ')

                bot.send_message(message.chat.id, f'Температура в Ольшанах   {data} {mes}!')
                bot.send_message(message.chat.id, f'минимальная температура {tmin}')
                bot.send_message(message.chat.id, f'максимальная температура {tmax}')
                bot.send_message(message.chat.id, f"Температура ночью {night_t}")
                bot.send_message(message.chat.id, str(infa) )

                markup.add(item1, item2)
                bot.send_message(message.chat.id, 'Сделайте выбор!', reply_markup=markup)


             elif  message.text == 'Погода на завтра!':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Погода на завтра!')
                item2 = types.KeyboardButton('ДОМОЙ')

                bot.send_message(message.chat.id, f'Температура в Ольшанах  {data_next}  {mes_next}!')
                bot.send_message(message.chat.id, f'минимальная температура {tmin_next}')
                bot.send_message(message.chat.id, f'максимальная температура {tmax_next}')

                markup.add(item1, item2)
                bot.send_message(message.chat.id, 'Сделайте выбор!', reply_markup=markup)

################################################################################################################################## Кондей
             elif message.text == 'Нормы заправок автокондиционера!':
                     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                     item1 = types.KeyboardButton('Acura')
                     item2 = types.KeyboardButton('Alfa Romeo')
                     item3 = types.KeyboardButton('Audi')
                     item4 = types.KeyboardButton('Bmw')
                     item5 = types.KeyboardButton('Citroen')
                     item6 = types.KeyboardButton('Ford')
                     item7 = types.KeyboardButton('Honda')
                     item8 = types.KeyboardButton('Mercedes')
                     item9 = types.KeyboardButton('Opel')
                     item10 = types.KeyboardButton('Peugeot')
                     item11 = types.KeyboardButton('Toyota')
                     item12 = types.KeyboardButton('Wolkswagen')
                     item13 = types.KeyboardButton('Aston Martin')
                     item14 = types.KeyboardButton('Cadillac')
                     item15 = types.KeyboardButton('Chevrolet')
                     item16 = types.KeyboardButton('Wolkswagen')
                     item17 = types.KeyboardButton('Chrysler(jeep)')
                     item18 = types.KeyboardButton('Dacia')
                     item19 = types.KeyboardButton('Daewoo')
                     item20 = types.KeyboardButton('Dodge')
                     item21 = types.KeyboardButton('Fiat')
                     item22 = types.KeyboardButton('Geely')
                     item23 = types.KeyboardButton('Hyundai')
                     item24 = types.KeyboardButton('Kia')
                     item25 = types.KeyboardButton('Land Rover')
                     item26 = types.KeyboardButton('Lexus')
                     item27 = types.KeyboardButton('Mazda')
                     item28 = types.KeyboardButton('Mitsubishi')
                     item29 = types.KeyboardButton('Nissan')
                     item30 = types.KeyboardButton('Renault')
                     item31 = types.KeyboardButton('Seat')
                     item32 = types.KeyboardButton('Subaru')
                     item33 = types.KeyboardButton('Volvo')

                     item40 = types.KeyboardButton('Грузовые автомобили')
                     item41 = types.KeyboardButton('ДОМОЙ')

                     markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10,
                                item11, item12, item13, item14, item15, item16, item17, item18, item19,
                                item20, item21, item22, item23, item24, item25, item26, item27, item28,
                                item29, item30, item31, item32, item33, item40, item41)
                     bot.send_message(message.chat.id, 'Выберите марку автомобиля!', reply_markup=markup)
###############################################################################################################################  Кондей грузовики!
             elif message.text == 'Грузовые автомобили':
                     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

                     item1 = types.KeyboardButton('DAF')
                     item2 = types.KeyboardButton('Iveco')
                     item3 = types.KeyboardButton('MAN')
                     item4 = types.KeyboardButton('Mercedes-Benz cargo')
                     item5 = types.KeyboardButton('Renault V.I.')
                     item6 = types.KeyboardButton('Scania cargo')
                     item7 = types.KeyboardButton('Volvo cargo')

                     item8 = types.KeyboardButton('Нормы заправок автокондиционера!')
                     item9 = types.KeyboardButton('ДОМОЙ')
                     markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
                     bot.send_message(message.chat.id, 'Выберите марку автомобиля!', reply_markup=markup)

#####################################################################################################################################   ACURA
             elif message.text == 'Acura':
                     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                     item1 = types.KeyboardButton('ILX')
                     item2 = types.KeyboardButton('MDX')
                     item3 = types.KeyboardButton('RSX')
                     item6 = types.KeyboardButton('ДОМОЙ')
                     markup.add(item1, item2, item3, item6)
                     bot.send_message(message.chat.id, 'Выберите модэль автомобиля!', reply_markup=markup)
##################################################################################################################################### ILX
             elif message.text == 'ILX':
                     bot.send_message(message.chat.id, text='2012-2014 >> 400-450')
                     bot.send_message(message.chat.id, text='2014-2022 >> 400-450')
##################################################################################################################################### MDX
             elif message.text == 'MDX':
                     bot.send_message(message.chat.id, text='2001-2006 >> 700-750')
                     bot.send_message(message.chat.id, text='2006-2013 >> 600-650')
###################################################################################################################################### RSX
             elif message.text == 'RSX':
                     bot.send_message(message.chat.id, text='2001-2007 >> 500-550')
             elif message.text == 'Alfa Romeo':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=61')
             elif message.text == 'Aston Martin':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=60')
             elif message.text == 'Cadillac':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=57')
             elif message.text == 'Chevrolet':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=56')
             elif message.text == 'Citroen':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=54')
             elif message.text == 'Chrysler(jeep)':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=55')
             elif message.text == 'Dacia':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=53')
             elif message.text == 'Daewoo':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=52')
             elif message.text == 'Dodge':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=50')
             elif message.text == 'Fiat':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=49')
             elif message.text == 'Geely':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=47')
             elif message.text == 'Hyundai':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=43')
             elif message.text == 'Kia':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=39')
             elif message.text == 'Land Rover':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=37')
             elif message.text == 'Lexus':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=35')
             elif message.text == 'Mazda':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=33')
             elif message.text == 'Mitsubishi':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=31')
             elif message.text == 'Nissan':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=30')
             elif message.text == 'Renault':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=25')
             elif message.text == 'Seat':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=22')
             elif message.text == 'Skoda':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=21')
             elif message.text == 'Subaru':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=18')
             elif message.text == 'Volvo':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=12')
             elif message.text == 'Audi':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=59')
             elif message.text == 'Bmw':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=58')
             elif message.text == 'Ford':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=48')
             elif message.text == 'Honda':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=45')
             elif message.text == 'Mercedes':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=32')
             elif message.text == 'Opel':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=29')
             elif message.text == 'Peugeot':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=28')
             elif message.text == 'Toyota':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=14')
             elif message.text == 'Wolkswagen':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=13')

             elif message.text == 'DAF':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=10')
             elif message.text == 'Iveco':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=8')
             elif message.text == 'MAN':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=7')
             elif message.text == 'Mercedes-Benz cargo':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=6')
             elif message.text == 'Renault V.I.':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=3')
             elif message.text == 'Scania cargo':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=2')
             elif message.text == 'Volvo cargo':
                     bot.send_message(message.chat.id, text='https://www.avtokondicioner.kiev.ua/auto/index.php?page=post&id=0')






#########################################################################################################################################   Помощь!
             elif message.text == 'Помощь':
                     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                     item1 = types.KeyboardButton('ДОМОЙ')


                     markup.add(item1)

                     bot.send_message(message.chat.id, 'Информация!', reply_markup=markup)
                     bot.send_message(message.chat.id,
                                      text='Бот предоставит информацию!'+'\n'+ 'Нормы заправки автокондиционера!'+'\n'+
                                           'Курс валюты Беларусбанка!'+'\n'+
                                           'Погода в аг Ольшаны!')


###########################################################################################################################################   Домой!

             elif message.text == 'ДОМОЙ':
                     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                     item1 = types.KeyboardButton('Помощь')
                     item2 = types.KeyboardButton('Нормы заправок автокондиционера!')
                     item3 = types.KeyboardButton('Курс валюты')
                     item4 = types.KeyboardButton('Погода в Ольшанах')
                     markup.add(item1, item2, item3, item4)
                     bot.send_message(message.chat.id, 'Выберите меню!', reply_markup=markup)




bot.polling(none_stop=True)
