#Written by Matthew Unterslak 
from dbFunctions import *

try:
    initialiseDatabase()
    print "Database Initialised"
except:
    print "Database Initialisation Failed"

try:
    readToDB('Broken.txt')
    print "Textfile reading into database Passed"
except:
    print "Textfile contains errors. Test Failed."

try:
    printSampleFromDB()
    print "Print sample Passed"
except:
    print "Textfile contains less than 30 entries or blank entries encountered. Test Failed."
try:
    persons = getPeopleFromDB()
    print "Database reading Passed"
except:
    print "Database reading Failed. "
   
try:
    order = getOrderFlag()
    print "Order from user Passed."
except:
    print "Order not of type expected. Order from user Failed"

try:
    persons = sortPeople(persons,order)
    print "Sort entries Passed"
except:
    print "Sort Failed. "

try:
    writePeopleToText(persons,'lab3Output.txt')
    print "Writing to output file Passed"
except:
    print "Writing to output file Failed."

try:
    printSampleFromText('lab3Output.txt')
    print "Print sample from Text Passed"
except:
    print "The database contains less than 30 entries or blank entries encountered. Print Failed."
