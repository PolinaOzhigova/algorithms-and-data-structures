CC = mingw32-g++
CFLAGS = -std=c++11 -Wall -pedantic

ifeq ($(OS), Windows_NT)
	RM = del
	TARGET = main.exe
else
	RM = rm
	TARGET = main
endif



all:
	$(CC) $(CFLAGS) -o $(TARGET) main.cpp

run: all
	$(TARGET) 

clean:
	$(RM) $(TARGET)