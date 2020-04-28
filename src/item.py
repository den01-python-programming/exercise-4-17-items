from datetime import datetime as dt

class Item:

    def __init__(self,name):
        self.name = name
        self.created_at = dt.now()

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name + " (created at: " + str(self.created_at) + ")"
