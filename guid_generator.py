# -*- coding: utf-8 -*-
"""
Created on Sat May  1 21:13:27 2021

@author: William Ponton
Date: 5.1.21
guid_generator.py
description:
    creating functions to create guids by parameter
"""

# import libraries
# Import the random library and set the seed
import random
random.seed()





# guid_hex_generate()
# returns a string of HEX_CHARS [0 - 9, a - f, A- F]
# user defines length and chunks
# calls the hex_chunk function to inject hypens in chunks of [8, 4, 4, 4, 12]
def guid_hex_generate(length, chunks):
  HEX_CHARS = '0123456789abcdefABCDEF'
  hex_code = ''
  while len(hex_code) < 32:
    hex_code += random.choice(HEX_CHARS)
  # format hex_code into chunks with hyphen
  hex_code = hex_chunk(hex_code)
  return hex_code

# hex_chunk()
# accepts a string, hex_code
# validation that hex_code is 32 characters in length
# splits the string into chunks of [8, 4, 4, 4, 12]
# concatenates the blocks into the return string hex_code
def hex_chunk(hex_code):
    length_check = len(hex_code)
    if length_check != 32:
      return("Error - GUID is not 32 characters.\nHEX_CODE length: ".format(length_check))
    else:
      # block1 = 8 chars
      block1 = hex_code[0:8]
      # block2 = 4chars
      block2 = hex_code[8:12]
      # block3 = 4 chars
      block3 = hex_code[12:16]
      #block4 = 4 chars
      block4 = hex_code[16:20]
      # block5 = 12 chars
      block5 = hex_code[20:32]
      # concatenation with hyphens
      hex_code = block1 + "-" + block2 + "-" + block3 + "-" + block4 + "-" + block5
      # return hex_code
      return hex_code
