CC = mingw32-g++
CFLAGS = -std=c++11 -Wall -pedantic
SOURCE = main1.cpp

ifeq ($(OS), Windows_NT)
	RM = del
	TARGET = main1.exe
else
	RM = rm
	TARGET = main1
endif



all:
	$(CC) $(CFLAGS) -o $(TARGET) $(SOURCE)

run: all
	.\$(TARGET) | py .\main.py

clean:
	$(RM) $(TARGET)