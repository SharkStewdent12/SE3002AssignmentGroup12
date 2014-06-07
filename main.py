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
	
#Main

initialiseDatabase()

readToDB('lab3Input.txt')


persons = getPeopleFromDB()

#get flag for order
ASC = False
DESC = True
order = ASC
persons = sortPeople(persons,order)

for person in persons:
	print '-',person.stuNum, person.name
	#outputFile.write( str(person.stuNum) + ', ' + person.name + '\n')

for i in (range(0,15) + range(len(persons)-15,len(persons))):	
	outputFile.write( str(persons[i].stuNum) + ', ' + persons[i].name + '\n')


outputFile.close()
