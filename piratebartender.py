import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def ask():
    for x in questions:
        print(questions[x])
        response[x] = input("y/n? ")
        while (response[x] != 'y') and (response[x] != 'n'):
            response[x] = input("type only y or n. I ask again: {} ".format(questions[x]))
    
    print(response)
    
    for x in response:
        if response[x] == 'y':
            print (random.choice(ingredients[x]))
            
response = {
    
}    
if __name__ == '__main__':
    ask()
another = input("Would you like another drink? y/n ")
while (another != 'y') and (another != 'n'):
    another = input('Type only y or n. Another drink? ')
while another == 'y':
    ask()
    another = input("Would you like another drink? y/n ")