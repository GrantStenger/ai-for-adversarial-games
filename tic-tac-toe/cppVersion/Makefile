CPPFLAGS = g++ -g -Wall -std=c++11 

all: Game main

main: main.cpp Game.o
	$(CPPFLAGS) main.cpp Game.o -o main

Game: Game.cpp Game.h
	$(CPPFLAGS) Game.cpp -c -o Game.o

.PHONY: clean

clean:
	-rm main