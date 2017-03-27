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
adjective = ['Hairy', 'Stupid', 'Blonde', 'Smelly', 'Loose', 'Putrid', 'Disgusting', 'Violent', 'Bloody', 'Carribbean',
'Lazy', 'Slow', 'Hot', 'Slimy', 'Old', 'Moist', 'Shiny', 'Frothy', 'Holy', 'Yellow', 'Rancid', 'Spoiled', 'Weird', 'Cheesy',
'Funky', 'Bad', 'Wet', 'Crappy', 'Mad', 'Septic', 'Dusty', 'Dirty']
noun = ['Gravy', 'Navel', 'Dog', 'Cat', 'Hag', 'Poop', 'Discharge', 'Gunk', 'Rust', 'Cheese', 'Scum', 'Rat', 'Johnson',
'Sewage', 'Sea Water', 'Dust', 'Toenail', 'Fungus', 'Paint', 'Santorum', 'Imitation Crab', 'Callus', 'Wart', 'Plague',
'Headcheese', 'Pus', 'Rubbing Alcohol', 'Glue', 'Galbladder', 'Nipple', 'Battery Acid', 'Chicken']
name = {
    
}
def ask():
    choices = {
        
    }
    for x in questions:
        print(questions[x])
        choices[x] = input("y/n? ")
        while (choices[x] != 'y') and (choices[x] != 'n'):
            choices[x] = input("type only y or n. I ask again: {} ".format(questions[x]))
    print(choices)
    make_drink(choices)
            
def make_drink(choices):
    drink = ()
    for x in choices:
        if choices[x] == 'y':
            drink = drink + (random.choice(ingredients[x]),)
    print(drink)
    name_drink(drink)
    
def name_drink(drink):
    namequeue = random.choice(adjective) + " " + random.choice(noun)
    if drink in name:
        print(name[drink])
    else:
        while namequeue in name.items():
            namequeue = random.choice(adjective) + " " + random.choice(noun)
        name[drink] = namequeue
        print(name[drink])

if __name__ == '__main__':
    ask()
    another = input("Would you like another drink? y/n ")
    while (another != 'y') and (another != 'n'):
        another = input('Type only y or n. Another drink? ')
    while another == 'y':
        ask()
        another = input("Would you like another drink? y/n ")