import config
from SQLighter import SQLighter
from SQLighter import Record
def SQLInsertTest1():
	db_worker = SQLighter(config.database_name)

	obj = Record("Insert Test 1 message", 0001, 0000, 1000)

	msg = db_worker.insert_single(obj)

	db_worker.close()

	return "Complete"

def SQLSelectTest1():
	db_worker = SQLighter(config.database_name)

	fire_time = 1000

	list = db_worker.select_fire_list(fire_time)

	db_worker.close()

	print(list)
	return "Complete"

def SQLUpdateTest1():
	db_worker = SQLighter(config.database_name)

	fire_time = 1000

	list = db_worker.select_fire_list(fire_time)
	for obj in list:
		print(obj.period)
		obj.firetime += obj.period
	db_worker.update_fire_list(list)
	list = db_worker.select_fire_list(fire_time+100)
	db_worker.close()

	print(list)
	return "Complete"

if __name__ == '__main__':

	print(SQLInsertTest1())
	print(SQLSelectTest1())
	print(SQLUpdateTest1())