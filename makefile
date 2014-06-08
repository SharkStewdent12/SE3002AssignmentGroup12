SRC_DIR = src
CC = python -c "import py_compile; py_compile.compile(
_CC =)"

MOD = $(wildcard $(SRC_DIR)/*.py)



$(MOD): $(patsubst %, $(SRC_DIR)/%.py, $@)
	$(CC) '$^','./$@.pyc' $(_CC)

#dbFunctions: $(SRC_DIR)/dbFunctions.py
#	$(CC) '$^','./$@.pyc' $(_CC)
#	
#main: $(SRC_DIR)/main.py $(SRC_DIR)/dbFunctions.py
#	$(CC) '$^','./$@.pyc' $(_CC)
#
#.PHONY: testProgram
#
#testProgram: $(SRC_DIR)/testProgram.py
#	$(CC) $^ $(_CC)
