from Media import Media

class DB_Handler():
	def __init__(self):
		self.msdb = MySQLDatabase('mediaskrape', user='mediaskrape', passwd=MS_PASSWORD, field_types={'image':'image'})
		msdb.create_tables([Media], safe=True)