from Media import Media
from datetime import datetime

# class DB_Handler():
# 	def __init__(self):
# 		self.msdb = MySQLDatabase('mediaskrape', user='mediaskrape', passwd=MS_PASSWORD, field_types={'image':'image'})
# 		self.msdb.create_tables([Media], safe=True)

# 	def add_media(self, media_type, time_posted=datetime.now(), text='', image=None):
# 		Media.insert(media_type=media_type, time_posted=time_posted, text=text, image=image).execute()

# 	def get_media_in_range(self, start_time, end_time):
# 		posts = Media.select().where(Media.time_posted >= start_time and Media.time_posted <= end_time)
# 		return posts