import sqlite3


class Record:

	def __init__(self, msgtext, userid, firetime, period):
		self.msgid = 0
		self.msgtext = msgtext
		self.userid = userid
		self.firetime = firetime
		self.period = period


class SQLighter:

	def __init__(self, database):
		self.connection = sqlite3.connect(database)
		self.cursor = self.connection.cursor()

	def select_fire_list(self, fire_time):
		with self.connection:
			return self.cursor.execute('SELECT * FROM messages where firetime < ?', (fire_time,)).fetchall()

	def update_fire_list(self, list):
		with self.connection:
			for obj in list:
				self.cursor.execute('UPDATE messages set firetime = ? where msgid=?', (list.firetime, list.msgid,))
			self.connection.commit()

	def select_single(self, rownum):
		with self.connection:
			return self.cursor.execute('SELECT * FROM messages WHERE msgid = ?',(rownum,)).fetchall()[0]

	def insert_single(self, obj):
		with self.connection:
			self.cursor.execute('INSERT INTO messages VALUES(null, ?, ?, ?, ?)', (obj.msgtext, obj.userid, obj.firetime, obj.period,))
			self.connection.commit()


	def count_rows(self):
		with self.connection:
			result = self.cursor.execute('SELECT * FROM messages').fetchall()
			return len(result)

	def close(self):
		self.connection.close()

