import pymysql, sys
 


def create_connection():

													#should probably delete my password before i turn it in :^)
	conn = pymysql.connect(db='Endangered', user='root', passwd='fbbsfbbs327', host='localhost')	#Change user/password/host as needed!
	return conn


def rollback_Bird():
 
	is_success = True
	#safe_mode_stmt = "SET SQL_SAFE_UPDATES = 0"
	rollback_stmt = "delete from Bird" # had to add the last little bit to avoid MySQL's safe update mode from giving us an error
 
	try:
		connection = create_connection()
		cursor = connection.cursor()
 
		cursor.execute(rollback_stmt)
		connection.commit()
	except:
		print "Unexpected error:", sys.exc_info()[0]				#prints out the error type 
    	is_success= False											#changes boolean to failure :(
 
	return is_success

rollback_Bird()