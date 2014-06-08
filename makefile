SRC_DIR = src
CC = python -c "import py_compile; py_compile.compile(
_CC =)"

main: src/main.py dbFunctions
	$(CC) 'src/$@.py','$@.pyc' $(_CC)
	
dbFunctions: src/dbFunctions.py
	$(CC) 'src/$@.py','$@.pyc' $(_CC)

testProgram: src/testProgram.py dbFunctions
	$(CC) 'src/$@.py','$@.pyc' $(_CC)

