#Written by Khalid Ebrahim, Mark Durrheim and Matthew Unterslak
from peewee import *
import os.path

db = SqliteDatabase('people.db')

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
	if (os.path.exists(textfileName)):
		try:
			inputFile = open(textfileName,'r')
		except:
			print 'Cannot open file',textfileName
	else:
		print 'Cannot find input file "',textfileName,'", please ensure that it is in the directory',os.path.dirname(os.path.realpath(__file__))
		exit(0)
	try:
		for record in inputFile:
			if (record == ""):
				print 'Error in input, blank lines are not allowed'
				exit(0)
			line =  record.split(',')
			recNum = int( line[0].strip() )
			if (len(line[0].strip()) != 6):
				print 'Error in input, incorrect student number format:',record
				exit(0)
			recName = line[1].strip()
			if (recName == ""):
				print 'Error in input, blank student name:',record
				exit(0)
			Person.create( name = recName, stuNum = recNum)
	except:
		print 'Incorrect input format:"',record.strip(),'"from',textfileName
		exit(0)
	inputFile.close()

def getPeopleFromDB():
	try:
		persons = []
		for person in Person.select():
			persons.append(person)
		return persons
	except:
		print 'Cannot read people from the database'
	
def sortPeople(persons, order):
	persons = sorted(persons, key=lambda person:person.stuNum, reverse = order)
	return persons
	
def writePeopleToText(persons,textfileName):
	outputFile = open(textfileName,'w')
	for person in persons:
		outputFile.write( str(person.stuNum) + ', ' + person.name + '\n')
	outputFile.close()

def printSampleFromDB():
	persons = getPeopleFromDB()
	print "Sample from Database:"
	if (len(persons) >= 30):
		persons = getPeopleFromDB()
		print 'First 15:'
		for i in range(0,15):
			print persons[i].stuNum, persons[i].name
		print '\nLast 15:'
		for i in range(len(persons)-15,len(persons)):
			print persons[i].stuNum, persons[i].name
	else:	
		print 'Less than 30 records, printing all.'
		for person in persons:
			print persons[i].stuNum, persons[i].name


def printSampleFromText(textfileName):
	print "Sample from",textfileName
	inputFile = open(textfileName,'r')
	records = []
	for record in inputFile:
		records.append(record.strip())
	if (len(records) >= 30):
		print 'First 15:'
		for i in range(0,15):
			print records[i]
		print '\nLast 15:'
		for i in range(len(records)-15,len(records)):
			print records[i]		
	else:	
		print 'Less than 30 records, printing all.'
		for record in records:
			print record

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
	
