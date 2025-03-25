import random
#python journal project simple python program
#Consuelo Maldonado


# List of possible responses from the Magic 8 Ball

responses = [
    "Yes", 
    "No", 
    "Maybe", 
    "haha you wish", 
    "Definitely", 
    "Dont hold your breath"
]

def magic_8_ball():
    print("Welcome to the Magic 8 Ball! I will predict your future!") #Welcome prompt
    question = input("Ask the Magic 8 Ball a question if you dare: ")  # Ask the user for a question
    
    # Randomly choose a response
    answer = random.choice(responses)
    
    print(f"The Magic 8 Ball says: {answer}") #printed with every answer
    
    # Ask if the user wants to ask another question
    play_again = input("Do you dare to ask another question? (yes/no): ").lower()
    
    if play_again == 'yes': #if yes
        magic_8_ball()  # Call the function again to ask another question
    else:
        print("Thank you for playing! Goodluck") #if no End the game

# Run the Magic 8 Ball function
magic_8_ball()