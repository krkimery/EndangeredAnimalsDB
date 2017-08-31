
import pymysql
from db_connection import *

def print_menu():
	print "1. Show all animals with scientific names that begin with a specific letter"
	print "2. Count the number of migratory OR non-migratory (user-input required) birds in the database"
	print "3. Show the common name of the animals alongside the continent they inhabit"
	print "4. Show the common names of the birds by choosing their migratory status"
	print "5. Show the scientific names of animals and their continents"
	print "6. Show all animals and their migratory status if applicable"
	print "7. List the endangered status of an animal alongside its continent, ordered by continent"
	print "8. Count the number of animals with status \"E\" for endangered"
	print "9. List all of the continents that start with the letter \"A\""
	print "10. Show all animals that match a user-input string"
	print "11. Show all animals that are of the myotis family"
	print "12. Show all animals that are of the equus family"
	print "13. Show all animals that are of the Prionailurus family"
	print "14. Show all birds that have -re- names"
	print "15. Show all birds that have -ea- names"
	print "16. Show number oftweets about endangered animals by continent"
	print "17. Show number of retweets about endangered animals by Twitter username (inner join)"
	print "18. Show retweets by username (right join) sorted by # of retweets"
	print "19. Show number of tweets about endangered North American Animals"
	print "20. Show twitter usernames by country tweeted about"

	print "21. Exit the program"



def injectionProjection(input):
	x = input
	y = "; drop table"

	if y in x:
		return False
	

	y = "; truncate table"

	if y in x:
		return False
	

	y = "; delete from"

	if y in x:
		return False
	

	y = "or 1=1"

	if y in x:
		return False
	else:
		return True









#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~QUERY 1~~~~~~~~~~~~~~~~~~~~~~~~~~
def query1(letter):

	is_success = True
	query = "select scientific_name from Animal_Range group by Animal_Range.scientific_name having scientific_name like \'" + letter +"%\'"
 
	try: 
		connection = create_connection()
		cursor = connection.cursor()

		query_status = True
		try: 
			cursor.execute(query)
		except:
			query_status = False

		if query_status:
			is_success = True
		else:
			is_success = False

		results = cursor.fetchall()
		print ""    
		for row in results:
			print row
		print "" 

	except pymysql.Error as e:
		is_success = False
		print "Scientific Name query failed: " + e.strerror

	return is_success
	

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~QUERY 2~~~~~~~~~~~~~~~~~~~~~~~~~~    
def query2(isMigratory):
	tempChar = "Y"
	is_success = True
	if isMigratory:
		tempChar = "Y"
	else:
		tempChar = "N"
	query = "select count(*) NumBirds from Bird group by migratory_status having migratory_status = \""+tempChar+"\""
 
	try: 
		connection = create_connection()
		cursor = connection.cursor()

		query_status = True
		try: 
			cursor.execute(query)
		except:
			query_status = False

		if query_status:
			is_success = True
		else:
			is_success = False

		results = cursor.fetchall()
		print ""    
		for row in results:
			print row
		print "" 

	except pymysql.Error as e:
		is_success = False
		print "Number of migratory birds query failed: " + e.strerror

	return is_success

	
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~QUERY 3~~~~~~~~~~~~~~~~~~~~~~~~~~    
def query3():

	is_success = True
	query = "SELECT Endangered_Animal.common_name, Animal_Range.continent_name FROM Endangered_Animal INNER JOIN Animal_Range ON Endangered_Animal.scientific_name = Animal_Range.scientific_name ORDER BY Endangered_Animal.common_name;"
 
	try: 
		connection = create_connection()
		cursor = connection.cursor()

		query_status = True
		try: 
			cursor.execute(query)
		except:
			query_status = False

		if query_status:
			is_success = True
		else:
			is_success = False

		results = cursor.fetchall()
		print ""    
		for row in results:
			print row
		print ""

	except pymysql.Error as e:
		is_success = False
		print "Query failed: " + e.strerror

	return is_success


	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~QUERY 4~~~~~~~~~~~~~~~~~~~~~~~~~~    
def query4(isMigratory):
	tempChar = "Y"
	is_success = True
	if isMigratory:
		tempChar = "Y"
	else:
		tempChar = "N"
	is_success = True
	query = "SELECT Endangered_Animal.common_name, Bird.migratory_status FROM Endangered_Animal INNER JOIN Bird ON Endangered_Animal.scientific_name = Bird.scientific_name WHERE Bird.migratory_status = \""+tempChar+"\" ORDER BY Endangered_Animal.common_name;"
 
	try: 
		connection = create_connection()
		cursor = connection.cursor()

		query_status = True
		try: 
			cursor.execute(query)
		except:
			query_status = False

		if query_status:
			is_success = True
		else:
			is_success = False

		results = cursor.fetchall()
		print ""    
		for row in results:
			print row
		print "" 

	except pymysql.Error as e:
		is_success = False
		print "Query failed: " + e.strerror

	return is_success


	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~QUERY 5~~~~~~~~~~~~~~~~~~~~~~~~~~    
def query5(isMammal):
	tempChar = "M"
	is_success = True
	if isMammal:
		tempChar = "M"
	else:
		tempChar = "B"
	is_success = True
	query = "SELECT Endangered_Animal.common_name, Animal_Range.continent_name FROM Endangered_Animal INNER JOIN Animal_Range ON Endangered_Animal.scientific_name = Animal_Range.scientific_name WHERE Endangered_Animal.animal_type = \""+tempChar+"\" ORDER BY Animal_Range.continent_name;"
 
	try: 
		connection = create_connection()
		cursor = connection.cursor()

		query_status = True
		try: 
			cursor.execute(query)
		except:
			query_status = False

		if query_status:
			is_success = True
		else:
			is_success = False

		results = cursor.fetchall()
		print ""    
		for row in results:
			print row
		print "" 

	except pymysql.Error as e:
		is_success = False
		print "Query failed: " + e.strerror

	return is_success


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~QUERY 6~~~~~~~~~~~~~~~~~~~~~~~~~~    
def query6():

	is_success = True
	query = "SELECT Endangered_Animal.common_name, Bird.migratory_status FROM Endangered_Animal LEFT JOIN Bird ON Endangered_Animal.scientific_name = Bird.scientific_name ORDER BY Endangered_Animal.animal_type;"
 
	try: 
		connection = create_connection()
		cursor = connection.cursor()

		query_status = True
		try: 
			cursor.execute(query)
		except:
			query_status = False

		if query_status:
			is_success = True
		else:
			is_success = False

		results = cursor.fetchall()
		print ""    
		for row in results:
			print row
		print "" 

	except pymysql.Error as e:
		is_success = False
		print "Query failed: " + e.strerror

	return is_success



	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~QUERY 7~~~~~~~~~~~~~~~~~~~~~~~~~~    
def query7():

	is_success = True
	query = "SELECT Endangered_Animal.endangered_status, Animal_Range.continent_name FROM Endangered_Animal LEFT JOIN Animal_Range ON Endangered_Animal.scientific_name = Animal_Range.scientific_name ORDER BY Animal_Range.continent_name;"
 
	try: 
		connection = create_connection()
		cursor = connection.cursor()

		query_status = True
		try: 
			cursor.execute(query)
		except:
			query_status = False

		if query_status:
			is_success = True
		else:
			is_success = False

		results = cursor.fetchall()
		print ""    
		for row in results:
			print row
		print "" 

	except pymysql.Error as e:
		is_success = False
		print "Query failed: " + e.strerror

	return is_success



	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~QUERY 8~~~~~~~~~~~~~~~~~~~~~~~~~~    
def query8():

	is_success = True
	query = "SELECT COUNT(*) NumEnd FROM Endangered_Animal WHERE endangered_status = \"E\";"
 
	try: 
		connection = create_connection()
		cursor = connection.cursor()

		query_status = True
		try: 
			cursor.execute(query)
		except:
			query_status = False

		if query_status:
			is_success = True
		else:
			is_success = False

		results = cursor.fetchall()
		print ""    
		for row in results:
			print row
		print "" 

	except pymysql.Error as e:
		is_success = False
		print "Query failed: " + e.strerror

	return is_success

	

	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~QUERY 9~~~~~~~~~~~~~~~~~~~~~~~~~~    
def query9():

	is_success = True
	query = "SELECT DISTINCT continent_name FROM Continent WHERE continent_name like \"a%\";"
 
	try: 
		connection = create_connection()
		cursor = connection.cursor()

		query_status = True
		try: 
			cursor.execute(query)
		except:
			query_status = False

		if query_status:
			is_success = True
		else:
			is_success = False

		results = cursor.fetchall()
		print ""    
		for row in results:
			print row
		print "" 

	except pymysql.Error as e:
		is_success = False
		print "Query failed: " + e.strerror

	return is_success



	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~QUERY 10~~~~~~~~~~~~~~~~~~~~~~~~~~    
def query10(animalString):

	is_success = True
	query = "SELECT common_name FROM Endangered_Animal WHERE common_name like \"%" +animalString+"%\";"
 
	try: 
		connection = create_connection()
		cursor = connection.cursor()

		query_status = True
		try: 
			cursor.execute(query)
		except:
			query_status = False

		if query_status:
			is_success = True
		else:
			is_success = False

		results = cursor.fetchall()
		print ""    
		for row in results:
			print row
		print "" 

	except pymysql.Error as e:
		is_success = False
		print "Query failed: " + e.strerror

	return is_success


def query11():

	is_success = True
	view = "USE Endangered; CREATE VIEW AnimalNames AS SELECT scientific_name FROM Animal_Range;"
	query = "SELECT * FROM AnimalNames WHERE scientific_name like \"%myotis%\";"
	dropView = "drop view AnimalNames;"
 
	try: 
		connection = create_connection()
		cursor = connection.cursor()

		query_status = True
		try: 
			cursor.execute(view)
			cursor.execute(query)
		except:
			query_status = False

		if query_status:
			is_success = True
		else:
			is_success = False

		results = cursor.fetchall()
		print ""    
		for row in results:
			print row
		print "" 

		cursor.execute(dropView)

	except pymysql.Error as e:
		is_success = False
		print "Query failed: " + e.strerror

	return is_success

def query12():

	is_success = True
	view = "USE Endangered; CREATE VIEW AnimalNames AS SELECT scientific_name FROM Animal_Range;"
	query = "SELECT * FROM AnimalNames WHERE scientific_name like \"%Equus%\";"
	dropView = "drop view AnimalNames;"

 
	try: 
		connection = create_connection()
		cursor = connection.cursor()

		query_status = True
		try: 
			cursor.execute(view)
			cursor.execute(query)
		except:
			query_status = False

		if query_status:
			is_success = True
		else:
			is_success = False

		results = cursor.fetchall()
		print ""    
		for row in results:
			print row
		print "" 
		cursor.execute(dropView)

	except pymysql.Error as e:
		is_success = False
		print "Query failed: " + e.strerror

	return is_success

def query13():

	is_success = True
	view = "USE Endangered; CREATE VIEW AnimalNames AS SELECT scientific_name FROM Animal_Range;"
	query = "SELECT * FROM AnimalNames WHERE scientific_name like \"%Prionailurus%\";"
	dropView = "drop view AnimalNames;"

	try: 
		connection = create_connection()
		cursor = connection.cursor()

		query_status = True
		try: 
			cursor.execute(view)
			cursor.execute(query)
		except:
			query_status = False

		if query_status:
			is_success = True
		else:
			is_success = False

		results = cursor.fetchall()
		print ""    
		for row in results:
			print row
		print ""
		cursor.execute(dropView)

	except pymysql.Error as e:
		is_success = False
		print "Query failed: " + e.strerror

	return is_success

def query14():

	is_success = True
	view = "USE Endangered; CREATE VIEW BirdNames AS SELECT scientific_name FROM Bird;"
	query = "SELECT * FROM BirdNames WHERE scientific_name like \"%re%\";"
	dropView = "drop view BirdNames;"

	try: 
		connection = create_connection()
		cursor = connection.cursor()

		query_status = True
		try: 
			cursor.execute(view)
			cursor.execute(query)
		except:
			query_status = False

		if query_status:
			is_success = True
		else:
			is_success = False

		results = cursor.fetchall()
		print ""    
		for row in results:
			print row
		print "" 
		cursor.execute(dropView)

	except pymysql.Error as e:
		is_success = False
		print "Query failed: " + e.strerror

	return is_success

def query15():

	is_success = True
	view = "USE Endangered; CREATE VIEW BirdNames AS SELECT scientific_name FROM Bird;"
	query = "SELECT * FROM BirdNames WHERE scientific_name like \"%ea%\";"
	dropView = "drop view BirdNames;"

	try: 
		connection = create_connection()
		cursor = connection.cursor()

		query_status = True
		try: 
			cursor.execute(view)
			cursor.execute(query)
		except:
			query_status = False

		if query_status:
			is_success = True
		else:
			is_success = False

		results = cursor.fetchall()
		print ""    
		for row in results:
			print row
		print "" 
		cursor.execute(dropView)

	except pymysql.Error as e:
		is_success = False
		print "Query failed: " + e.strerror

	return is_success


def query16():
	is_success = True
	query = "select continent_name, count(*) tweet_count from Tweet group by continent_name order by tweet_count desc;"
	try: 
		connection = create_connection()
		cursor = connection.cursor()

		query_status = True
		try: 
			cursor.execute(query)
		except:
			query_status = False


		if query_status:
			is_success = True
		else:
			is_success = False

		results = cursor.fetchall()
		print results
		print ""    
		for row in results:
			print row
		print "" 

	except pymysql.Error as e:
		is_success = False
		print "Query failed: " + e.strerror

	return is_success

def query17():

	is_success = True
	query = "select screen_name, retweet_count from Tweet t inner join Continent c on t.continent_name = c.continent_name;"
 
	try: 
		connection = create_connection()
		cursor = connection.cursor()

		query_status = True
		try: 
			cursor.execute(query)
		except:
			query_status = False

		if query_status:
			is_success = True
		else:
			is_success = False

		results = cursor.fetchall()
		print ""    
		for row in results:
			 print row
		print "" 

	except pymysql.Error as e:
		is_success = False
		print "Query failed: " + e.strerror

	return is_success

def query18():

	is_success = True
	query = "select screen_name, retweet_count from Tweet t right join Continent c on t.continent_name =  c.continent_name;"
 
	try: 
		connection = create_connection()
		cursor = connection.cursor()

		query_status = True
		try: 
			cursor.execute(query)
		except:
			query_status = False

		if query_status:
			is_success = True
		else:
			is_success = False

		results = cursor.fetchall()
		print ""    
		for row in results:
			print row
		print "" 

	except pymysql.Error as e:
		is_success = False
		print "Query failed: " + e.strerror

	return is_success
def query19():

	is_success = True
	query = "select continent_name, count(*) tweet_count from Tweet where continent_name = \"North America\";"
 
	try: 
		connection = create_connection()
		cursor = connection.cursor()

		query_status = True
		try: 
			cursor.execute(query)
		except:
			query_status = False

		if query_status:
			is_success = True
		else:
			is_success = False

		results = cursor.fetchall()
		print ""    
		for row in results:
			print row
		print "" 

	except pymysql.Error as e:
		is_success = False
		print "Query failed: " + e.strerror

	return is_success

def query20():

	is_success = True
	query = "select c.continent_name, t.screen_name from Tweet t right join Continent c on t.continent_name = c.continent_name;"
 
	try: 
		connection = create_connection()
		cursor = connection.cursor()

		query_status = True
		try: 
			cursor.execute(query)
		except:
			query_status = False

		if query_status:
			is_success = True
		else:
			is_success = False

		results = cursor.fetchall()
		print ""    
		for row in results:
			print row
		print "" 

	except pymysql.Error as e:
		is_success = False
		print "Query failed: " + e.strerror

	return is_success

	
while True:          
	print_menu()   
	choice = raw_input("Enter your choice [1-21]: ")
	 
	if choice=="1": 
		validChoice = False  
		letter = " "  
		print "You have chosen to show animals whose names begin with a certain letter"
		while not validChoice:
			letter = raw_input("Please enter a single letter you wish to investigate: ")
			if len(letter)!= 1:
				validChoice = False
				print "Error, please only input a single letter"
			elif not letter.isalpha():
				validChoice = False
				print "Error, must enter a letter"
			elif not injectionProjection(letter):
				print "Error, invalid characters detected"
				validChoice = False
			else:
				validChoice = True

		query1(letter)
	elif choice=="2":
		validChoice = False
		isMigratory = True  
		letter = " "  
		print "You have chosen to view birds based upon their migratory status"
		while not validChoice:
			letter = raw_input("Please enter \'Y\' or \'y\' to view birds that migrate or any other character to view non-migrating birds: ")
			if letter =="Y" or letter == "y":
				validChoice = True 
				isMigratory = True  
			elif not injectionProjection(letter):
				print "Error, invalid characters detected"
				validChoice = False
			else:
				validChoice = True
				isMigratory = False

		query2(isMigratory)
	elif choice=="3":
		print "You have chosen view the common names and countries. Here are the results: "
		query3()
	elif choice=="4":
		validChoice = False
		isMigratory = True  
		letter = " "  
		print "You have chosen to view the birds and their migratory statuses. Here are the results: "
		while not validChoice:
			letter = raw_input("Please enter \'Y\' or \'y\' to view birds that migrate or any other character to view non-migrating birds: ")
			if letter =="Y" or letter == "y":
				validChoice = True 
				isMigratory = True  
			elif not injectionProjection(letter):
				print "Error, invalid characters detected"
				validChoice = False
			else:
				validChoice = True
				isMigratory = False
		query4(isMigratory)
	elif choice=="5":
		validChoice = False
		isMammal = True  
		letter = " "  
		print "You have chosen to show the animals' scientific names and continents by animal type."
		while not validChoice:
			letter = raw_input("Please enter \'M\' or \'m\' to view mammals, or any other character(s) to view birds: ")
			if letter =="M" or letter == "m":
				validChoice = True 
				isMammal = True  
			elif not injectionProjection(letter):
				print "Error, invalid characters detected"
				validChoice = False
			else:
				validChoice = True
				isMammal = False
		query5(isMammal)
	elif choice=="6":
		print "You have chosen to show all animals and their migratory status. Here are the results: "
		query6()
	elif choice=="7":
		print "You have chosen to see the ordered continent list of endangered statuses. Here are the results: "
		query7()
	elif choice=="8":
		print "You have chosen to count the number of endangered animals. Here is the result: "
		query8()
	elif choice=="9":
		print "You have chosen to see all of the contients that start with the letter\"A\"....Here are the results: "
		query9()
	elif choice=="10":
		print "You have selected a user-input search of the common animal names."
		validChoice = False  
		letter = " "  
		while not validChoice:
			letter = raw_input("Please enter a text string you wish to search for in the database: ")
			if not injectionProjection(letter):
				print "Error, invalid characters detected"
				validChoice = False
			else:
				validChoice = True

		query10(letter)
	elif choice=="11":
		print "You have chosen to view the myotis family. Here is the result: "
		query11()

	elif choice=="12":
		print "You have chosen to view the equus family. Here is the result: "
		query12()

	elif choice=="13":
		print "You have chosen to view the Prionailurus family. Here is the result: "
		query13()
	elif choice=="14":
		print "You have chosen to view -re- birds. Here is the result: "
		query14()
	elif choice=="15":
		print "You have chosen to view -ea- birds. Here is the result: "
		query15()
	elif choice=="16":
		print "You have chosen to view tweets about endangered animals by continent. Here is the result: "
		query16()
	elif choice=="17":
		print "You have chosen to Show number of retweets about endangered animals by Twitter username. Here is the result: "
		query17()
	elif choice=="18":
		print "You have choosen to show retweets by username (right join) results: "
		query18()
	elif choice=="19":
		print "You have chosen to view number of North American endangered tweets. Here is the result: "
		query19()
	elif choice=="20":
		print "You have chosen to view twitter usernames by country tweeted about. Here is the result: "
		query20()







	elif choice=="21":
		print "Exiting"
		break
	else:
		print "Invalid user input, try again."
