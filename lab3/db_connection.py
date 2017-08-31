#This script contains all the reusable code for the execution of main.py, along with
#each of the various import and rollback statements. 
#Created by Kyle Kimery and Ivy Markwell
#CS327E
#10/17/16

import pymysql, os, sys, csv


#This function creates a pymysql connection for further use
def create_connection():
													#should probably delete my password before i turn it in :^)
	conn = pymysql.connect(db='Endangered', user='root', passwd='password', host='localhost')	#Change user/password/host as needed!
	return conn 	#returns the connection variable 


#a function to close the connection at the end of use
def end_connection(connection):
	connection.close()


#a function for the error/exception handling of each of the sub-scripts
#this is how the errors are handled
def except_test(is_success):
	
	if sys.exc_info()[0] == None:
		pass
	else:	
		print "Error! ", sys.exc_info()[0] 	#prints out the error message that is received
		is_success = False

	return is_success	


