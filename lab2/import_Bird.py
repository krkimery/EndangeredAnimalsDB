#Script to populate Bird table in Endangered database
#Created by Kyle Kimery, with assitance from Ivy Markwell
#

import os, csv, pymysql,sys
from db_connection import *


	#function to import the data from the csv file to the SQL database
def import_Bird():

	is_success = True								#success/failure boolean
	insert_prefix = "insert into Bird (scientific_name, migratory_status) values ("		#SQL syntax to insert row
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

		

			#this for loop reads data from each entry and creates/executes insert statements in SQL
		for i in bird_list: 
			insert_statement = insert_prefix 
			for j in range(len(i)):
				
				if j == 2:
					sciName = i[j]
					insert_statement += "'" + sciName + "',"	#animal_type is manually put in here, assumed birds and mammals are properly segregated in the data source
				if j == 5:
					mStatus = i[j][0]
					insert_statement += "'" +mStatus+"')"
					cursor.execute(insert_statement)


		connection.commit()											#I don't really know what this does, but it makes it work :^)







	except:
		except_test(is_success)

	end_connection(connection)
	return is_success


test = import_Bird()									#Should probably use something other than "test" here... 