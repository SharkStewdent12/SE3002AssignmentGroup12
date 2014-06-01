from peewee import *

db = SqliteDatabase('people.db')
inputFile = open('lab3Input.txt','r')

class Person(Model):
	name = CharField()
	stuNum = IntegerField()
	
	class Meta:
		database = db


#Main



if Person.table_exists():
	Person.drop_table()

Person.create_table()

#for i in range(0,15):
#	Person.create( name = 'test'+str(i), stuNum = i+100)

for record in inputFile:
	line =  record.split(',')
	recNum = int( line[0].strip() )
	recName = line[1].strip()
	Person.create( name = recName, stuNum = recNum)

for person in Person.select():
	print person.stuNum, person.name


