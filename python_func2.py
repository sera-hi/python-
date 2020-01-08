def show_magicians(names):
    for name in names:
        msg = ('Hello, the great ' + name)
        print(msg)

name_magicians = ['Ada','Alice','Sera']
show_magicians(name_magicians)

# def make_salad(*fruits):
#     for fruit in fruits:
#         print('-' + fruit)

# name1 = input('enter the fruits you want to use')
# make_salad(name1)

def make_salad(*fruits):
    for fruit in fruits:
        print('-' + fruit)

while True:
    f_name = input('Hello, please enter the fruits you want to use for making salad.\nYou could enter q at anytime to finish the choice')
    if f_name == 'q':
        break
    make_salad(f_name)
        
    