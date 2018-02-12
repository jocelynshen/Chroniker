import peewee
from peewee import *

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
    media_type = FixedCharField() # one of t, f, i
    text = TextField(null=True, default='')
    image = BlobField(null=True, default=None) # TODO: handle multiple images
    uuid = UUIDField()

    class Meta:
        database = msdb
