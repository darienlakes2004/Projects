#include <stdio.h>
#include <stdlib.h>
#include <time.h>

									     	       //Init variables
int player_score = 0;
int comp_score = 0;
int playing = 1;
int comp_choice = 0;

int main(){
	while (playing == 1){
		int player_choice = 0;
		
		srand(time(NULL)); 						       // Gets the time as a seed
	
		int comp_choice = ((random() % 3)+1); 				       // Uses the seed to get a number 0-5
	
		printf("\e[H\e[2J\e[3J");				               // Clears the console, \e[H Moves the
										       // cursor to the top left. \e[2j
										       // clears the screen and \e[2J resets
	                	          					       // the scroll
	
		printf("Rock Paper Scissors?\n[1] Rock\n[2] Paper\n[3] Scissors\n");   // Presents the player with their 
								       		       // options
	
	
		while(player_choice == 0 || player_choice > 3){			       // Evaluates if the user replied with 
										       // a zero, which happends to be the 
										       // result if you place an ASCII 
										       // character, or a number greater than
										       // those offered
			printf("1, 2, or 3? ");
			scanf("%d", &player_choice); 				       // Gets the players choice
		}

		if (player_choice == 1){					       // 52 lines telling the player their
			printf("You chose rock\n");				       // choice, the computer's choice, and
			if (comp_choice == 1){					       // the result
				printf("Computer chose rock\n");
				printf("Tie! Nothing happens\n");
			}
			if (comp_choice == 2){
				printf("Computer chose paper\n");
				printf("You lose. Computer gets a point\n");
				comp_score++;
			}
			if (comp_choice == 3){
				printf("Computer chose scissors\n");
				printf("Yay! You got a point\n");
				player_score++;
			}
	}
	
		if (player_choice == 2){
			printf("You chose paper\n");
			if (comp_choice == 1){
				printf("Computer chose rock\n");
				printf("Yay! You got a point\n");
				player_score++;
			}
			if (comp_choice == 2){
				printf("Computer chose paper\n");
				printf("Tie! Nothing happens\n");
			}
			if (comp_choice == 3){
				printf("Computer chose scissors\n");
				printf("You lose. Computer gets a point\n");
				comp_score++;
			}
		}
	
		if (player_choice == 3){
			printf("You chose scissors\n");
			if (comp_choice == 1){
				printf("Computer chose rock\n");
				printf("You lose. Computer gets a point\n");
				comp_score++;
			}
			if (comp_choice == 2){
				printf("Computer chose paper\n");
				printf("Yay! You got a point\n");
				player_score++;
			}
			if (comp_choice == 3){
				printf("Computer chose scissors\n");
				printf("Tie! Nothing happens\n");
			}
		}
		
		
		printf("Your score: %d| Computer score: %d\n",player_score,comp_score);// Relays the current scores
		printf("Wanna play again?\n[1] Yes\n[2] No\n");			       // Asks if the player wants to go 
		scanf("%d",&playing);						       // again. If they reply 1, the
										       // loop continues. But if they put any
										       // other response, the loop breaks and
										       // the program terminates
		
	
	}
}

