#include "Game.h"

Game::Game(){
	for(int i=0; i<3; ++i){
		std::vector<int> temp;
		for(int j=0; j<3; ++j){
			temp.push_back(0);
		}
		this->board.push_back(temp);
	}

	this->spotsLeft = 9;
}

Game::~Game(){

}

// -1 for human player, 1 for computer player
// some logic wrong here
std::pair<char, std::string> Game::findMoves(char player){
	char winnerFound = checkWin();
	if(!this->spotsLeft){
		return std::make_pair(winnerFound, "");
	}else{
		//if someone has won, return the winner
		if(winnerFound){
			return std::make_pair(winnerFound, "");
		}
	}

	std::vector<std::pair<char,std::string> > possibleMoves;

	for(uint i=0; i<board.size(); ++i){
		for(uint j=0; j<board[0].size(); ++j){
			bool validMove = setMove(i, j, player, false);
			if(validMove){
				std::pair<char,std::string> nextMove = findMoves(-1*player);
				int number = 3*i + j + 1;
				char otherTemp = number + '0';
				nextMove.second = otherTemp + nextMove.second;
				possibleMoves.push_back(nextMove);
				undoMove(i, j, player, false);
			}
		}
	}

/*	if(player == 1)	std::sort(possibleMoves.begin(), possibleMoves.end());
	else std::sort(possibleMoves.end(), possibleMoves.begin());*/

	for(uint i=0; i<possibleMoves.size(); ++i){
		if(possibleMoves[i].first == player){
			return possibleMoves[i];
		}
	}

	for(uint i=0; i<possibleMoves.size(); ++i){
		if(possibleMoves[i].first == 0){
			return possibleMoves[i];
		}
	}

	return possibleMoves[possibleMoves.size() -1];
}

void Game::undoMove(uint i, uint j, char player, bool human){
	this->board[i][j] = 0;
	++this->spotsLeft;
}

int Game::play(char response){
	int intResponse = (int)response;
	if(intResponse){
		playTwoHumans();
	}else{
		playAgainstComputer();
	}

	return 0;
}

//returns 1 for computer first, -1 for player first
char Game::chooseFirstMover(bool human){
	if(human){
		std::cout << "Who should go first?" << std::endl;
		std::cout << "Input O or X" << std::endl;
	}else{
		std::cout << "Should the computer or human go first?" << std::endl;
		std::cout << "Input O for computer and X for human" << std::endl;
	}	

	std::string responseStr = "";
	char response = 0;

	while(response == 0){
		getline(std::cin, responseStr);
		response = responseStr[0];

		if(response == 'X' || response == 'x'){
			std::cout << "The player will go first" << std::endl;
			return -1;
		}else if(response == 'O' || response == 'o'){
			std::cout << "The computer will go first" << std::endl;
			return 1;
		}
		std::cout << "Please pick a valid option" << std::endl;
		if(human) std::cout << "Input O for computer and X for human " << std::endl;
		else std::cout << "Input O or X" << std::endl;
		std::cout << "Input O or X" << std::endl;
		getline(std::cin, responseStr);
		if(response == 2) return 0;
	}

	return 0;
}

void Game::playTwoHumans(){
	std::cout << "here";
	char player = chooseFirstMover(true);
	if(!player) return;
	startHumanGame(player);
}

void Game::startHumanGame(int response){
	char checkWin = 0;
	char alternate = 1;

	while(!checkWin && this->spotsLeft > 0){
		checkWin = humanTurn(alternate*response);
		alternate *= -1;
	}

	printBoard();
	char player = ' ';

	if(checkWin == 0) player = 0;
	else if(checkWin == -1) player = 'O';
	else player = 'X';

	endMessage(player);
}

char Game::humanTurn(char player){
	printBoard();
	std::cout << "Which space do you want to take?" << std::endl;

	int row = -1;
	int column = -1;
	std::string input;
	bool validMove = 0;

	while(!validMove){
		std::getline(std::cin, input);
		std::cout << input << std::endl;

		for(uint i=0; i<input.size(); ++i){
			if(row == -1 && input[i] >= '0' && input[i] <= '9'){
				row = input[i] - '0';
			}
			else if(column == -1 && input[i] >= '0' && input[i] <= '9'){
				column = input[i] - '0';
			}
			if(row != -1 && column != -1) break;
		}

		validMove = setMove(row, column, player, true);
		row = -1;
		column = -1;
	}

	return checkWin();
}

bool Game::setMove(uint row, uint column, char player, bool human){
/*	std::cout << "row: " << row << std::endl;
	std::cout << "column: " << column << std::endl;*/
	if(row >= board.size() || row < 0 || column >= board.size() || column < 0){
		if(human) std::cout << "Please input a valid move" << std::endl;
		return false;
	}
	if(this->board[row][column] != 0){
		if(human) std::cout << "Please input a valid move" << std::endl;
		return false;
	}

	this->board[row][column] = player;
	--this->spotsLeft;
	return true;
}

char Game::checkWin(){
	for(uint i=0; i<this->board.size(); ++i){
		int rowSum = 0;
		int columnSum = 0;
		for(uint j=0; j<this->board.size(); ++j){
			rowSum += this->board[i][j];
			columnSum += this->board[j][i];
		}

		if(rowSum == 3 || columnSum == 3) return 1;
		else if(rowSum == -3 || columnSum == -3) return -1;
	}

	int leftDiag = 0;
	int rightDiag = 0;
	for(uint i=0; i<this->board.size(); ++i){
		leftDiag += this->board[i][i];
		rightDiag += this->board[i][this->board.size()-1-i];
	}

	if(leftDiag == 3 || rightDiag == 3) return 1;
	else if(leftDiag == -3 || rightDiag == -3) return -1;

	return 0;
}

void Game::playAgainstComputer(){
	char player = chooseFirstMover(false);

	if(!player) return;

	startComputerGame(player);
}

void Game::startComputerGame(int response){
	std::cout << "response in computerGame: " << (int)response << std::endl;
	char checkWin = 0;
	char alternate = 1;
	bool humanNow = false;

	char player = response;
	if(player == -1) humanNow = true;

	while(!checkWin && this->spotsLeft > 0){
		if(humanNow) checkWin = humanTurn(alternate*response);
		else checkWin = computerTurn(alternate*response);
		alternate *= -1;
		humanNow = !humanNow;
	}

	if(checkWin == 0) player = 0;
	else if(checkWin == -1) player = 'O';
	else player = 'X';

	endMessage(player);
}

char Game::computerTurn(char player){
	printBoard();
	int row = -1;
	int column = -1;

	std::pair<char, std::string> nextMoves = findMoves(player);
	char nextMove = nextMoves.second[0] - '0';

	row = (nextMove-1)/3;
	column = (nextMove-1)%3;

	setMove(row, column, player, true);
	return checkWin();
}

void Game::printBoard(){
	//std::cout << " ";
	for(uint i=0; i<board.size(); ++i){
		std::cout << " _____ ";
	}
	//std::cout << "_ " << std::endl;
	std::cout << std::endl;
	for(uint i=0; i<board.size(); ++i){
		for(uint j=0; j<board.size(); ++j){
			char output = ' ';
			if(board[i][j] == -1) output = 'O';
			else if(board[i][j] == 1) output = 'X';
			std::cout << "|  " << output << "  |";
		}
		std::cout << std::endl;
		for(uint j=0; j<board.size(); ++j){
			std::cout << "|__" << "_" << "__|";
		}
		std::cout << std::endl;
	}

	std::cout << std::endl << std::endl;
}

void Game::endMessage(char winner){
	printBoard();
	if(winner == 0){
		std::cout << "The game ends in a tie" << std::endl;
	}else{
		std::cout << "Congratulations player " << winner << "!  You've won!" << std::endl;
	}
}