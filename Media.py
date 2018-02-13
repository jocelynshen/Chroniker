import peewee
from peewee import *
import uuid
from datetime import datetime
from secrets import *

'''
Types of media:
- tweet
- instagram post
- facebook post
(these are to start with)

Fields:
- text
- image

'''

# class Media(Model):
#     media_type = FixedCharField(constraints=[Check('media_type in ["t", "f", "i"]')]) # one of t, f, i
#     text = TextField(null=True, default='')
#     image = BlobField(null=True, default=None) # TODO: handle multiple images
#     time_posted = DateTimeField()
#     uuid = UUIDField(default=uuid.uuid4, unique=True)

#     class Meta:
#         database = MySQLDatabase('mediaskrape', user='mediaskrape', passwd=MS_PASSWORD, field_types={'image':'image'}) #msdb

class Media():
    def __init__(self):
        pass