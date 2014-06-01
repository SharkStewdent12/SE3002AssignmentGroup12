from peewee import *

db = SqliteDatabase('people.db')
inputFile = open('lab3Input.txt','r')
outputFile = open('lab3Output.txt','w')

class Person(Model):
	name = CharField()
	stuNum = IntegerField()
	
	class Meta:
		database = db


#Main
if Person.table_exists():
	Person.drop_table()

Person.create_table()

for record in inputFile:
	line =  record.split(',')
	recNum = int( line[0].strip() )
	recName = line[1].strip()
	Person.create( name = recName, stuNum = recNum)

for person in Person.select():
	print person.stuNum, person.name

#Now for reading for output

persons = []
for person in Person.select():
	persons.append(person)

persons = sorted(persons, key=lambda person:person.stuNum)

for person in persons:
	print '-',person.stuNum, person.name
	#outputFile.write( str(person.stuNum) + ', ' + person.name + '\n')

for i in (range(0,15) + range(len(persons)-15,len(persons))):	
	outputFile.write( str(persons[i].stuNum) + ', ' + persons[i].name + '\n')


outputFile.close()
