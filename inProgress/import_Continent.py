#Script to populate Bird table in Endangered database
#Created by Kyle Kimery, with assitance from Ivy Markwell
#

import os, csv, pymysql,sys


	#navigate to directory where the datasource file is located... Maybe not ideal?
os.chdir("/home/kyle/Desktop/School/CS327E/lab1")	#Change this to where your file is!


	#function to create a connection to the local mySQL using pymysql stuff
def create_connection():

													#should probably delete my password before i turn it in :^)
	conn = pymysql.connect(db='Endangered', user='root', passwd='fbbsfbbs327', host='localhost')	#Change user/password/host as needed!
	return conn


	#function to import the data from the csv file to the SQL database
def import_Continent():

	is_success = True								#success/failure boolean
	insert_prefix = "insert into Continent (continent_name) values ("		#SQL syntax to insert row
	try:

		connection = create_connection()
		cursor = connection.cursor()

		csvfile = open('homeRangesEdited.csv', 'rb')		#this is the name of the file (in current directory!!)
		reader = csv.reader(csvfile)															#change the filename as needed!


		current_list = []							#several lists to hold the data from our CSV file
		mammal_list = []
		bird_list = []
		header_row = []


			#headers appear at top of the CSV file as well as in the middle, dividing the data in half vertically
			#the top ~half are the mammals, and the bottom ~half is birds
		for row in reader:
			if row[0]=="Mammals":
				current_list = mammal_list
			elif row[0] == "Birds":
				current_list = bird_list 			#The header that divides the data is in the 0th column
			elif row[4]=="":
				pass
			elif row[4]=="status":					#the header row has "status" in this location, hopefully no animals are named "status"
				header_row=row
			else:
				current_list.append(row)			#the lists are actually lists of lists (2D lists)

		used_continents =[]
		continents = ["North America", "South America", "Australia", "Asia", "Europe"]

			#this for loop reads data from each entry and creates/executes insert statements in SQL
		for i in bird_list: 
			insert_statement = insert_prefix 
			for j in range(len(i)):
				if j == 3:
					continent_list = i[j].split(",")
					for m in range(len(continent_list)):
						if continent_list[m].startswith(" "):
							continent_list[m] = continent_list[m][1:]
						if continent_list[m].endswith(" "):
							continent_list[m] = continent_list[m][:len(continent_list[m])]
						word = continent_list[m]
						if word in continents and word not in used_continents:
							insert_statement_new = insert_statement+"'" +word+"')"
							cursor.execute(insert_statement_new)
							used_continents.append(word)


		for i in mammal_list: 
			insert_statement = insert_prefix 
			for j in range(len(i)):
				if j == 3:
					continent_list = i[j].split(",")
					for m in range(len(continent_list)):
						if continent_list[m].startswith(" "):
							continent_list[m] = continent_list[m][1:]
						if continent_list[m].endswith(" "):
							continent_list[m] = continent_list[m][:len(continent_list[m])]
						word = continent_list[m]
						if word in continents and word not in used_continents:
							insert_statement_new = insert_statement+"'" +word+"')"
							cursor.execute(insert_statement_new)
							used_continents.append(word)



		connection.commit()											#I don't really know what this does, but it makes it work :^)







	except:
		print "Unexpected error:", sys.exc_info()[0]				#prints out the error type 
    	is_success= False											#changes boolean to failure :(

	return is_success


test = import_Continent()									#Should probably use something other than "test" here... 