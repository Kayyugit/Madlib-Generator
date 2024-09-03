import json
import random

print("=============================")
print("Welcome to Madlib Generator.")
print("=============================")
print("Instructions: Fill in the appropriate fields with words that meet the specified criteria.\nNot sure what words to enter? No problem!\nYou can choose to view sample words.")

def load_stories(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data['stories']

def show_tip():
    print(".................................................................")
    print("Here are some sample words: ")
    tips = [
    "Nouns: Apple, Car, Dog, House, River, Tree, Elephant, Computer, Mountain, Book",
    "Adjectives: Happy, Bright, Mysterious, Tiny, Energetic, Ancient, Delicious, Swift, Colorful, Fierce",
    "Verbs: Jump, Run, Write, Sing, Eat, Dance, Fly, Read, Swim, Laugh",
    "Adverbs: Quickly, Silently, Happily, Carefully, Bravely, Gracefully, Eagerly, Mysteriously, Rapidly, Joyfully"
    ]

    for tip in tips:
        print(tip)
    

def create_madlib():
    while True:
        show_tip_input = input("Would you like to see sample words before we start? (yes/no): ").strip().lower()
        if show_tip_input in ['yes', 'no']:
            break
        print("Please enter 'yes' or 'no'.")

    if show_tip_input == 'yes':
        show_tip()

    stories = load_stories('stories.json')
    story_template = random.choice(stories)['template']

    print(".................................................................")
    adjective1 = input("Enter an adjective: ")
    print("................................")
    noun1 = input("Enter a noun: ")
    print("................................")
    verb1 = input("Enter a verb: ")
    print("................................")
    adverb1 = input("Enter an adverb: ")
    print("................................")
    adjective2 = input("Enter another adjective: ")
    print("................................")
    noun2 = input("Enter another noun: ")
    print("................................")
    noun3 = input("Enter one more noun: ")
    print("................................")
    adjective3 = input("Almost there. Enter one last adjective: ")
    print("................................")
    verb2 = input("Last one: Enter one more verb: ")

    madlib = story_template.format(
        adjective1=adjective1,
        noun1=noun1,
        verb1=verb1,
        adverb1=adverb1,
        adjective2=adjective2,
        noun2=noun2,
        noun3=noun3,
        adjective3=adjective3,
        verb2=verb2
    )

    border_width = 60
    print("." * border_width)
    print("Here's your Madlib story:".center(border_width))
    print("." * border_width)
    
    print(madlib)
    print("." * border_width)

def play_madlib_game():
    while True:
        create_madlib()
        
        while True:
            play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
            print("......................................")
            if play_again in ['yes', 'no']:
                break
            print("Please enter 'yes' or 'no'.")
        
        if play_again == 'no':
            print("\nThank you for playing! Goodbye!")
            print("...............................")
            break

play_madlib_game()