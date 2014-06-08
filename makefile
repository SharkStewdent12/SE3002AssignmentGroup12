SRC_DIR = src
CC = python -c "import py_compile; py_compile.compile(
_CC =)"

main: src/main.py src/dbFunctions.py dbFunctions
	$(CC) 'src/$@.py','$@.pyc' $(_CC)
	
dbFunctions: src/dbFunctions.py
	$(CC) 'src/$@.py','$@.pyc' $(_CC)

testProgram: src/testProgram.py src/dbFunctions.py
	$(CC) 'src/$@.py','$@.pyc' $(_CC)

