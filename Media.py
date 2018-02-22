#import peewee
#from peewee import *
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

class Media(Model):
    # media_type = FixedCharField(constraints=[Check('media_type in ["t", "f", "i"]')]) # one of t, f, i
    media_type = FixedCharField()
    text = TextField(null=True, default='')
    # image = BlobField(null=True) # TODO: handle multiple images
    image=TextField(null=True) # just hold the urls for now
    time_posted = DateTimeField()
    uuid = UUIDField(default=uuid.uuid4, unique=True)

    class Meta:
        database = MySQLDatabase('mediaskrape', user='mediaskrape', passwd=MS_PASSWORD, field_types={'image':'image'})
