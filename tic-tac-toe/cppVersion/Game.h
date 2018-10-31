#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

class Game {
	public:
		Game();
		~Game();
		int play(char response);
	private:
		std::vector<std::vector<int> > board;
		unsigned char spotsLeft;
		void playTwoHumans();
		void playAgainstComputer();
		void printBoard();
		void startHumanGame(int response);
		char humanTurn(char player);
		char checkWin();
		void endMessage(char winner);
		bool setMove(uint row, uint column, char player, bool human);
		std::pair<char, std::string> findMoves(char player);
		void undoMove(uint i, uint j, char player, bool human);
		char chooseFirstMover(bool human);
		void startComputerGame(int player);
		char computerTurn(char player);
};