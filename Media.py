"""Each media object holds the type of media, the date that media was created, and the contents """
class Media:
    def __init__(self, media_type, date, contents):
        self.media_type = media_type
        self.date = date
        self.contents = contents

    def get_contents():
        return self.contents

    def set_contents(data):
        self.contents = data
        return self.contents
        
    def __str__(self):
        return "Type: " + str(self.media_type) + "; Date: " + str(self.date) + "; Contents: " + str(self.contents)
