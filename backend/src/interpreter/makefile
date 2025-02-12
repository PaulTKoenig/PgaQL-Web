# Compiler and flags
CC=gcc
CFLAGS=-I.

# Source files and target executable
SRC=main.c lexer.c parser.c interpreter.c
TARGET=main

# Default target: compile the executable
all: $(TARGET)

# Compile the executable
$(TARGET): $(SRC)
	$(CC) -o $(TARGET) $(SRC) $(CFLAGS)

# Clean target to remove any generated files
clean:
	rm -f 