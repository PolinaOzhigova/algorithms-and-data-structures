CC = mingw32-g++
CFLAGS = -std=c++11 -Wall -pedantic

ifeq ($(OS), Windows_NT)
	RM = del
	TARGET1 = main1.exe
	TARGET2 = main2.exe
else
	RM = rm
	TARGET1 = main1
	TARGET2= main2
endif



all:
	$(CC) $(CFLAGS) -o $(TARGET1) main1.cpp
	$(CC) $(CFLAGS) -o $(TARGET2) main2.cpp

run: all
	$(TARGET1) | $(TARGET2)

clean:
	$(RM) $(TARGET1)
	$(RM) $(TARGET2)