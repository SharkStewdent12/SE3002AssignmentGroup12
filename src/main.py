#Written by Mark Durrheim
from dbFunctions import *

initialiseDatabase()

readToDB('lab3Input.txt')

printSampleFromDB()

persons = getPeopleFromDB()

order = getOrderFlag()

persons = sortPeople(persons,order)

print '\n'

writePeopleToText(persons,'lab3Output.txt')

printSampleFromText('lab3Output.txt')
