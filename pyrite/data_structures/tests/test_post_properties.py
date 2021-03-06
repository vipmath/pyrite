# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import unittest

from datetime import datetime

from .. import post_properties 

class TestPostProperties(unittest.TestCase):

  def test_title_compile(self):
    title = post_properties.Title("Title")
    self.assertEqual(title.compile(), ("<div "
      "class=\"post_title\">\nTitle\n</div>\n"))

  def test_post_body_compile(self):
    postbody = post_properties.PostBody("Body")
    self.assertEqual(postbody.compile(), ("<div "
      "class=\"post_body\">\nBody\n</div>\n"))

  def test_date_compile(self):
    now=datetime.now()
    date = post_properties.Date(now)
    self.assertEqual(date.compile(), ("<div "  
      "class=\"post_date\">\n"+str(now)+"\n</div>\n"))

if __name__ == '__main__':
  unittest.main()

