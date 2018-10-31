#include "Game.h"

int main(int argc, char* argv[]){
	std::cout << "How do you want to play?  Input 0 to play " << std::endl;
	std::cout << "against the computer, and 1 to have two humans play" << std::endl;

	std::string responseStr = "";
	char response = -1;
	getline(std::cin, responseStr);

	response = responseStr[0] - '0';
	std::cout << (int)response << std::endl;

	if(response != 0 && response != 1){
		std::cout << "Please input a valid play option." << std::endl;
		return 1;
	}

	Game* game = new Game();

	return game->play(response);
}