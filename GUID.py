# -*- coding: utf-8 -*-
"""
Created on Sat May  1 21:21:26 2021

@author: William Ponton
Date: 5.1.21
Description: Specifications for the GUID class
"""

# GUID class specifications

class GUID:
    def __init__(myGUID, length, chunks):
        myGUID.length = length
        myGUID.chunks = chunks

    def get_guid_params(myGUID):
        return print("Length of GUID is {} and the number of chunks is {}".format(myGUID.length, myGUID.chunks))

    def get_guid_quantity():
        guid_quantity = print(input("How many GUIDs would you like to generate?"))
    return guid_quantity



myGUID = GUID(32, 4)
myGUID.get_guid_params()

# GUID class specifications

class GUID:
    def __init__(self, length, chunks):
        self.length = length
        self.chunks = chunks

    def get_guid_params(myGUID):
        return print("Length of GUID is {} and the number of chunks is {}".format(myGUID.length, myGUID.chunks))

# Test output
myGUID = GUID(32, 4)
myGUID.get_guid_params()