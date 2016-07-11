import config
from SQLighter import SQLighter
from SQLighter import Record
def SQLInsertTest1():
	db_worker = SQLighter(config.database_name)

	obj = Record("Insert Test 1 message", 0001, 0000, 1000)

	msg = db_worker.insert_single(obj)

	db_worker.close()

	return "Complete"


if __name__ == '__main__':

	print(SQLInsertTest1())