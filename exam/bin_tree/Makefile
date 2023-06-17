generate := python generate_tree.py
analyze := python analyze_tree.py

RM = rm
TARGET1 = tree_graph.png
TARGET2 = tree.json
TARGET3 = tree1.txt

ifeq ($(OS), Windows_NT)
	RM = del
endif

generate:
	$(generate)

analyze:
	$(analyze)

all: generate analyze

run: all

clean:
	$(RM) $(TARGET1)
	$(RM) $(TARGET2)
	$(RM) $(TARGET3)