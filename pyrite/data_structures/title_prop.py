# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

from post_property import PostProperty

def parse(string): 
    return Title(string)

class Title(PostProperty):
    def __init__(self, title):
        """
        Constructor should be only accessed by parse method.
        """
        PostProperty.__init__(self, "post_title") 
        self.title = title

    def generate(self):    # self.divId is the name of the HTML class
        return PostProperty.generate(self, self.title)

    def to_string(self):
        return self.title
