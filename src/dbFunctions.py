from peewee import *

db = SqliteDatabase('people.db')

outputFile = open('lab3Output.txt','w')

class Person(Model):
	name = CharField()
	stuNum = IntegerField()
	
	class Meta:
		database = db

def initialiseDatabase():
	if Person.table_exists():
		Person.drop_table()
	Person.create_table()
	
def readToDB(textfileName):
	inputFile = open(textfileName,'r')
	for record in inputFile:
		line =  record.split(',')
		recNum = int( line[0].strip() )
		recName = line[1].strip()
		Person.create( name = recName, stuNum = recNum)

def getPeopleFromDB():
	persons = []
	for person in Person.select():
		persons.append(person)
	return persons
	
def sortPeople(persons, order):
	persons = sorted(persons, key=lambda person:person.stuNum, reverse = order)
	return persons
	
def writePeopleToText(persons,textfileName):
	outputFile = open(textfileName,'w')
	for person in persons:
		outputFile.write( str(person.stuNum) + ', ' + person.name + '\n')
	outputFile.close()

def printSampleFromDB():
	print "Sample from Database:"
	persons = getPeopleFromDB()
	for i in (range(0,15) + range(len(persons)-15,len(persons))):
		print persons[i].stuNum, persons[i].name

def printSampleFromText(textfileName):
	print "Sample from",textfileName
	inputFile = open(textfileName,'r')
	persons = []
	for record in inputFile:
		line =  record.split(',')
		recNum = int( line[0].strip() )
		recName = line[1].strip()
		persons.append(Person( name = recName, stuNum = recNum))
	for i in (range(0,15) + range(len(persons)-15,len(persons))):
		print persons[i].stuNum, persons[i].name

def getOrderFlag():
	ASC = False
	DESC = True
	print "Select order to sort records 'ASC' or 'DESC'."
	while True:
		lineIn = raw_input()
		if (lineIn.upper() == "ASC"):
			return ASC
		elif (lineIn.upper() == "DESC"):
			return DESC
		else:
			print "you must input 'ASC' or 'DESC'"
	
