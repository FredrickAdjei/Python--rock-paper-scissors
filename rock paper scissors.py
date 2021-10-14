import random
userwins = 0
computerwins = 0
draws = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock paper scissors or Q to quit-  ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    
    # 0-rock 1- paper 2- scissors
    random_number = random.randint(0, 2)
    
    pcpick = options[random_number]
    print("Computer picked", pcpick + '.')

    if user_input == 'rock' and pcpick == 'scissors':
        print("you won!")
        userwins += 1
    elif user_input == 'paper' and pcpick == 'rock':
        print("you won!")
        userwins += 1

    elif user_input == 'scissors' and pcpick == 'paper':
        print("you won!")
        userwins += 1

    elif user_input ==  pcpick :
        print("you draw!")
        draws += 1

    else:
        print("you lost")
        computerwins += 1
        


print("you won", userwins, "times")   
print("the computer won", computerwins, "times") 
print("you guys drew", draws, "times") 
print("Goodbye!")
