# -*- coding: utf-8 -*-
print("hello world") #Good luck for today's learning!

# #函数 位置实参
# def make_shirt(size,color,words_on_it):
#     print('This shirt is size '+size+". It's "+color+". "+ "It says "+words_on_it+".")
# make_shirt('S','red',"I love python")

# #关键词实参
# def make_shirt(size,color):
#     print('This shirt is size '+size+". It's "+color+".")
# make_shirt(color = 'red',size = 'S',words_on_it)

#多次调用函数
def diy_shirt(size,color,words_on_it):
    print('hello, I wear size '+size+"."+'\nMy favorite color is '+color+". "+ '\nPlease add '+words_on_it+" on it.")
diy_shirt('S','red','I love python')
diy_shirt('M','green','I love you')
diy_shirt('L','white','My eyes are on you')

def capital_country(capital,country):
    print(capital+ ' is the capital of '+country+"." )
capital_country('Beijing','China')
capital_country('Washington','US')





