import os, csv, pymysql,sys
from db_connection import *


def rollback_Bird():
 
	is_success = True
	#safe_mode_stmt = "SET SQL_SAFE_UPDATES = 0"
	rollback_stmt = "delete from Bird" 
 
	try:
		connection = create_connection()
		cursor = connection.cursor()
 
		cursor.execute(rollback_stmt)
		connection.commit()

	except:
		except_test(is_success)

	end_connection(connection)
	return is_success

rollback_Bird()