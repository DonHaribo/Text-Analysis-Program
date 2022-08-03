"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jonatan Kahle
email: jonatankahle@gmail.com
discord: Jonatan Kahle#8562
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
#user input
username = input('input username: ')
password = input('input password: ')
#registered users
user_info = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}
#check if input is in registered users
separation = 25*'-'
if username in user_info.keys() and password in user_info.values():
    print(separation)
    print(f'Welcome to the app, {username} ')
    print('We have 3 texts to be analyzed.')
    print(separation)
else:
    print(f'username: {username}')
    print(f'password: {password}')
    print('unregistered user, terminating the program..')
    exit()
#user chooses text
user_choice = input('Enter a number btw. 1 and 3 to select: ')
print(separation)
if  user_choice in '1' or '2' or '3':
    pass
else:
    print(f'{user_choice} is not a valid option, terminating..')
    exit()

user_text = TEXTS[int(user_choice) -1]
#Counting words in text

len_user_text = len(user_text.split())
print(f'There are {len_user_text} words in the selected text.')

# Splitting the text into individual words
text_list = tuple(user_text.split(' '))

#Counting words with Capital letter

capital_words = []
for word in text_list:
    if word.istitle():
        capital_words.append(1)
print('There are ' + str(sum(capital_words)) + ' capital words.')

#Counting upper case words
upper_words = []
for word in text_list:
    if word.isupper():
        upper_words.append(1)
print('There are ' + str(sum(upper_words)) + ' uppercase words.')

#Counting lower case words
lower_words = []
for word in text_list:
    if word.islower():
        lower_words.append(1)
print('There are ' + str(sum(lower_words)) + ' lowercase words.')

#Counting number of number
numbers = []
for word in text_list:
    if word.isnumeric():
         numbers.append(int(word))
print('There are ' + str(len(numbers)) + ' numbers.')
print('The sum of all numbers in the text is equal to ' + str(sum(numbers)) + '.')


#graph of the lenghts of individual words in text
print(separation)
print('LEN|  OCCURENCES  |NR.')
print(separation)
x = 0
for word in text_list:
    word_lenght = len(word)
    x += 1
    print(f'{x}| ' + (word_lenght) * '*' + '  ' + str(word_lenght))