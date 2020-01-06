# -*- coding: utf-8 -*-
print("hello world") #Good luck for today's learning!

# List 修改添加删除
motorcycles = ['bus','car','plane']
motorcycles.insert(1,'train')
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(popped_motorcycles) 
#删除末尾元素并且还能继续使用它，括号里加索引删除任意元素
popped_motorcycles2 = motorcycles.pop(0)
print(popped_motorcycles2)

dinner_names = ['Michael Jordan','Kobe Bryant','Stephen Curry']
print('Hello, '+dinner_names[0]+ ', '+dinner_names[1]+', '+dinner_names[2]+ ', could you have dinner with me?')
#库里有事来不了
print('Oh, '+dinner_names[2]+' could not attend our dinner.')
#换成水花兄弟的另一位汤普森吧
dinner_names[2] = 'Klay Thompson'
print(dinner_names)
print('Hello, '+dinner_names[0]+ ', '+dinner_names[1]+', '+dinner_names[2]+ ', could you have dinner with me?')
#找到个大桌子
print("Hello, I've found a larger table!")
dinner_names.insert(0,'Kawhi Leonard')
dinner_names.insert(2,'Kevin Durant')
dinner_names.append('LeBron James')
print(dinner_names)
print('Hello, '+dinner_names[0]+ ', '+dinner_names[1]+', '+dinner_names[2]+dinner_names[3]+ ', '+dinner_names[4]+ ', '+dinner_names[5]+ ', could you have dinner with me?')
#要减少人数了
print('Ok, I am so sorry that I could only invite two of you.')
dinner_names_delete = dinner_names.pop()
print('Sorry, '+dinner_names_delete+', see you next time!')




