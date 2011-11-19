# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

from post_property import PostProperty
from datetime import datetime

class DateParser(object):
    def __init__(self, parse_type):
        self.parse_methods = ["%d/%m/%y", "%d/%m/%y %H:%M", "%d %B %Y"]
        self.cached_parsing = self.parse_methods[0]
        self.out_format = "%d %B %Y"

    def parse(self, string):
        parsed_date = self.getDatetime(string)
        if parsed_date == None:
            raise Exception("Unknown date format: " + string)
        else:
            return Date(parsed_date, self.out_format)

    def getDatetime(self, string):  
        parsed_date = None
        for method, index in zip(self.parse_methods, 
                                 range(len(self.parse_methods))):
            try: 
                parsed_date = datetime.strptime(string, method) 
            except: 
                pass 
            if parsed_date != None:
                break

        # This doesn't work quite yet:
        # if parsed_date != None:
        #    self.parse_methods = self.parse_methods.insert(0, 
        #            parse_methods.pop(index))
        return parsed_date


class Date(PostProperty):   
    """
    The Date Property stores a Date object locally until it comes time to
    create the HTML post, in which case it renders as a String 
    """
    def __init__(self, date, out_format):
        """
        Constructor should be accessed by parse method.
        """
        PostProperty.__init__(self, "post_date")    
        self.date = date
        self.out_format = out_format
        self.id_format = "%Y-%m-%d"

    def generate(self):    
        return PostProperty.generate(
            self, self.date.strftime(self.out_format))

    def to_string(self):
        return self.date.strftime(self.id_format)

    def display_ast(self, indents):
        indenting = indents * "  "
        return indenting + "Date:" + self.to_string() + "\n"


# Utility Methods 
def num_to_month(num): 
    num_dict = {
            1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June",
            7:"July", 8:"August", 9:"September",10:"October",11:"November",
            12:"December"
            }
    return num_dict.get(num)