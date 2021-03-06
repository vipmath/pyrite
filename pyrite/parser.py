#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import re
import sys
import data_structures.blog

def buildParser(parse_type, options): 
  return Parser(parse_type, options)

class Parser(object): 
  def __init__(self, parse_type, options):
    self.options = options 
    self.blog_parser = data_structures.blog.BlogParser(parse_type, options)
    self.parse = self.toplevel_parser(parse_type)

  def toplevel_parser(self, parse_type):
    if parse_type == "yaml":
      return self.parse_yaml
    else:
      print("Unknown file type")
      sys.exit();

  #######################################
  # Below are the type-specific parsers #
  #######################################
  def parse_yaml(self, yaml_strs):
    """
    Parse a YAML post and return a Post object
    ---
    title: Post
    tags: code, fun, python
    date: 2 August 2011, 2:00
    ... / more tags / ...
    ---
    Blog post content
    """
    postlist_raw = []

    for string in yaml_strs: 
      sections =  string.split("---")
      labels_raw = {}

      for section in sections: 
        stripped = section.strip()
        if stripped == "": continue # Discard empty sections 
        if labels_raw == {}:
          # Do some basic parsing of the labels
          for line in stripped.split("\n"): 
            label, splitter, data = line.partition(":")
            labels_raw[label.strip()] = data.strip()
        else:
            # Append a new labels and content pair
            postlist_raw.append((labels_raw, stripped))
            labels_raw = {}

    return self.blog_parser.parse(postlist_raw) 

  def parse_markdown(self, md_str):
    raise Exception("Not implemented yet")

  def parse_html(self, html_str):
    """
    Takes HTML as string and returns a Post object

    General expectation for HTML: TODO 
    """ 
    raise Exception("Not implemented yet")
