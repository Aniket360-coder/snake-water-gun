def start():
    import time
    import os
    import random

    def clear():
        os.system("cls")

    os.system("title Snake Water Gun game")

    clear()
    print()
    print('Welcome to Snake Water Gun'.center(100))



    num_of_rounds = 0
    print()
    num_of_rounds_input = input('Enter Number of Rounds: ')
    if num_of_rounds_input=="0":
        print("program ends because of 0 rounds")
        quit()

    try:
        num_of_rounds = int(num_of_rounds_input)
    except Exception as e:
        print("Error: " + str(e))
        quit()


    print(f"Total Rounds: {num_of_rounds}")
    print()
    print("1. 1st player VS 2nd Player\n2. Human VS Computer")
    game_mode = input(
        "Type the serial number of the game mode above which you want to select: ")
    if game_mode == "1" or game_mode.lower() == "1. 1st player VS 2nd Player".lower() or game_mode.lower() == "first mode".lower():
        def mode1():
            def clear():
                os.system("cls")
            print()
            print("Mode - 1. 1st player VS 2nd Player , Selected")
            # mode 1
            first_player_name = input("Enter name of first player: ")
            print()
            second_player_name = input("Enter name of second player: ")
            print()
            print("Game starts in 3 seconds")
            time.sleep(3)
            clear()
            
        
            
            print()
            round_list = [num for num in range(1,num_of_rounds+1)]
            first_player_round_won = 0
            second_player_round_won = 0
            wording = ['s','w','g']
            for round in round_list:
                print()
                print(f"| Round {round} |".center(100))
                print()
                # start round
                first_choice = input(f"Enter your choice {first_player_name}\n's' for snake\n'w' for water\n'g' for gun\nEnter: ").lower()
                
                clear()
                print()
                print(f"| Round {round} |".center(100))
                print()
                second_choice = input(f"Enter your choice {second_player_name}\n's' for snake\n'w' for water\n'g' for gun\nEnter: ").lower()
                
                if first_choice=="s" and (second_choice=="w"):
                    print()
                    print("Snake drank water and snake wins")
                    
                    print(f"{first_player_name} wins.")
                    first_player_round_won+=1
                    
                if second_choice=="s" and (first_choice=="w"):
                    print()
                    print("Snake drank water and snake wins")
                    
                    print(f"{second_player_name} wins.")
                    second_player_round_won+=1
            
                if first_choice=="w" and (second_choice=="g"):
                    print()
                    print("Gun drowned in water and Water wins")
                    
                    print(f"{first_player_name} wins.")
                    first_player_round_won+=1
                    
                if second_choice=="w" and (first_choice=="g"):
                    print()
                    print("Gun drowned in water and Water wins")
                    
                    print(f"{second_player_name} wins.")
                    second_player_round_won+=1
                    

                if first_choice=="g" and (second_choice=="s"):
                    print()
                    print("Gun killed snake and gun wins")
                    
                    print(f"{first_player_name} wins.")
                    first_player_round_won+=1
                    
                if second_choice=="g" and (first_choice=="s"):
                    print()
                    print("Gun killed snake and gun wins")
                    
                    print(f"{second_player_name} wins.")
                    second_player_round_won+=1
                if first_choice==second_choice:
                    e = ""
                    if first_choice=="s":
                        e="snake"
                    if first_choice=="w":
                        e="water"
                    if first_choice=="g":
                        e="gun"
                    print(f"Error: two players cannot take {e}")
                time.sleep(6)
                clear()
                if round==num_of_rounds:
                    clear()
                    if first_player_round_won>second_player_round_won:
                        print(f"{first_player_name} wins the game!")
                    elif first_player_round_won<second_player_round_won:
                        print(f"{second_player_name} wins the game!")
                    elif first_player_round_won==second_player_round_won:
                        print("It's a tie!")
        mode1()
                
            


    elif game_mode == "2" or game_mode.lower() == "2. Human VS Computer".lower() or game_mode.lower() == "second mode".lower():
        print()
        print("Mode - 2. Human VS Computer , Selected")
        # mode 1
        print()
        first_player_name = input("Enter human's name: ")
        print()
        second_player_name = "computer"
        print('Game starts in 3 seconds')
        time.sleep(3)
        clear()
        # start human vs computer

        print()
        round_list = [num for num in range(1,num_of_rounds+1)]
        first_player_round_won = 0
        second_player_round_won = 0
        wording = ['s','w','g']
        for round in round_list:
            print()
            print(f"| Round {round} |".center(100))
            print()
            # start round
            first_choice = input(f"Enter your choice {first_player_name}\n's' for snake\n'w' for water\n'g' for gun\nEnter: ").lower()
            lst = ["s", "w", "g"]
            second_choice = random.choice(lst)
            if second_choice==first_choice:
                while True:
                    second_choice = random.choice(lst)
                    if second_choice==first_choice:
                        continue
                    else:
                        break
            
            print()
            
            
            print(f"Computer chose {second_choice}")
            
            if first_choice=="s" and (second_choice=="w"):
                print()
                print("Snake drank water and snake wins")
                
                print(f"{first_player_name} wins.")
                first_player_round_won+=1
                
            if second_choice=="s" and (first_choice=="w"):
                print()
                print("Snake drank water and snake wins")
                
                print(f"{second_player_name} wins.")
                second_player_round_won+=1
           
            if first_choice=="w" and (second_choice=="g"):
                print()
                print("Gun drowned in water and Water wins")
                
                print(f"{first_player_name} wins.")
                first_player_round_won+=1
                
            if second_choice=="w" and (first_choice=="g"):
                print()
                print("Gun drowned in water and Water wins")
                
                print(f"{second_player_name} wins.")
                second_player_round_won+=1
                

            if first_choice=="g" and (second_choice=="s"):
                print()
                print("Gun killed snake and gun wins")
                
                print(f"{first_player_name} wins.")
                first_player_round_won+=1
                
            if second_choice=="g" and (first_choice=="s"):
                print()
                print("Gun killed snake and gun wins")
                
                print(f"{second_player_name} wins.")
                second_player_round_won+=1
            if first_choice==second_choice:
                e = ""
                if first_choice=="s":
                    e="snake"
                if first_choice=="w":
                    e="water"
                if first_choice=="g":
                    e="gun"
                print(f"Error: two players cannot take {e}")
            time.sleep(6)
            clear()
            if round==num_of_rounds:
                clear()
                if first_player_round_won>second_player_round_won:
                    print(f"{first_player_name} wins the game!")
                elif first_player_round_won<second_player_round_won:
                    print(f"{second_player_name} wins the game!")
                elif first_player_round_won==second_player_round_won:
                    print("It's a tie!")
                print()
                restart = input("Play again? type 'y' for yes, type 'q' to quit: ")
                if restart=="y":
                    start()
                if restart=="q":
                    quit()
                else:
                    print("Wrong input")

    else:
        print("Wrong input")

    """
    Rules :-
    snake vs water - Snake drinks water and snake wins
    water vs gun - Gun will drown in water and Water wins
    gun vs snake - Gun kill snake and gun wins
    """
    
start()
