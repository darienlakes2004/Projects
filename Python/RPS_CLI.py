from random import randint as ran

#Clears the terminal
print("\033[H\033[J", end="")

#Inits variables
player_score = 0
comp_score = 0
options = ["1","2","3"]


while True:
	#Clears variables that will be altered later
	player_choice = 0
	comp_choice = 0
	
	#Promt with options
	print("Rock Paper Scissors?")
	print("[1] Rock")
	print("[2] Paper")
	print("[3] Scissors")
	
	#While loop that ensures the user responds with a valid option
	while (player_choice not in options): 
		print("Please type a number 1, 2, or 3")
		player_choice = input()

	#Gets a random choice as the computers play
	comp_choice = str(ran(1,3))
	
	# 60 lines of code that evaluates if the player gets a point, if the computer gets a point, or if it's a tie
	if player_choice == options[0]:
		print("OH WOW. YOU CHOSE ROCK")
		if comp_choice == options[0]:
			print("They chose rock. Tie")
		if comp_choice == options[1]:
			print("They chose paper. Comp wins")
			comp_score = comp_score + 1
		if comp_choice == options[2]:
			print("They chose scissors. You win")
			player_score = player_score + 1	
	if player_choice == options[1]:
		print("OH WOW. YOU CHOSE PAPER")
		if comp_choice == options[0]:
			print("They chose rock. You win")
			player_score = player_score + 1
		if comp_choice == options[1]:
			print("They chose paper. Tie")
		if comp_choice == options[2]:
			print("They chose scissors. Comp win")
			comp_score = comp_score + 1
		
	if player_choice == options[2]:
		print("OH WOW. YOU CHOSE SCISSORS")
		if comp_choice == options[0]:
			print("They chose rock. Comp Wins")
			comp_score = comp_score + 1
		if comp_choice == options[1]:
			print("They chose paper. You win")
			player_score = player_score + 1
		if comp_choice == options[2]:
			print("They chose scissors. Tie")
			
	#Displays score and promts whether or not to play again
	print("Score ",player_score,"| ",comp_score)
	print("Play again?","\n","[1] Yeah","\n","[2] No")
	if input() == options[0]:
		player_choice = 0
		print("\033[H\033[J", end="")
		continue
	else:
		print("\033[H\033[J", end="")
		break 
