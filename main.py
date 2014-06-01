from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
	name = CharField()
	stuNum = IntegerField()
	
	class Meta:
		database = db


#Main
if Person.table_exists():
	Person.drop_table()

Person.create_table()

for i in range(0,15):
	Person.create( name = 'test'+str(i), stuNum = i+100)

for person in Person.select():
	print person.name, person.stuNum


